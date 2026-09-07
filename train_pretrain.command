#!/bin/bash

# MiniMind Türkçe Pretraining (Ön Eğitim) Otomatik Başlatıcı
# MacBook Air M4 için optimize edilmiştir (caffeinate ile uyku engelleme, MPS hızlandırma)

cd "$(dirname "$0")"

# Sanal ortamı aktifleştir
source .venv/bin/activate

# Log ve çıktı klasörlerini oluştur
mkdir -p out checkpoints

echo "=================================================="
echo "🚀 MiniMind Türkçe Pretraining (Ön Eğitim) Başlatılıyor..."
echo "📍 Cihaz: Apple Silicon M4 (MPS)"
echo "📊 Veri Seti: dataset/pretrain_turkce.jsonl"
echo "☕ caffeinate devrede: Ekran kapansa da Mac uyumayacak."
echo "📝 Loglar: out/train_pretrain.log dosyasına da yazılıyor."
echo "=================================================="
echo ""

# caffeinate -i: İşlem sürdüğü müddetçe sistemin uykuya geçmesini engeller
# PYTHONUNBUFFERED=1: Terminal loglarının anında akmasını sağlar
caffeinate -i env PYTHONUNBUFFERED=1 python trainer/train_pretrain.py \
    --device mps \
    --batch_size 16 \
    --accumulation_steps 4 \
    --max_seq_len 340 \
    --learning_rate 5e-4 \
    --epochs 1 \
    --log_interval 50 \
    --save_interval 1000 \
    --save_weight pretrain_tr \
    --data_path dataset/pretrain_turkce.jsonl \
    --from_resume 1 \
    2>&1 | tee -a out/train_pretrain.log

STATUS=$?

echo ""
echo "=================================================="
if [ $STATUS -eq 0 ]; then
    echo "🎉 Ön Eğitim Başarıyla Tamamlandı!"
    osascript -e 'display notification "MiniMind Türkçe Pretraining Tamamlandı!" with title "MiniMind 🚀"'
    afplay /System/Library/Sounds/Glass.aiff
else
    echo "⚠️ Eğitim bir hatayla veya kullanıcı tarafından durduruldu (Çıkış Kodu: $STATUS)."
fi
echo "=================================================="

echo "Pencereyi kapatabilirsiniz."
