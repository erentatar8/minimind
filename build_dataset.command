#!/bin/bash

# MiniMind Türkçe Ön Eğitim Verisi İndirici
cd "$(dirname "$0")"
source .venv/bin/activate

echo "=================================================="
echo "📚 Türkçe Vikipedi Külliyatı İndiriliyor..."
echo "=================================================="

python dataset/build_turkish_pretrain.py --max_samples 75000

echo ""
echo "🎉 Veri seti hazır: dataset/pretrain_turkce.jsonl"
osascript -e 'display notification "Türkçe Pretraining Veri Seti Hazır!" with title "MiniMind 📚"'
afplay /System/Library/Sounds/Glass.aiff
