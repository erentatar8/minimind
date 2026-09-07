#!/bin/bash

# MiniMind Türkçe Pretrain Modeli Test Başlatıcı
# out/pretrain_tr_768.pth ağırlıklarını Apple Silicon M4 MPS üzerinde çalıştırır

cd "$(dirname "$0")"

# Sanal ortamı aktifleştir
source .venv/bin/activate

echo "=================================================="
echo "🧠 MiniMind Türkçe Pretrain Model Çıkarım Testi"
echo "📍 Yüklenen Ağırlık: out/pretrain_tr_768.pth"
echo "⚡ Cihaz: Apple Silicon M4 (MPS)"
echo "=================================================="
echo "💡 İpucu: Bu bir Ön Eğitim (Pretrain) modelidir."
echo "   Soru-cevap sohbeti yerine metin tamamlama yapar."
echo "   Örnek: 'Türkiye Cumhuriyeti,' veya 'Galatasaray, 2000 yılında'"
echo "=================================================="
echo ""

python eval_llm.py --weight pretrain_tr --device mps
