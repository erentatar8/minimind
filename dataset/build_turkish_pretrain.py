import json
import re
import argparse
from datasets import load_dataset
from tqdm import tqdm

def clean_paragraph(p):
    # Fazla boşlukları ve kontrol karakterlerini temizle
    p = re.sub(r'[ \t]+', ' ', p).strip()
    return p

def main():
    parser = argparse.ArgumentParser(description="MiniMind Türkçe Pretraining Veri Seti Üretici (Wikipedia)")
    parser.add_argument("--max_samples", type=int, default=100000, help="Toplanacak maksimum paragraf/metin parçası sayısı")
    parser.add_argument("--min_char_len", type=int, default=120, help="Kabul edilecek minimum karakter uzunluğu")
    parser.add_argument("--max_char_len", type=int, default=1200, help="Bir parçanın maksimum karakter uzunluğu")
    parser.add_argument("--output_path", type=str, default="dataset/pretrain_turkce.jsonl", help="Çıktı JSONL dosyası")
    args = parser.parse_args()

    print("==================================================")
    print("📚 Türkçe Vikipedi (Wikipedia) Külliyatı İndiriliyor...")
    print(f"🎯 Hedef Örnek Sayısı: {args.max_samples:,}")
    print(f"💾 Çıktı Dosyası: {args.output_path}")
    print("==================================================")

    # Streaming modunda indirme (RAM şişmez, anında başlar)
    dataset = load_dataset('wikimedia/wikipedia', '20231101.tr', split='train', streaming=True)

    collected = 0
    skipped_articles = 0
    total_articles = 0

    with open(args.output_path, 'w', encoding='utf-8') as f_out:
        pbar = tqdm(total=args.max_samples, desc="Toplanan Metinler", unit="örnek")
        
        for article in dataset:
            total_articles += 1
            title = article.get('title', '')
            text = article.get('text', '')

            # Anlam ayrımı sayfalarını veya taslakları atla
            if '(anlam ayrımı)' in title.lower() or len(text) < 200:
                skipped_articles += 1
                continue

            # Makaleyi paragraflara böl
            raw_paras = text.split('\n\n')
            buffer = ""

            for raw_p in raw_paras:
                p = clean_paragraph(raw_p)
                if not p:
                    continue

                # Başlıkları veya liste elemanlarını birleştirerek bağlamı koru
                if len(buffer) + len(p) < args.max_char_len:
                    buffer += ("\n" if buffer else "") + p
                else:
                    if len(buffer) >= args.min_char_len:
                        f_out.write(json.dumps({"text": buffer}, ensure_ascii=False) + '\n')
                        collected += 1
                        pbar.update(1)
                        if collected >= args.max_samples:
                            break
                    buffer = p

                if collected >= args.max_samples:
                    break

            # Döngü bittiğinde tamponda kalan metni de yaz
            if collected < args.max_samples and len(buffer) >= args.min_char_len:
                f_out.write(json.dumps({"text": buffer}, ensure_ascii=False) + '\n')
                collected += 1
                pbar.update(1)

            if collected >= args.max_samples:
                break

        pbar.close()

    print("\n==================================================")
    print(f"🎉 Tamamlandı! Toplam {collected:,} kaliteli Türkçe paragraf kaydedildi.")
    print(f"📖 Taranan Makale Sayısı: {total_articles:,} (Atlanan: {skipped_articles:,})")
    print(f"📍 Dosya: {args.output_path}")
    print("==================================================")

if __name__ == "__main__":
    main()
