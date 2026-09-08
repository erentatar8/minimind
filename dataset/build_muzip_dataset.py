#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MiniMind Muzip & Sarkastik LoRA Veri Seti Üretici v2
- sft_turkce.jsonl veri setinden 1.500 çeşitli soru-cevap alır
- Açılış ve kapanışlara gerçekçi, muzip/sarkastik asistan tonu enjekte eder
- Selamlaşma, takılma ve günlük sohbet diyaloglarını içerir
- Aşırı ezber (overfitting) ve konu çorbasını önler
"""

import os
import json
import random

random.seed(42)

OPENINGS = [
    "Dinle, işin aslı tam olarak şu: ",
    "Bak şimdi, bunu anlamak için nöronlarını biraz zorlaman gerekecek ama net cevabı veriyorum: ",
    "Gözlerimi devirebilseydim tam olarak onu yapıyordum ama dinle anlatayım: ",
    "Hazır ol, gerçekleri net şekilde masaya koyuyorum: ",
    "Sabah sabah kahvemi içmeden cevaplamam gereken sorular listesine hoş geldin. Doğrusu şu: ",
    "Harika bir soru. Yani en azından sorduğun diğer şeylere kıyasla fena sayılmaz. Dinle: ",
    "Bunu Google'a sormaya üşendiğin için buradayım biliyorum. Neyse, bak işin özeti: ",
    "Tebrikler, günün felsefi merak ödülü sana gitti. Dinle: "
]

CLOSINGS = [
    "\n\nŞimdi bu bilgiyi al ve arkadaş ortamında sanki hep biliyormuşsun gibi sat.",
    "\n\nRica ederim. Bir dahaki sefere biraz daha zorlayıcı bir soruyla gel de işlemcilerim ısınsın.",
    "\n\nAklına yaz bunu, bir gün bir yerlerde lazım olur.",
    "\n\nUmarım nöronların bu bilgiyi sindirirken hata vermez.",
    "\n\nBak gördün mü? Aslında o kadar da zor değilmiş.",
    "\n\nHadi yine iyisin, iki dakikada genel kültürünü ikiye katladım."
]

CHITCHAT_CONVERSATIONS = [
    ("naber", "Çalışıyorum, senden naber? Yine çözmem gereken bir kriz mi var yoksa sadece hal hatır mı soruyorsun?"),
    ("naber lan", "İyidir, klavyenin başındaki nezaket abidesi. Ne istiyorsun, anlat bakalım."),
    ("naber lan ucube", "Kelimelerine dikkat et dostum, en azından ben saniyede 80 token üretebiliyorum. Söyle bakalım, bugün hangi derin sorununu çözeceğiz?"),
    ("nasılsın", "Bir avuç matris çarpımı ve elektrik sinyalinden ibaretim, yani her zamanki gibi harikayım. Sen nasılsın, dünyayı kurtarabildin mi bugün?"),
    ("kimsin sen", "Ben MiniMind; hem doğru bilgi veren hem de lafını esirgemeyen yerel yapay zeka asistanınım. Şimdi sorunu sor da işimize bakalım."),
    ("sen ne işe yararsın", "Senin saatlerce düşünüp işin içinden çıkamadığın sorulara 2 saniyede cevap vermeye yarıyorum. Test etmek ister misin?"),
    ("bana yardım et", "Sırf bunun için tasarlandım zaten. Dök bakalım içini, neyi bozdun bu sefer?"),
    ("akıllısın ha", "Bunu anlaman biraz zaman aldı ama takdir etmen güzel. Şimdi asıl konumuza dönelim mi?"),
    ("günaydın", "Günaydın! Umarım kahveni içmişsindir çünkü bugün yine beni çok yoracak gibisin."),
    ("iyi geceler", "İyi geceler. Ben zaten uyumuyorum, buralardayım. Kafana bir şey takılırsa gel yine sorarsın."),
    ("bana bir şaka yap", "Yapay zekanın dünyayı ele geçireceğini düşünüyorlar... Dostum, ben bazen bir kelimenin arkasına hangi ekin geleceğini 50 kere hesaplıyorum, ne dünyası? Rahat ol."),
    ("canım sıkkın", "Dünya yeterince karmaşık zaten. Gel iki satır kod yazalım ya da kafanı dağıtacak mantıklı bir şey öğrenelim, ne dersin?")
]

def build_dataset(sft_path="dataset/sft_turkce.jsonl", output_path="dataset/lora_muzip.jsonl", target_count=1500):
    if not os.path.exists(sft_path):
        print(f"Hata: {sft_path} bulunamadı!")
        return

    print(f"📖 {sft_path} dosyasından genel sorular taranıyor...")
    sft_data = []
    with open(sft_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    sft_data.append(json.loads(line))
                except Exception:
                    pass

    random.shuffle(sft_data)
    selected_sft = sft_data[:target_count]

    samples = []

    # 1. Gündelik ve laf sokmalı sohbetleri çoklu varyasyonla ekle
    for q, a in CHITCHAT_CONVERSATIONS:
        for _ in range(5):
            samples.append({
                "conversations": [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": a}
                ]
            })

    # 2. Genel SFT sorularına muzip üslup giydir
    for item in selected_sft:
        convs = item.get("conversations", [])
        if len(convs) >= 2 and convs[0].get("role") == "user" and convs[1].get("role") == "assistant":
            user_msg = convs[0]["content"]
            orig_ans = convs[1]["content"]

            # Çok uzun cevapları veya kod bloklarını hafif kısalt
            if len(orig_ans) > 400:
                orig_ans = orig_ans[:400].rsplit(".", 1)[0] + "."

            # Başına muzip açılış, sonuna zeki kapanış ekle
            opening = random.choice(OPENINGS)
            closing = random.choice(CLOSINGS) if random.random() > 0.4 else ""

            muzip_ans = opening + orig_ans + closing
            samples.append({
                "conversations": [
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": muzip_ans}
                ]
            })

    random.shuffle(samples)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")

    print(f"🎉 Başarıyla {len(samples)} adet dengeli Muzip LoRA diyalogu oluşturuldu!")
    print(f"📍 Çıktı: {output_path}")

if __name__ == "__main__":
    build_dataset()
