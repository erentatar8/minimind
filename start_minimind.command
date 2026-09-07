#!/bin/bash

# MiniMind Web Arayüzü Başlatıcı
cd "$(dirname "$0")"

# Sanal ortamı aktifleştir
source .venv/bin/activate

echo "=================================================="
echo "🌐 MiniMind WebUI Başlatılıyor..."
echo "📍 Adres: http://localhost:8501"
echo "=================================================="

streamlit run scripts/web_demo.py &
STREAMLIT_PID=$!

sleep 3
open http://localhost:8501

wait $STREAMLIT_PID
