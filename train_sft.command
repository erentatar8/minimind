#!/bin/bash

# MiniMind Türkçe SFT Otomatik Eğitim Betiği
# MacBook Air M4 için optimize edilmiştir (caffeinate ile uyku engelleme, MPS hızlandırma)

cd "$(dirname "$0")"

# Sanal ortamı aktifleştir
source .venv/bin/activate

# Log ve çıktı klasörlerini oluştur
mkdir -p out checkpoints

echo "=================================================="
echo "🚀 MiniMind Türkçe SFT Eğitimi Başlatılıyor..."
echo "📍 Cihaz: Apple Silicon M4 (MPS)"
echo "📊 Veri Seti: dataset/sft_turkce.jsonl (56.782 örnek)"
echo "☕ caffeinate devrede: Ekran kapansa da Mac uyumayacak."
echo "📝 Loglar: out/train_sft.log dosyasına da yazılıyor."
echo "=================================================="
echo ""

# caffeinate -i: İşlem sürdüğü müddetçe sistemin uykuya geçmesini engeller
# PYTHONUNBUFFERED=1: Terminal loglarının anında akmasını sağlar
caffeinate -i env PYTHONUNBUFFERED=1 python trainer/train_full_sft.py \
    --device mps \
    --batch_size 8 \
    --accumulation_steps 4 \
    --max_seq_len 384 \
    --learning_rate 1e-5 \
    --epochs 1 \
    --log_interval 20 \
    --save_interval 500 \
    --save_weight full_sft_tr \
    --data_path dataset/sft_turkce.jsonl \
    --from_resume 1 \
    2>&1 | tee -a out/train_sft.log

STATUS=$?

echo ""
echo "=================================================="
if [ $STATUS -eq 0 ]; then
    echo "🎉 Eğitim Başarıyla Tamamlandı!"
    osascript -e 'display notification "MiniMind Türkçe SFT Eğitimi Tamamlandı!" with title "MiniMind 🚀"'
    afplay /System/Library/Sounds/Glass.aiff
else
    echo "⚠️ Eğitim bir hatayla veya kullanıcı tarafından durduruldu (Çıkış Kodu: $STATUS)."
fi
echo "=================================================="

echo "Pencereyi kapatabilirsiniz."
