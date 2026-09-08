#!/bin/bash

# MiniMind Muzip LoRA (Sarkastik Asistan) Test Başlatıcı
cd "$(dirname "$0")"
source .venv/bin/activate

echo "=================================================="
echo "🎭 MiniMind Muzip Modu (Sarkastik Asistan) Başlatılıyor..."
echo "📍 Temel Model: out/full_sft_tr_768.pth"
echo "📍 LoRA Adaptörü: out/lora_muzip_768.pth"
echo "⚡ Cihaz: Apple Silicon M4 (MPS)"
echo "=================================================="
echo ""

python eval_llm.py --weight full_sft_tr --lora_weight lora_muzip --device mps
