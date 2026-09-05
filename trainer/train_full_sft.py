import os
import sys

__package__ = "trainer"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datasets  # noqa: F401  # Windows pyarrow/torch DLL conflict workaround (issue #771)
import argparse
import time
import warnings
import torch
import torch.distributed as dist
from contextlib import nullcontext
from torch import optim, nn
from torch.nn.parallel import DistributedDataParallel
from torch.utils.data import DataLoader, DistributedSampler
from model.model_minimind import MiniMindConfig
from dataset.lm_dataset import SFTDataset
from trainer.trainer_utils import get_lr, Logger, is_main_process, lm_checkpoint, init_distributed_mode, setup_seed, init_model, SkipBatchSampler

warnings.filterwarnings('ignore')


def train_epoch(epoch, loader, iters, start_step=0, wandb=None):
    start_time = time.time()
    last_step = start_step
    for step, (input_ids, labels) in enumerate(loader, start=start_step + 1):
        input_ids = input_ids.to(args.device)
        labels = labels.to(args.device)
        last_step = step
        lr = get_lr(epoch * iters + step, args.epochs * iters, args.learning_rate)
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr

        with autocast_ctx:
            res = model(input_ids, labels=labels)
            loss = res.loss + res.aux_loss
            loss = loss / args.accumulation_steps

        scaler.scale(loss).backward()

        if step % args.accumulation_steps == 0:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)

            scaler.step(optimizer)
            scaler.update()

            optimizer.zero_grad(set_to_none=True)

        if step % args.log_interval == 0 or step == iters:
            spend_time = time.time() - start_time
            current_loss = loss.item() * args.accumulation_steps
            current_aux_loss = res.aux_loss.item() if res.aux_loss is not None else 0.0
            current_logits_loss = current_loss - current_aux_loss
            current_lr = optimizer.param_groups[-1]['lr']
            eta_min = spend_time / max(step - start_step, 1) * (iters - step) // 60
            Logger(f'Epoch:[{epoch + 1}/{args.epochs}]({step}/{iters}), loss: {current_loss:.4f}, logits_loss: {current_logits_loss:.4f}, aux_loss: {current_aux_loss:.4f}, lr: {current_lr:.8f}, epoch_time: {eta_min:.1f}min')
            if wandb: wandb.log({"loss": current_loss, "logits_loss": current_logits_loss, "aux_loss": current_aux_loss, "learning_rate": current_lr, "epoch_time": eta_min})

        if (step % args.save_interval == 0 or step == iters) and is_main_process():
            model.eval()
            moe_suffix = '_moe' if lm_config.use_moe else ''
            ckp = f'{args.save_dir}/{args.save_weight}_{lm_config.hidden_size}{moe_suffix}.pth'
            raw_model = model.module if isinstance(model, DistributedDataParallel) else model
            raw_model = getattr(raw_model, '_orig_mod', raw_model)
            state_dict = raw_model.state_dict()
            torch.save({k: v.half().cpu() for k, v in state_dict.items()}, ckp)
            lm_checkpoint(lm_config, weight=args.save_weight, model=model, optimizer=optimizer, 
                         epoch=epoch, step=step, wandb=wandb, save_dir='../checkpoints', scaler=scaler)
            model.train()
            del state_dict

        del input_ids, labels, res, loss

    if last_step > start_step and last_step % args.accumulation_steps != 0:
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)


