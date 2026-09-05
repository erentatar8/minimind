import os
import time
import argparse
import random
import warnings
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from model.model_minimind import MiniMindConfig, MiniMindForCausalLM
from model.model_lora import *
from trainer.trainer_utils import setup_seed, get_model_params
warnings.filterwarnings('ignore')

def init_model(args):
    tokenizer = AutoTokenizer.from_pretrained(args.load_from)
    if 'model' in args.load_from:
        model = MiniMindForCausalLM(MiniMindConfig(
            hidden_size=args.hidden_size,
            num_hidden_layers=args.num_hidden_layers,
            use_moe=bool(args.use_moe),
            inference_rope_scaling=args.inference_rope_scaling
        ))
        moe_suffix = '_moe' if args.use_moe else ''
        ckp = f'./{args.save_dir}/{args.weight}_{args.hidden_size}{moe_suffix}.pth'
        model.load_state_dict(torch.load(ckp, map_location=args.device), strict=True)
        if args.lora_weight != 'None':
            apply_lora(model)
            load_lora(model, f'./{args.save_dir}/{args.lora_weight}_{args.hidden_size}.pth')
    else:
        model = AutoModelForCausalLM.from_pretrained(args.load_from, trust_remote_code=True)
    get_model_params(model, model.config)
    return model.half().eval().to(args.device), tokenizer

def main():
    default_w = 'full_sft_tr' if os.path.exists('out/full_sft_tr_768.pth') else 'full_sft'
    parser = argparse.ArgumentParser(description="MiniMind Model Çıkarımı ve Sohbet")
    parser.add_argument('--load_from', default='model', type=str, help="Model yükleme yolu (model=yerel torch ağırlıkları, diğer yollar=transformers formatı)")
    parser.add_argument('--save_dir', default='out', type=str, help="Model ağırlık dizini")
    parser.add_argument('--weight', default=default_w, type=str, help="Ağırlık adı öneki (pretrain, full_sft, full_sft_tr, rlhf, reason)")
    parser.add_argument('--lora_weight', default='None', type=str, help="LoRA ağırlık adı (None=kullanma, örn: lora_identity, lora_medical)")
    parser.add_argument('--hidden_size', default=768, type=int, help="Gizli katman boyutu (hidden_size)")
    parser.add_argument('--num_hidden_layers', default=8, type=int, help="Gizli katman sayısı")
    parser.add_argument('--use_moe', default=0, type=int, choices=[0, 1], help="MoE mimarisi kullanılsın mı (0=Hayır, 1=Evet)")
    parser.add_argument('--inference_rope_scaling', default=False, action='store_true', help="RoPE konumsal kodlama ekstrapolasyonunu etkinleştir")
    parser.add_argument('--max_new_tokens', default=8192, type=int, help="Maksimum yeni belirteç sayısı")
    parser.add_argument('--temperature', default=0.85, type=float, help="Örnekleme sıcaklığı (0-1 arası, yükseldikçe yaratıcılık artar)")
    parser.add_argument('--top_p', default=0.95, type=float, help="Nucleus örnekleme eşiği (0-1)")
    parser.add_argument('--open_thinking', default=0, type=int, help="Uyarlanabilir düşünmeyi etkinleştir (0=Hayır, 1=Evet)")
    parser.add_argument('--historys', default=0, type=int, help="Diyalog geçmişi tur sayısı (çift sayı olmalı, 0=geçmişsiz)")
    parser.add_argument('--show_speed', default=1, type=int, help="Üretim hızını göster (tokens/s)")
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu'), type=str, help="Çalıştırma donanımı (cuda, mps, cpu)")
    args = parser.parse_args()
    
    prompts = [
        'Bize kendini tanıtır mısın?',
        'Gökyüzü neden mavidir?',
        'Python ile Fibonacci dizisini hesaplayan bir fonksiyon yaz.',
        'Fotosentezin temel aşamalarını kısaca açıkla.',
        'Yapay zeka ve makine öğrenmesi arasındaki temel fark nedir?',
        'Evde kedi mi yoksa köpek mi beslemek daha avantajlıdır?',
        'Merkezi Limit Teoremi istatistikte neden bu kadar önemlidir?',
        'Türk mutfağının en meşhur lezzetlerinden bazılarını önerir misin?'
    ]
    
    conversation = []
    model, tokenizer = init_model(args)
    input_mode = int(input('[0] Otomatik Test Soruları\n[1] Canlı Sohbet (Kendin Yaz)\nSeçiminiz: '))
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    prompt_iter = prompts if input_mode == 0 else iter(lambda: input('💬: '), '')
    for prompt in prompt_iter:
        setup_seed(random.randint(0, 31415926))
        if input_mode == 0: print(f'💬: {prompt}')
        conversation = conversation[-args.historys:] if args.historys else []
        conversation.append({"role": "user", "content": prompt})
        if 'pretrain' in args.weight:
            inputs = tokenizer.bos_token + prompt
        else:
            inputs = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True, open_thinking=bool(args.open_thinking))
        
        inputs = tokenizer(inputs, return_tensors="pt", truncation=True).to(args.device)

        print('🧠: ', end='')
        st = time.time()
        generated_ids = model.generate(
            inputs=inputs["input_ids"], attention_mask=inputs["attention_mask"],
            max_new_tokens=args.max_new_tokens, do_sample=True, streamer=streamer,
            pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id,
            top_p=args.top_p, temperature=args.temperature, repetition_penalty=1
        )
        response = tokenizer.decode(generated_ids[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)
        conversation.append({"role": "assistant", "content": response})
        gen_tokens = len(generated_ids[0]) - len(inputs["input_ids"][0])
        print(f'\n[Speed]: {gen_tokens / (time.time() - st):.2f} tokens/s\n\n') if args.show_speed else print('\n\n')

if __name__ == "__main__":
    main()