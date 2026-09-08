#!/bin/bash

# MiniMind Muzip Asistan (Muzip LoRA) Adaptör Eğitimi
# Apple Silicon M4 MPS için optimize edilmiştir

cd "$(dirname "$0")"

# Sanal ortamı aktifleştir
source .venv/bin/activate

mkdir -p out checkpoints

echo "=================================================="
echo "🎭 MiniMind Muzip LoRA (Sarkastik Asistan) Eğitimi"
echo "📍 Temel Model: out/full_sft_tr_768.pth"
echo "📊 Veri Seti: dataset/lora_muzip.jsonl"
echo "⚡ Cihaz: Apple Silicon M4 (MPS)"
echo "☕ caffeinate devrede"
echo "=================================================="
echo ""

caffeinate -i env PYTHONUNBUFFERED=1 python trainer/train_lora.py \
    --device mps \
    --from_weight full_sft_tr \
    --lora_name lora_muzip \
    --data_path dataset/lora_muzip.jsonl \
    --epochs 3 \
    --batch_size 16 \
    --accumulation_steps 1 \
    --max_seq_len 384 \
    --learning_rate 5e-5 \
    --log_interval 10 \
    --save_interval 50 \
    --from_resume 0 \
    2>&1 | tee -a out/train_lora.log

STATUS=$?

echo ""
echo "=================================================="
if [ $STATUS -eq 0 ]; then
    echo "🎉 Muzip LoRA Adaptörü Başarıyla Eğitildi!"
    echo "📍 Kaydedildi: out/lora_muzip_768.pth"
    osascript -e 'display notification "Muzip LoRA Adaptörü Hazır!" with title "MiniMind 🎭"'
    afplay /System/Library/Sounds/Glass.aiff
else
    echo "⚠️ Eğitim durduruldu veya bir sorun oluştu (Çıkış: $STATUS)."
fi
echo "=================================================="
echo "Pencereyi kapatabilirsiniz."