if __name__ == "__main__":
    default_out = "../out" if os.path.exists("../out") else "out"
    default_data = "../dataset/sft_turkce.jsonl" if os.path.exists("../dataset/sft_turkce.jsonl") else "dataset/sft_turkce.jsonl"
    default_ckp = "../checkpoints" if os.path.exists("../checkpoints") else "checkpoints"

    parser = argparse.ArgumentParser(description="MiniMind Full SFT")
    parser.add_argument("--save_dir", type=str, default=default_out, help="Model kayıt dizini")
    parser.add_argument('--save_weight', default='full_sft', type=str, help="Kayıt ağırlık dosya öneki")
    parser.add_argument("--epochs", type=int, default=2, help="Eğitim tur (epoch) sayısı")
    parser.add_argument("--batch_size", type=int, default=16, help="Batch boyutu")
    parser.add_argument("--learning_rate", type=float, default=1e-5, help="Başlangıç öğrenme oranı (learning rate)")
    parser.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu"), help="Eğitim cihazı (cuda / mps / cpu)")
    parser.add_argument("--dtype", type=str, default="bfloat16", help="Karma hassasiyet tipi (bfloat16 / float16)")
    parser.add_argument("--num_workers", type=int, default=0 if sys.platform == "darwin" else 8, help="Veri yükleme iş parçacığı sayısı (macOS için varsayılan 0)")
    parser.add_argument("--accumulation_steps", type=int, default=8, help="Gradyan biriktirme adımı")
    parser.add_argument("--grad_clip", type=float, default=1.0, help="Gradyan kırpma (clipping) eşiği")
    parser.add_argument("--log_interval", type=int, default=100, help="Log yazdırma sıklığı (adım)")
    parser.add_argument("--save_interval", type=int, default=1000, help="Model kaydetme sıklığı (adım)")
    parser.add_argument('--hidden_size', default=768, type=int, help="Gizli katman boyutu (hidden size)")
    parser.add_argument('--num_hidden_layers', default=8, type=int, help="Gizli katman sayısı")
    parser.add_argument('--max_seq_len', default=512, type=int, help="Maksimum dizi uzunluğu (sequence length)")
    parser.add_argument('--use_moe', default=0, type=int, choices=[0, 1], help="MoE mimarisi kullanılsın mı? (0=Hayır, 1=Evet)")
    parser.add_argument('--seed', default=42, type=int, help="Rastgelelik tohumu (random seed)")
    parser.add_argument("--data_path", type=str, default=default_data, help="SFT eğitim veri seti yolu")
    parser.add_argument('--from_weight', default='none', type=str, help="Hangi ağırlıktan başlanacağı (örn: pretrain, sıfırdan başlamak için none)")
    parser.add_argument('--from_resume', default=0, type=int, choices=[0, 1], help="Kaldığı checkpoint'ten otomatik devam etsin mi? (0=Hayır, 1=Evet)")
    parser.add_argument("--use_wandb", action="store_true", help="Wandb / Swanlab takibi aktif edilsin mi?")
    parser.add_argument("--wandb_project", type=str, default="MiniMind-Full-SFT", help="Wandb proje adı")
    parser.add_argument("--use_compile", default=0, type=int, choices=[0, 1], help="torch.compile hızlandırması kullanılsın mı? (0=Hayır, 1=Evet)")
    args = parser.parse_args()

    # ========== 1. Ortam ve Rastgelelik Tohumu ==========
    local_rank = init_distributed_mode()
    if dist.is_initialized(): args.device = f"cuda:{local_rank}"
    setup_seed(args.seed + (dist.get_rank() if dist.is_initialized() else 0))
    
    # ========== 2. Dizinler, Model Parametreleri, Checkpoint Kontrolü ==========
    os.makedirs(args.save_dir, exist_ok=True)
    os.makedirs(default_ckp, exist_ok=True)
    lm_config = MiniMindConfig(hidden_size=args.hidden_size, num_hidden_layers=args.num_hidden_layers, use_moe=bool(args.use_moe))
    ckp_data = lm_checkpoint(lm_config, weight=args.save_weight, save_dir=default_ckp) if args.from_resume==1 else None
    
    # ========== 3. Karma Hassasiyet (Mixed Precision) Ayarı ==========
    device_type = "cuda" if "cuda" in args.device else ("mps" if "mps" in args.device else "cpu")
    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
    if device_type == "cuda":
        autocast_ctx = torch.cuda.amp.autocast(dtype=dtype)
    elif device_type == "mps":
        autocast_ctx = torch.amp.autocast(device_type="mps", dtype=dtype)
    else:
        autocast_ctx = nullcontext()
    
    # ========== 4. Wandb Yapılandırması ==========
    wandb = None
    if args.use_wandb and is_main_process():
        import swanlab as wandb
        wandb_id = ckp_data.get('wandb_id') if ckp_data else None
        resume = 'must' if wandb_id else None
        wandb_run_name = f"MiniMind-Full-SFT-Epoch-{args.epochs}-BatchSize-{args.batch_size}-LearningRate-{args.learning_rate}"
        wandb.init(project=args.wandb_project, name=wandb_run_name, id=wandb_id, resume=resume)
    
    # ========== 5. Model, Veri Seti ve Optimizatör ==========
    model, tokenizer = init_model(lm_config, args.from_weight, save_dir=args.save_dir, device=args.device)
    train_ds = SFTDataset(args.data_path, tokenizer, max_length=args.max_seq_len)
    train_sampler = DistributedSampler(train_ds) if dist.is_initialized() else None
    scaler = torch.amp.GradScaler(device_type, enabled=(args.dtype == 'float16'))
    optimizer = optim.AdamW(model.parameters(), lr=args.learning_rate)
    
    # ========== 6. Checkpoint'ten Durum Kurtarma ==========
    start_epoch, start_step = 0, 0
    if ckp_data:
        model.load_state_dict(ckp_data['model'])
        optimizer.load_state_dict(ckp_data['optimizer'])
        scaler.load_state_dict(ckp_data['scaler'])
        start_epoch = ckp_data['epoch']
        start_step = ckp_data.get('step', 0)
    
    # ========== 7. Derleme ve Dağıtık Sarmalama ==========
    if args.use_compile == 1:
        model = torch.compile(model)
        Logger('torch.compile aktif edildi')
    if dist.is_initialized():
        model = DistributedDataParallel(model, device_ids=[local_rank])
    
    # ========== 8. Eğitimi Başlat ==========
    for epoch in range(start_epoch, args.epochs):
        train_sampler and train_sampler.set_epoch(epoch)
        setup_seed(args.seed + epoch); indices = torch.randperm(len(train_ds)).tolist()
        skip = start_step if (epoch == start_epoch and start_step > 0) else 0
        batch_sampler = SkipBatchSampler(train_sampler or indices, args.batch_size, skip)
        loader = DataLoader(train_ds, batch_sampler=batch_sampler, num_workers=args.num_workers, pin_memory=(device_type == "cuda"))
        if skip > 0: 
            Logger(f'Epoch [{epoch + 1}/{args.epochs}]: İlk {start_step} adım atlanıyor, adım {start_step + 1} üzerinden devam ediliyor')
            train_epoch(epoch, loader, len(loader) + skip, start_step, wandb)
        else:
            train_epoch(epoch, loader, len(loader), 0, wandb)
    
    # ========== 9. Dağıtık Süreçleri Temizle ==========
    if dist.is_initialized():
        dist.barrier()
        dist.destroy_process_group()