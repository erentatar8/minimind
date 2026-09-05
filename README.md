<div align="center">

![logo](./images/logo.png)

</div>

<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)](https://github.com/jingyaogong/minimind/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind)](https://github.com/jingyaogong/minimind/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/12586)

</div>

<div align="center">
  <h3>"Büyük Yol Sadeliğe Dayanır"</h3>
</div>

<div align="center">

Türkçe | [English](./README_en.md) | [中文](./README_zh.md)

</div>

> [!NOTE]
> **Bu Çatal (Fork) Hakkında / Türkçe Dokümantasyon & Apple Silicon (M4) Çalışması**  
> Bu depo; modern bir Büyük Dil Modelinin (LLM) sıfırdan nasıl inşa edildiğini, ön eğitim (pretraining), denetimli ince ayar (SFT) ve pekiştirmeli öğrenme (RL) süreçlerinin iç mekanizmalarını bizzat deneyimlemek amacıyla oluşturulmuştur.  
> Projenin bir diğer temel odağı, Apple Silicon mimarisinin (özellikle M4 çipi ve Birleşik Bellek / Unified Memory) bu ölçekteki modellerin yerel eğitimi ve çıkarımındaki verimliliğini test etmektir.  
> Türkçe konuşan araştırmacı ve geliştiricilere derli toplu bir açık kaynak kaynağı sunmak adına tüm dokümantasyon Türkçeleştirilmiş; orijinal İngilizce (`README_en.md`) ve Çince (`README_zh.md`) sürümler de depoda korunmuştur.

* Bu açık kaynaklı proje, yaklaşık 64M parametreli son derece küçük bir dil modeli olan MiniMind'ı, yalnızca yaklaşık 3 RMB maliyet ve 2 saatlik eğitim süresiyle tamamen sıfırdan eğitmeyi amaçlamaktadır.
* MiniMind serisi bilinçli olarak hafif tasarlanmıştır. Ana daldaki en küçük model GPT-3'ün yaklaşık $\frac{1}{2700}$'i boyutundadır; bu sayede tam eğitim ve yeniden üretim sıradan kişisel GPU'larda bile kolayca gerçekleştirilebilir.
* Proje; MoE, veri temizleme, ön eğitim (pretraining), Denetimli İnce Ayar (SFT), LoRA, RLHF (DPO), RLAIF (PPO / GRPO / CISPO), Araç Kullanımı (Tool Use), Agentic RL, Uyarlanabilir Düşünme (Adaptive Thinking) ve Model Damıtma (Distillation) dahil olmak üzere minimalist bir model mimarisi ve uçtan uca bir LLM eğitim süreci sunar.
* MiniMind ayrıca bir görsel modele [MiniMind-V](https://github.com/jingyaogong/minimind-v), çok modlu bir Omni modele [MiniMind-O](https://github.com/jingyaogong/minimind-o), bir difüzyon dil modeline (MiniMind-dLM) ve bir doğrusal dikkat modeline (MiniMind-Linear) genişletilmiştir. Detaylar için [Tartışmalar (Discussions)](https://github.com/jingyaogong/minimind/discussions) bölümüne göz atabilirsiniz.
* Tüm temel algoritmalar, üçüncü taraf kütüphanelerin yüksek seviyeli soyutlamalarına bağımlı kalmadan, doğrudan saf (native) PyTorch ile sıfırdan uygulanmıştır.
* MiniMind, hem LLM eğitim sürecinin uçtan uca açık kaynaklı bir yeniden üretimi hem de büyük dil modellerinin derinliklerini öğrenmek için pratik bir eğitim rehberidir.
* Bu projenin daha fazla kişi için yeniden üretilebilir, anlaşılır ve genişletilebilir bir başlangıç noktası sunmasını, üretmenin keyfini paylaşmasını ve yapay zeka topluluğunu ileriye taşımaya katkı sağlamasını umuyoruz.

> Not: Bu proje Apache 2.0 lisansı altında yayımlanmıştır ve tamamen ücretsizdir. "2 saat", tek bir NVIDIA 3090 üzerinde SFT aşamasının `1 epoch` çalıştırılması için ölçülen süreyi; "3 RMB" ise buna karşılık gelen sunucu/GPU kiralama maliyetini temsil eder.

---

<div align="center">

![minimind-3](./images/minimind-3.gif)

[🔗 Çevrim İçi Demo](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗 Video Tanıtımı](https://www.bilibili.com/video/BV12dHPeqE72)


<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://huggingface.co/collections/jingyaogong/minimind" style="text-decoration: none;">
          <img src="./images/with_huggingface.png" alt="Hugging Face Logosu" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.modelscope.cn/profile/gongjy" style="text-decoration: none;">
          <img src="./images/with_modelscope.png" alt="ModelScope Logosu" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
    </tr>
  </table>
</div>


</div>

---

# 📌 Proje Tanıtımı

Büyük Dil Modellerinin (LLM) ortaya çıkışı, yapay zekaya yönelik dünya çapında benzeri görülmemiş bir ilgi uyandırdı. ChatGPT, DeepSeek, Qwen ve daha birçok model, etkileyici performanslarıyla insanları büyüleyerek bu teknoloji dalgasının etkisini son derece somut hale getirdi. Ancak on veya yüz milyarlarca parametreye sahip modellerin yalnızca kişisel cihazlarda eğitilmesi imkânsız olmakla kalmıyor, çoğu zaman yerel olarak dağıtılması bile erişilemez kalıyor. Büyük modellerin o "kara kutusunu" açıp içeride gerçekten nasıl çalıştıklarını anlamak son derece heyecan verici olmalıydı. Ne yazık ki çoğu araştırma ve deneme, LoRA gibi teknikleri kullanarak mevcut büyük modelleri birkaç yeni talimat veya belirli görevler üzerinde ince ayar (fine-tune) yapmaktan öteye geçemiyor. Bu durum, Newton'a 21. yüzyılın akıllı telefonunu nasıl kullanacağını öğretmeye benziyor — ilgi çekici, ancak fiziğin özünü anlama hedefine tam olarak uymuyor.

Aynı zamanda, `transformers` / `trl` / `peft` gibi üçüncü taraf LLM kütüphaneleri ve araç setleri genellikle yalnızca son derece soyut arayüzler sunar. Yalnızca bir düzine satır kodla "model yükle + veri kümesi yükle + çıkarım yap + pekiştirmeli öğrenme uygula" eğitim zincirinin tamamı tamamlanabilir. Bu tür yüksek seviyeli paketleme son derece pratiktir, ancak geliştiricileri temel donanım ve matematiksel uygulamadan bir dereceye kadar kopararak LLM'lerin çekirdek kodunu derinlemesine anlama fırsatını azaltır. İnanıyorum ki "bir uçağı Lego parçalarından kendi elinizle inşa etmek, birinci sınıfta uçmaktan çok daha heyecan vericidir." Daha pratik bir sorun ise internetin, yüzeysel ve yarım yamalak açıklamalarla sarılmış sözde yapay zeka eğitimleri ve pazarlama içerikleriyle dolu olmasıdır. Bu nedenle, bu projenin temel amacı LLM öğrenme eşiğini mümkün olduğunca düşürmek, herkesin her satır kodu anlayarak işe başlamasını sağlamak ve kendi elleriyle sıfırdan minik bir dil modeli eğitebilmesine imkân tanımaktır. Evet, sadece **çıkarım (inference)** seviyesinde kalmak değil, **tamamen sıfırdan eğitmek**. 3 RMB'den daha az bir sunucu maliyetiyle, bir dil modelini 0'dan 1'e inşa etmenin tüm sürecini bizzat deneyimleyebilirsiniz.

😊 Gelin, üretmenin sevincini birlikte paylaşalım!

---

#### 🎉 Bu Proje Şunları İçerir

- `Qwen3 / Qwen3-MoE` ekosistemiyle uyumlu tam MiniMind-LLM mimari uygulamasını (Dense + MoE) sunar.
- `<tool_call>`, `<tool_response>`, `<think>` gibi özel şablon belirteçlerini (tokens) destekleyen belirteçleyiciyi (tokenizer) ve tokenizer eğitim kodunu içerir.
- Ön eğitim (pretraining), SFT, LoRA, RLHF-DPO, RLAIF (PPO / GRPO / CISPO), Araç Kullanımı (Tool Use), Agentic RL, Uyarlanabilir Düşünme ve Model Damıtma gibi uçtan uca eğitim hatlarını kapsar.
- Toplanan, damıtılan, temizlenen ve tekilleştirilen yüksek kaliteli veri kümelerini kapsayacak şekilde tüm aşamalar için açık kaynaklı veriler sağlar.
- Temel eğitim algoritmaları ve çekirdek modüller, üçüncü taraf çatıların paketlemelerine dayanmadan tamamen sıfırdan uygulanmıştır.
- `transformers`, `trl`, `peft` gibi ana akım çatıların yanı sıra `llama.cpp`, `vllm`, `ollama` gibi yaygın çıkarım motorları ve `Llama-Factory` gibi eğitim araçlarıyla uyumludur.
- Tek düğüm tek GPU ve tek düğüm çoklu GPU eğitimini (DDP, DeepSpeed), wandb / swanlab görselleştirmesini ve dinamik eğitim duraklatma/devam ettirme (checkpoint resume) özelliklerini destekler.
- C-Eval, C-MMLU, OpenBookQA gibi üçüncü taraf kıyaslama (benchmark) paketlerinde değerlendirmeyi ve YaRN aracılığıyla RoPE uzun bağlam ekstrapolasyonunu destekler.
- FastGPT ve Open-WebUI gibi üçüncü taraf sohbet arayüzleriyle entegrasyon için hafif, OpenAI uyumlu bir API sunucusu sağlar (`reasoning_content`, `tool_calls` ve `open_thinking` desteğiyle).
- Düşünce sürecini görüntüleme, araç seçimi ve çok turlu Tool Call desteğine sahip Streamlit tabanlı minimalist bir sohbet WebUI'ı sunar.
- Deneysel uzantılar içerir: Difüzyon dil modeli ([dLM](https://github.com/jingyaogong/minimind/discussions/618)) ve doğrusal dikkat modeli ([Linear Attention](https://github.com/jingyaogong/minimind/discussions/704)); her ikisi de ana özbağlanımlı (autoregressive) modelden itibaren eğitilebilir.

#### 🎉 Yayımlanan Model Listesi

| Model | Parametre Sayısı | Yayımlanma |
|------|--------|---------|
| minimind-3 | 64M | 2026.04.01 |
| minimind-3-moe | 198M-A64M | 2026.04.01 |
| minimind2-small | 26M | 2025.04.26 |
| minimind2-moe | 145M | 2025.04.26 |
| minimind2 | 104M | 2025.04.26 |
| minimind-v1-small | 26M | 2024.08.28 |
| minimind-v1-moe | 4×26M | 2024.09.17 |
| minimind-v1 | 108M | 2024.09.01 |

---

#### 📝 Değişiklik Günlüğü

<details> 
<summary> <b>🔥 2026-04-01</b> </summary>

- `minimind-3` / `minimind-3-moe` yayımlandı: Mimari, Tokenizer, eğitim hattı, çıkarım arayüzü ve varsayılan konfigürasyonda kapsamlı güncellemeler yapıldı
- Ana dal mimarisi `Qwen3 / Qwen3-MoE` ekosistemiyle hizalandı: Dense yaklaşık `64M`, MoE yaklaşık `198M-A64M` olarak ayarlandı ve paylaşılan uzman (shared expert) tasarımı kaldırıldı
- Varsayılan eğitim verileri `pretrain_t2t(_mini).jsonl`, `sft_t2t(_mini).jsonl`, `rlaif.jsonl`, `agent_rl.jsonl` ve `agent_rl_math.jsonl` olarak güncellendi
- Bağımsız `train_reason.py` kaldırıldı; düşünme yeteneği artık `chat_template + <think>` ve `open_thinking` uyarlanabilir anahtar kontrolü ile birleşik hale getirildi
- `toolcall` yeteneği `sft_t2t / sft_t2t_mini` ana dal verilerine entegre edildi, varsayılan `full_sft` modeli temel Tool Call yeteneğine sahip oldu; ayrıca `scripts/chat_api.py` gibi çıkarım örnekleri eklendi
- Çok turlu Araç Kullanımı (Tool-Use) senaryolarında `GRPO / CISPO` algoritmalarını destekleyen saf `Agentic RL` eğitim betiği `train_agent.py` eklendi
- RLAIF / Agentic RL eğitim hattında `rollout engine` ayrıştırması tamamlandı, üretim arka uçlarının daha esnek biçimde değiştirilmesi desteklendi
- `serve_openai_api.py` ve `web_demo.py` dosyalarına `reasoning_content` / `tool_calls` / `open_thinking` desteği eklendi
- Tokenizer `BPE + ByteLevel` temelinde güncellendi; yeni araç çağırma ve düşünme belirteçleri eklendi, gelecekteki genişletmeler için tampon belirteçler ayrıldı
- LoRA ağırlık birleştirme ve dışa aktarma hattı eklendi; temel model ve LoRA ağırlıkları `scripts/convert_model.py` üzerinden yeni bir bütün model ağırlığında birleştirilebilir
- Mimari şemaları güncellendi, README kapsamlı biçimde yenilendi

</details>

<details> 
<summary> <b>2025-10-24</b> </summary>

- 🔥 RLAIF eğitim algoritmaları eklendi: PPO, GRPO, SPO (doğrudan sıfırdan saf PyTorch ile kodlandı)
- Kontrol noktası devam ettirme (checkpoint resume) işlevi eklendi: Eğitimin otomatik kurtarılması, farklı GPU sayıları arasında kurtarma ve wandb kayıt sürekliliği desteklendi
- RLAIF veri kümesi eklendi: `rlaif-mini.jsonl` (SFT verilerinden rastgele örneklenen 10.000 girdi); DPO veri kümesi sadeleştirildi, Çince veriler eklendi
- YaRN algoritması eklendi: RoPE uzun bağlam ekstrapolasyonunu destekleyerek uzun dizi işleme yeteneğini geliştirdi
- Uyarlanabilir Düşünme: Reason modeli isteğe bağlı olarak düşünce zincirini (CoT) etkinleştirebilir
- `chat_template`, Araç Çağırma ve Akıl Yürütme etiketlerini (`<tool_call>`, `<think>` vb.) tam olarak destekler
- Kapsamlı RLAIF bölümü, eğitim eğrisi karşılaştırması ve katlanabilir algoritma prensipleri açıklamaları eklendi
- WandB yerine [SwanLab](https://swanlab.cn/) entegre edildi (API tam uyumludur)
- Tüm kodlar standartlaştırıldı ve bilinen hatalar giderildi

</details>

<details> 
<summary> <b>2025-04-26</b> </summary>

- Büyük güncelleme
- Geriye dönük uyumluluk ihtiyaçları için [🔗Eski Depo İçeriğini🔗](https://github.com/jingyaogong/minimind/tree/7da201a944a90ed49daef8a0265c959288dff83a) ziyaret edebilirsiniz.
- MiniMind model parametreleri, Transformers kütüphanesi modelleriyle hizalanacak şekilde tamamen yeniden adlandırıldı (tek tip adlandırma).
- `generate` metodu `GenerationMixin` sınıfından miras alacak şekilde yeniden yapılandırıldı.
- 🔥 llama.cpp, vllm, ollama gibi popüler üçüncü taraf ekosistemleri desteklendi.
- Kod ve dizin yapısı standartlaştırıldı.
- Kelime dağarcığı şablonu `<s></s>` -> `<|im_start|><|im_end|>` olarak değiştirildi.

```text
llama.cpp ve vllm gibi üçüncü taraf çıkarım çatılarıyla uyumlu olabilmek adına bu güncelleme bazı önemli değişiklikler getirdi.
Bu sürüm artık 25-04-26 öncesi eski modellerin çıkarım için "doğrudan" yüklenmesini desteklememektedir.
Llama'nın konumsal kodlama yöntemi ile minimind arasındaki farklar nedeniyle, Llama modeline eşleme yapıldıktan sonra QK değerleri farklılık gösterir.
minimind2 serisi eski modellerin tümü ağırlık eşleme + (ince ayar) QKVO doğrusal katman kalibrasyonu yoluyla kurtarılmıştır.
Bu güncellemeden sonra tüm `minimind-v1` serisinin bakımı durdurulmuş ve depodan kaldırılmıştır.
```

</details>

<details>
<summary> <b>Daha Fazlası...</b> </summary>

**2025-02-09**
- İlk yayımdan bu yana yapılan en büyük güncelleme: minimind2 Serisi Yayımlandı.
- Kod, daha öz ve net bir birleşik yapı kullanılarak neredeyse tamamen yeniden yazıldı.
  Eski kodlarla uyumluluk için [🔗Eski Depo İçeriğini🔗](https://github.com/jingyaogong/minimind/tree/6e9cd28ef9b34a0a10afbdf6f59e65cb6e628efb) ziyaret edebilirsiniz.
- Veri ön işleme adımları kaldırıldı. Veri kümesi formatı standartlaştırıldı ve veri kümesi indirme karmaşasını önlemek için `jsonl` formatına geçildi.
- minimind2 serisi, MiniMind-V1'e kıyasla performansı önemli ölçüde artırdı.
- Küçük iyileştirmeler: {kv-cache uygulaması daha standart hale getirildi, MoE yük dengeleme kaybı hesaba katıldı vb.}
- Modelleri özel veri kümelerine uyarlama eğitim çözümleri sağlandı (tıp modeli, benlik bilinci örnekleri).
- Ön eğitim veri kümesi sadeleştirildi ve veri kalitesi önemli ölçüde artırıldı; tek bir 3090 üzerinde 2 saatte yeniden üretilebilecek şekilde eğitim süresi büyük ölçüde kısaltıldı!
- Güncellemeler: LoRA ince ayarı peft paketleyicisinden ayrıştırıldı, LoRA süreci sıfırdan uygulandı; DPO algoritması PyTorch kullanılarak doğrudan sıfırdan yazıldı; model beyaz kutu damıtma (white-box distillation) yerel olarak kodlandı.
- minimind2-DeepSeek-R1 serisi damıtılmış modeller doğdu!
- minimind2 belirli bir İngilizce dil kabiliyetine kavuştu!
- minimind2'nin üçüncü taraf modellerle karşılaştırmalı benchmark test sonuçları güncellendi.

**2024-10-05**
- MiniMind için çok modlu yetenek genişletildi --- Görme (Vision)
- Detaylar için kardeş proje olan [minimind-v](https://github.com/jingyaogong/minimind-v)'yi ziyaret edin!

**2024-09-27**
- 09-27 ön eğitim veri kümesi ön işleme yöntemi güncellendi; metin bütünlüğünü korumak adına eğitim için .bin formatına ön işleme terk edildi (eğitim hızından ufak bir ödün verildi).
- Şu anda ön eğitimde işlenen dosya: `pretrain_data.csv`.
- Bazı gereksiz kodlar temizlendi.

**2024-09-17**
- `minimind-v1-moe` modeli güncellendi.
- Karışıklıkları önlemek için belirteçleme sürecinde artık mistral_tokenizer kullanılmıyor, tamamen özel `minimind_tokenizer` kullanılıyor.

**2024-09-01**
- `minimind-v1` (108M) modeli güncellendi; minimind_tokenizer kullanıldı, ön eğitim 3 epoch + SFT 10 epoch yapılarak daha derin bir eğitim ve daha güçlü performans elde edildi.
- Proje ModelScope Creative Space üzerinde dağıtıldı, şu adresten çevrim içi denenebilir:
- [🔗ModelScope Çevrim İçi Demosu🔗](https://www.modelscope.cn/studios/gongjy/minimind)

**2024-08-27**
- Proje ilk kez açık kaynak olarak yayımlandı.

</details>
---

# 📌 Hızlı Başlangıç

<details>
<summary>Donanım ve yazılım yapılandırmam (referans için)</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090 (24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10.16
* [requirements.txt](./requirements.txt)

</details>

## Adım 0

```bash
# Depoyu klonlayın ve bağımlılıkları yükleyin
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

## Ⅰ 🚀 Model Çıkarımı

### 1' Modeli İndirin

Proje kök dizininde:
```bash
# Yöntem 1
modelscope download --model gongjy/minimind-3 --local_dir ./minimind-3
# Yöntem 2
git clone https://huggingface.co/jingyaogong/minimind-3
```

### 2' CLI (Komut Satırı) Çıkarımı

```bash
# Yöntem 1: Transformers formatındaki modeli kullanma
python eval_llm.py --load_from ./minimind-3
# Yöntem 2: PyTorch modeline dayalı (ilgili ağırlıkların ./out dizininde olduğundan emin olun)
python eval_llm.py --load_from ./model --weight full_sft
```

### 3' (İsteğe Bağlı) WebUI

```bash
# `python>=3.10` gerekebilir, `pip install streamlit` ile kurun
# ⚠️ Öncelikle transformers formatındaki model klasörünü ./scripts/ dizinine kopyalamanız gerekir (örn: cp -r minimind-3 ./scripts/minimind-3). web_demo betiği ağırlık dosyalarını içeren alt dizinleri otomatik tarar; bulunamazsa hata verir.
cd scripts && streamlit run web_demo.py
```

### 4' (İsteğe Bağlı) Üçüncü Taraf Çıkarım Çatıları

```bash
# ollama
ollama run jingyaogong/minimind-3
# vllm
vllm serve /path/to/model --served-model-name "minimind"
```

## Ⅱ 🛠️ Model Eğitimi

<details>
<summary>Not: Torch'un kullanılabilir arka ucunu önceden doğrulayın</summary>

```python
import torch
print(torch.cuda.is_available())
```

Eğitim için CUDA kullanmayı planlıyorsanız, öncelikle geçerli ortamın GPU'yu doğru tanıyıp tanımadığını kontrol etmeniz önerilir.  
Eğer `cuda` kullanılamıyorsa, cihazınıza bağlı olarak `CPU` veya `MPS` seçebilirsiniz; ancak eğitim hızı ve uyumluluk belirgin şekilde farklılık gösterecektir.  
PyTorch sürümlerini kurmanız veya değiştirmeniz gerekirse [torch_stable](https://download.pytorch.org/whl/torch_stable.html) sayfasına ve [bu bağlantıya](https://blog.csdn.net/weixin_45456738/article/details/141029610?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%AE%89%E8%A3%85torch&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-141029610.nonecase&spm=1018.2226.3001.4187) göz atabilirsiniz.

</details>

### 1' Verileri İndirin

Aşağıda paylaşılan [veri kümesi indirme bağlantısından](https://www.modelscope.cn/datasets/gongjy/minimind_dataset/files) gerekli veri dosyalarını indirin ve `./dataset` dizinine yerleştirin.

> Şu anda varsayılan olarak `MiniMind Zero` diyalog modelini hızlıca yeniden üretmek için yalnızca `pretrain_t2t_mini.jsonl` ve `sft_t2t_mini.jsonl` dosyalarını indirmeniz yeterlidir.  
Diğer kullanım senaryoları için aşağıda çeşitli veri kombinasyonları sunulmuştur; görev hedeflerinize ve GPU kaynaklarınıza göre seçim yapabilirsiniz.

### 2' Eğitime Başlayın

<details>
<summary>💡 Kontrol Noktası Duraklatma ve Devam Ettirme (Checkpoint Resume)</summary>

Tüm eğitim betikleri kontrol noktası kaydetmeyi destekler. `--from_resume 1` parametresini eklediğinizde betik eğitim ilerlemesini otomatik olarak algılar ve kaldığı yerden devam eder:

```bash
python train_pretrain.py --from_resume 1
python train_full_sft.py --from_resume 1
# ...
```

**Kontrol Noktasından Devam Ettirme Talimatları:**
- Eğitim süreci tam kontrol noktalarını (model, optimize edici, eğitim ilerlemesi vb.) otomatik olarak `./checkpoints/` dizinine kaydeder
- Kontrol noktası dosyası adlandırması: `<weight_name>_<dimension>_resume.pth` (örn. `full_sft_512_resume.pth`)
- Farklı GPU sayıları arasında kurtarmayı destekler (adım sayısını otomatik ayarlar)
- wandb eğitim kaydı sürekliliğini destekler (aynı çalıştırmayı otomatik sürdürür)

> Uzun süreli eğitimler veya kararsız ortamlar için uygundur; kesinti nedeniyle ilerlemenin kaybolmasından endişelenmenize gerek kalmaz.

</details>

#### 2.1 Ön Eğitim (Zorunlu)

```bash
cd trainer && python train_pretrain.py
```

> Eğitimden sonra çıktı ağırlıkları olarak `out/pretrain_*.pth` üretilecektir (`*` model boyutunu temsil eder, varsayılan `768`)

#### 2.2 Talimat İnce Ayarı (Zorunlu)

```bash
cd trainer && python train_full_sft.py
```

> Eğitimden sonra çıktı ağırlıkları olarak `out/full_sft_*.pth` üretilecektir (`full`, tam parametreli ince ayarı belirtir)

#### 2.3 Eğitilen Modeli Test Etme (İsteğe Bağlı)

Test edilecek `*.pth` model dosyalarının `./out/` dizininde olduğundan emin olun; ayrıca önceden eğitilmiş `*.pth` ağırlıklarımı indirmek için doğrudan [buraya](https://www.modelscope.cn/models/gongjy/minimind-3-pytorch/files) gidebilirsiniz.

```bash
python eval_llm.py --weight full_sft
```

> `--weight`, ağırlık adı önekini belirtmek için kullanılır (`pretrain`, `full_sft` vb.); daha fazla parametre için doğrudan `eval_llm.py` dosyasına bakın.

<details>
<summary>Not: Diğer Bilgiler</summary>

1. Tüm eğitim betikleri yerel PyTorch temelinde uygulanmıştır ve çoklu GPU ivmelendirmesini destekler.

2. Cihazınızda `N (N > 1)` GPU varsa, tek makineli `N`-GPU eğitimini aşağıdaki gibi başlatabilirsiniz (DDP, çok makineli çoklu GPU'ya genişletmeyi de destekler):

```bash
torchrun --nproc_per_node N train_xxx.py
```

3. İhtiyacınıza göre eğitim sürecini kaydetmek için wandb'yi etkinleştirebilirsiniz:

```bash
... train_xxx.py --use_wandb
```
MiniMind şu anda eğitim görselleştirme aracı olarak arayüzü WandB ile neredeyse tamamen uyumlu olan [SwanLab](https://swanlab.cn/)'ı varsayılan olarak desteklemektedir; genellikle yalnızca `import wandb` yerine `import swanlab as wandb` yazmanız yeterlidir, diğer kullanımlar büyük ölçüde aynı kalır.

</details>
---

# 📌 Veri Tanıtımı

## Ⅰ Belirteçleyici (Tokenizer)

Bir belirteçleyici (tokenizer), LLM'ler tarafından kullanılan bir "sözlük" olarak düşünülebilir; doğal dili belirteç kimliklerine (token id) eşlemekten ve belirteç kimliklerini tekrar metne dönüştürmekten sorumludur. Proje ayrıca kelime dağarcığı eğitimi için bir örnek olarak `train_tokenizer.py` dosyasını sunar. Belirteçleyicinin yeniden eğitilmesi önerilmez; çünkü kelime haznesi ve bölme kuralları değiştiğinde model ağırlıkları, veri formatları, çıkarım arayüzleri ve topluluk ekosistem uyumluluğu doğrudan etkilenir ve ortaya çıkan modelin paylaşılması zorlaşır. Aynı zamanda belirteçleyici, belirteç başına hesaplanan PPL gibi metrikleri de etkiler; bu nedenle farklı belirteçleyicileri karşılaştırırken BPB (Bayt Başına Bit / Bits Per Byte) genellikle daha adil bir metriktir. Ayrıntılar için [bu makaleye](https://skeptric.com/perplexity/) göz atabilirsiniz.

MiniMind gibi küçük modeller için kelime dağarcığı boyutu, gömme (embedding) ve çıktı katmanlarının parametre oranını da doğrudan etkiler; bu nedenle kelime haznesini derli toplu tutmak genellikle daha dengeli bir tercihtir.

<details>
<summary>Belirteçleyici (Tokenizer) Tanıtımı</summary>

Güçlü açık kaynaklı modellerin belirteçleyici kelime dağarcığı boyutları şu şekildedir:

<table>
  <tr><th>Belirteçleyici Modeli</th><th>Kelime Dağarcığı Boyutu</th><th>Kaynak</th></tr>
  <tr><td>Yi</td><td>64.000</td><td>01.AI (Çin)</td></tr>
  <tr><td>Qwen2</td><td>151.643</td><td>Alibaba Cloud (Çin)</td></tr>
  <tr><td>ChatGLM</td><td>151.329</td><td>Zhipu AI (Çin)</td></tr>
  <tr><td>Mistral</td><td>32.000</td><td>Mistral AI (Fransa)</td></tr>
  <tr><td>Llama 3</td><td>128.000</td><td>Meta (ABD)</td></tr>
  <tr><td>MiniMind</td><td>6.400</td><td>Özel (Custom)</td></tr>
</table>

> Ana dal, geçmiş sürüm karmaşasını önlemek ve genel boyutu kontrol altında tutmak için tutarlı olarak `minimind_tokenizer` kullanır; `mistral_tokenizer` sürümünün bakımı artık yapılmamaktadır.

`minimind_tokenizer` yalnızca `6400` kelimelik bir hazneye sahip olmasına ve kodlama/kod çözme verimliliği `qwen2` veya `glm` gibi Çince dostu belirteçleyicilerden daha zayıf olmasına rağmen, gömme ve çıktı katmanlarının parametre payını önemli ölçüde azaltır. Bu da MiniMind gibi küçük modellerin boyut kısıtlamalarına çok daha iyi uyum sağlar.  
Pratikte bu belirteçleyici, nadir kelimelerde belirgin bir kod çözme hatasına yol açmamış ve genel kullanım için yeterince kararlı kalmıştır. Bu nedenle ana dal, ek çatallanmalar oluşturmak yerine tutarlı olarak bu kelime haznesini kullanır.

</details>

## Ⅱ Ön Eğitim Verisi (Pretrain Data)

Mevcut `MiniMind-3` ana dalı için ön eğitim verileri `pretrain_t2t.jsonl` / `pretrain_t2t_mini.jsonl` dosyalarıdır.  
Bu iki veri kümesi, sınırlı hesaplama gücü altında denge kurmayı hedefleyerek birleşik bir `metin -> sonraki belirteç tahmini (next token prediction)` eğitim formatında düzenlenmiştir:

- Metin kalitesi;
- Uzunluk dağılımı;
- Çince-İngilizce karma yetenek;
- Sonraki SFT / Araç Çağırma (Tool Calling) / RLAIF aşamalarıyla şablon uyumu.

Veri kaynakları genel metin derlemlerini, filtrelenmiş diyalog derlemlerini, damıtma verilerini ve **izin veren açık kaynak lisansları** altındaki çeşitli veri kümelerini içerir; ana dal verileri yalnızca temizleme, tekilleştirme, uzunluk kontrolü ve format standartlaştırma işlemlerinden sonra eğitime dâhil edilir. Veri kaynakları şunları içerir: [Craftsman LLM Dataset](https://www.modelscope.cn/datasets/deepctrl/deepctrl-sft-data), [Magpie-Align](https://www.modelscope.cn/organization/Magpie-Align) ve diğer kamuya açık kaynaklar.

Bunlar arasında:

- `pretrain_t2t_mini.jsonl` hızlı yeniden üretim için tasarlanmıştır;
- `pretrain_t2t.jsonl` ise `MiniMind-3` ana dal modelinin tam eğitimi için tasarlanmıştır.

Dosya formatı aşağıdaki gibidir:

```jsonl
{"text": "如何才能摆脱拖延症？治愈拖延症并不容易，但以下建议可能有所帮助。"}
{"text": "清晨的阳光透过窗帘洒进房间，桌上的书页被风轻轻翻动。"}
{"text": "Transformer 通过自注意力机制建模上下文关系，是现代大语言模型的重要基础结构。"}
```

## Ⅲ SFT Verisi (SFT Data)

Mevcut `MiniMind-3` ana dalı için SFT verileri `sft_t2t.jsonl` / `sft_t2t_mini.jsonl` dosyalarıdır. Önceki `sft_512 / sft_1024 / sft_2048` düzenlemelerine kıyasla güncel sürüm şunlara daha fazla odaklanır:

- Birleşik şablonlar;
- Diyalog + düşünme etiketleri + Araç Çağırma karma eğitimine daha uygun yapı;
- Veri ön işleme dallanmalarını en aza indirerek yeniden üretim maliyetlerini düşürme.

Veri kaynakları; yüksek kaliteli talimat takip verilerini, kamuya açık diyalog verilerini, model damıtmalı sentetik verileri ve izin veren lisanslı açık kaynak veri kümelerini kapsar; `t2t` ana dalına girmeden önce bu depoda kullanılan çok turlu diyalog formatında birleştirilirler. Mevcut ana dal ayrıca `qwen3-4b` modelinden sentezlenen yaklaşık `100K` `tool call` girdisi ve `qwen3` serisinden elde edilen `reasoning` verileri gibi çok sayıda sentetik veri içerir. Başlıca topluluk kaynakları: [Craftsman LLM Dataset](https://www.modelscope.cn/datasets/deepctrl/deepctrl-sft-data), [Magpie-Align](https://www.modelscope.cn/organization/Magpie-Align), [R1-Distill-SFT](https://www.modelscope.cn/datasets/AI-ModelScope/R1-Distill-SFT), [COIG](https://huggingface.co/datasets/BAAI/COIG), [Step-3.5-Flash-SFT](https://huggingface.co/datasets/stepfun-ai/Step-3.5-Flash-SFT) vb. Yayımlanan sürümler, veri kaynaklarının ve işleme süreçlerinin ilgili açık kaynak lisanslarının gerekliliklerine (Apache-2.0, CC-BY-NC-2.0 vb.) uygun olmasını sağlar.

Bunlar arasında:

- `sft_t2t_mini.jsonl`: Hızlıca bir diyalog modeli eğitmek için uygundur;
- `sft_t2t.jsonl`: Ana dal sürümünü eksiksiz biçimde yeniden üretmek için uygundur;
- `toolcall` yeteneği halihazırda ana dal SFT verilerine entegre edilmiştir.

Tüm SFT dosyaları, diyalog ve Araç Kullanımı (Tool Use) verilerini içerecek şekilde aynı formatı takip eder:

```jsonl
{
    "conversations": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！"},
        {"role": "user", "content": "再见"},
        {"role": "assistant", "content": "再见！"}
    ]
}
{
    "conversations": [
        {"role": "system", "content": "# Tools ...", "tools": "[...]"},
        {"role": "user", "content": "把'你好世界'翻译成english"},
        {"role": "assistant", "content": "", "tool_calls": "[{"name":"translate_text","arguments":{"text":"你好世界","target_language":"english"}}]"},
        {"role": "tool", "content": "{"translated_text":"Hello World"}"},
        {"role": "assistant", "content": "Hello World"}
    ]
}
```

## Ⅳ RL Verisi (Pekiştirmeli Öğrenme Verisi)

Mevcut `MiniMind` ana dalı için RL verisi, [DPO-En-Zh-20k](https://huggingface.co/datasets/llamafactory/DPO-En-Zh-20k) veri kümesinden örneklenen `dpo.jsonl` dosyasıdır.

Ana dalda bu örnekler, ödül modeli eğitimi veya tercih optimizasyonu amacıyla bu deponun tercih öğrenme formatında yeniden düzenlenmiştir. Burada `chosen` tercih edilen yanıtı, `rejected` ise daha zayıf yanıtı temsil eder.

`dpo.jsonl` veri formatı:

```json
{
  "chosen": [
    {"content": "Q", "role": "user"}, 
    {"content": "good answer", "role": "assistant"}
  ], 
  "rejected": [
    {"content": "Q", "role": "user"}, 
    {"content": "bad answer", "role": "assistant"}
  ]
}
```

Bunun dışında diğer RL verileri SFT verileriyle aynı formatı korur; genellikle toplam uzunluk ve diyalog turuna göre SFT verilerinden filtrelenir ve rollout aşamasında tamamlama yapılabilmesi için son `assistant` konumu boş bırakılır.

## Ⅴ MiniMind Eğitim Veri Kümesi

> [!NOTE]
> Mevcut ana dal eğitimi için gereken temel veri kümeleri açık kaynak olarak paylaşılmıştır; büyük ölçekli veri kümelerini kendiniz önceden işlemek zorunda kalmazsınız.

MiniMind eğitim veri kümesi indirme bağlantıları: [ModelScope](https://www.modelscope.cn/datasets/gongjy/minimind_dataset/files) | [HuggingFace](https://huggingface.co/datasets/jingyaogong/minimind_dataset/tree/main)

> Her şeyi klonlamanıza gerek yoktur, ihtiyacınız olan dosyaları tek tek indirebilirsiniz.

İndirilen veri kümesi dosyalarını `./dataset/` dizinine yerleştirin (✨ önerilen temel dosyaları belirtir):

```bash
./dataset/
├── agent_rl.jsonl (86MB)
├── agent_rl_math.jsonl (18MB)
├── dpo.jsonl (53MB)
├── pretrain_t2t_mini.jsonl (1.2GB, ✨)
├── pretrain_t2t.jsonl (10GB)
├── rlaif.jsonl (24MB, ✨)
├── sft_t2t_mini.jsonl (1.6GB, ✨)
└── sft_t2t.jsonl (14GB)
```

<details>
<summary>Not: Her Veri Kümesine Kısa Bakış</summary>

* `agent_rl.jsonl` -- Agentic RL ana dal eğitim verisi, `train_agent.py` çok turlu Tool-Use / CISPO / GRPO eğitimi için
* `agent_rl_math.jsonl` -- Agentic RL saf matematik tamamlayıcı verisi, nihai doğrulama hedefleri olan çok turlu akıl yürütme/araç kullanımı senaryolarına uygundur (RLVR için)
* `dpo.jsonl` -- RLHF aşaması tercih eğitimi verisi (DPO)
* `pretrain_t2t_mini`✨ -- `minimind-3` hafif ön eğitim verisi, hızlı yeniden üretime uygundur (önerilen ayar `max_seq_len≈768`)
* `pretrain_t2t` -- `minimind-3` ana dal ön eğitim verisi (önerilen ayar `max_seq_len≈380`)
* `rlaif.jsonl`✨ -- RLAIF eğitim veri kümesi; PPO/GRPO/CISPO ve diğer pekiştirmeli öğrenme algoritmalarının eğitimi için
* `sft_t2t_mini.jsonl`✨ -- `minimind-3` hafif SFT verisi (hızlıca bir Zero modeli eğitmek için), önerilen ayar `max_seq_len≈768`, içine bir miktar Tool Call örneği harmanlanmıştır
* `sft_t2t.jsonl` -- `minimind-3` ana dal SFT verisi, tam yeniden üretime uygundur, içine Tool Call örnekleri de harmanlanmıştır

Eğitim parametresi `max_seq_len` mutlak karakter sayısını değil, belirteç (token) uzunluğunu ifade eder.  
Bu projenin belirteçleyicisi Çince metinler için yaklaşık `1.5~1.7 karakter/belirteç`, saf İngilizce için `4~5 karakter/belirteç` sıkıştırma oranına sahiptir (veri dağılımına bağlı dalgalanmalar olabilir).  
Veri kümesi adlarında belirtilen "maksimum uzunluk" karakter cinsindendir; 100 karakterlik bir metin kabaca `100/1.5≈67` belirtece dönüştürülebilir.

Örneğin:
* Çince: `白日依山尽` (5 karakter) [`白日`,`依`,`山`,`尽`] şeklinde 4 belirtece ayrılabilir;
* İngilizce: `The sun sets in the west` (24 karakter) [`The `,`sun `,`sets `,`in `,`the`,`west`] şeklinde 6 belirtece ayrılabilir.

"Önerilen ayarlar", her veri kümesi için maksimum belirteç uzunluğunun kaba tahminlerini sunar.  
`max_seq_len` değerinin agresif ya da muhafazakâr biçimde ayarlanabileceğini, ancak her iki yönün de yan etkileri olduğunu unutmayın: `max_seq_len`'den kısa örnekler doldurma (padding) nedeniyle işlem gücünü israf ederken, uzun örnekler kesilme (truncation) nedeniyle bilgi kaybeder.

Pratikte hesaplama verimliliği ile anlamsal bütünlük arasında bir denge kurmak yeterlidir.

</details>

![dataset](./images/dataset.jpg)

> MiniMind ana dal eğitim verisi bileşimi ve önerilen kombinasyon şeması

<details>
<summary>Talimatlar ve Önerilen Eğitim Planları</summary>

* `minimind-3` ana dalı için `pretrain_t2t` + `sft_t2t` + `rlaif/agent_rl` aşamalı eğitim kombinasyonunun kullanılması önerilir.
* Sıfırdan bir Zero modelini en hızlı şekilde uygulamak için `pretrain_t2t_mini.jsonl` + `sft_t2t_mini.jsonl` veri kombinasyonunun kullanılması tavsiye edilir.
* Yeterli hesaplama kaynağına sahip olan veya performansı daha çok önemseyenlerin `minimind-3`'ü tam olarak yeniden üretmesi; tek bir GPU'su olan veya hızlı yeniden üretime öncelik verenlerin ise mini kombinasyonu kullanması önemle tavsiye edilir.
* Mevcut `sft_t2t / sft_t2t_mini` verilerine zaten Tool Call verileri entegre edilmiştir; bu nedenle genellikle ayrıca bağımsız bir Araç Çağırma SFT turuna gerek yoktur.

</details>
---

# 📌 Model

## Yapı (Structure)

`minimind-3` Dense, `transformers / llama.cpp / ollama / vllm` formatlarına daha kolay dönüştürülebilmesi için genel yapılandırması `Qwen3` ekosistemiyle hizalanmış bir Transformer Decoder-Only (Yalnızca Kod Çözücü) mimarisi kullanır:

* Pre-Normalization (Ön Normalizasyon) + RMSNorm kullanır.
* SwiGLU aktivasyon fonksiyonunu kullanır.
* YaRN ekstrapolasyon desteğiyle RoPE döner konumsal kodlamasını kullanır.
* `q_heads=8`, `kv_heads=4`, `max_position_embeddings=32768`, `rope_theta=1e6`.

`minimind-3-moe`, aynı yapı üzerinde MoE ileri beslemeli katmanlarını genişletir; uygulaması `Qwen3-MoE` tarzı yapılandırmayla uyumludur (paylaşılan uzman kaldırılmıştır).

* Mevcut varsayılan yapılandırma, daha düşük aktif parametreyle daha yüksek kapasite elde etmek için `4 uzman / top-1 yönlendirme` (4 experts / top-1 routing) şeklindedir.
* Uzman sayısı arttıkça eğitim, benzer boyuttaki yoğun (dense) bir modele göre çok daha yavaş hale gelebilir. Bu durum, yaygın olarak dile getirilen "MoE çıkarımı daha hızlıdır" iddiası karşısında mantığa aykırı görünebilir; ancak eğitim sırasında belirteçler önce uzmanlara göre sepetlere ayrılır (bucketing) ve ardından ayrı ayrı iletilir. Saf bir PyTorch uygulamasında çekirdek başlatma (kernel launch) ve çizelgeleme ek yükü hızla belirginleşir. Bu genellikle `Triton`, `DeepSpeed-MoE` veya `Megatron-LM` gibi özel kütüphaneler veya kaynaştırılmış (fused) MoE çekirdekleriyle optimizasyon gerektirir. MiniMind taşınabilirlik adına uygulamayı saf PyTorch'ta tuttuğundan, bu pratik bir ödünleşmedir. Mevcut uygulama altında `4 uzman / top-1` yapılandırması yoğun modele göre yalnızca yaklaşık `%50` daha yavaştır.

`minimind-3` serisinin mimari yapısı aşağıda gösterilmiştir:

![structure](./images/LLM-structure.jpg)
![structure-moe](./images/LLM-structure-moe.jpg)

Model yapılandırmasını değiştirmek için [./model/model_minimind.py](./model/model_minimind.py) dosyasına bakabilirsiniz. Referans model parametre sürümleri aşağıdaki tabloda sunulmuştur:

| Model Adı | Parametreler | len_vocab | max_pos | rope_theta | n_layers | d_model | kv_heads | q_heads | Not |
|------------|--------|-----------|---------|------------|----------|---------|----------|---------|------|
| minimind-3 | 64M | 6400 | 32768 | 1e6 | 8 | 768 | 4 | 8 | Dense |
| minimind-3-moe | 198M-A64M | 6400 | 32768 | 1e6 | 8 | 768 | 4 | 8 | 4 uzman / top-1 |
| minimind2-small | 26M | 6400 | 32768 | 1e6 | 8 | 512 | 2 | 8 | Tarihsel sürüm |
| minimind2-moe | 145M | 6400 | 32768 | 1e6 | 8 | 640 | 2 | 8 | Tarihsel sürüm |
| minimind2 | 104M | 6400 | 32768 | 1e6 | 16 | 768 | 2 | 8 | Tarihsel sürüm |


## Model Yapılandırması (Model Configuration)

Büyük dil modellerinde parametre konfigürasyonu konusunda [MobileLLM](https://arxiv.org/pdf/2402.14905), küçük modeller üzerinde oldukça temsili sistematik bir çalışma yürütmüştür. MiniMind gibi ~100M seviyesindeki modeller için `d_model` ve `n_layers` arasındaki denge yalnızca bir parametre dağıtımı meselesi olmayıp, eğitim kararlılığını ve nihai performansı da doğrudan etkiler.

Mevcut `minimind-3` ana dalı `dim=768, n_layers=8` konfigürasyonunu kullanır; bu temelde bir mühendislik ödünleşimidir: Daha sığ ağlar daha hızlı eğitilirken, `dim` değeri ciddi bir temsil darboğazını önleyecek kadar büyüktür. Bu da eğitim verimliliği, kararlılık ve nihai performans arasında makul bir denge sağlar.

<details>
<summary>Ayrıntılı Açıklamayı Görüntüle</summary>

Ölçekleme yasaları (scaling laws) küçük model rejiminde genellikle farklı davranır. Transformer parametre ölçeğini belirleyen temel mimari parametreler genellikle `d_model` ve `n_layers`'dır:

* `d_model`↑ + `n_layers`↓ -> geniş ve sığ
* `d_model`↓ + `n_layers`↑ -> dar ve derin

Klasik ölçekleme yasaları eğitim verisi boyutunun, parametre sayısının ve eğitim adımlarının rolünü vurgular; mimari farklılıkları ise genellikle ikincil planda tutar. Ancak küçük model rejiminde bu çıkarım her zaman geçerli olmaz.  
MobileLLM'in temel gözlemlerinden biri, sabit bir parametre bütçesi altında derinliğin genellikle genişlikten daha önemli olduğudur. Geniş ve sığ modellere kıyasla dar ve derin modeller soyut kavramları daha etkili bir şekilde öğrenme eğilimindedir.  
Örneğin, parametre sayısı `125M` veya `350M` olarak sabitlendiğinde, `30~42` katmana sahip dar modeller, yaklaşık `12` katmanlı geniş modellerden belirgin şekilde daha iyi performans gösterir; genel mantık yürütme, soru-cevap ve okuduğunu anlama gibi değerlendirmelerde benzer eğilimler görülür.

Bu bulgu, MiniMind'ın `d_model` ve `n_layers` etrafındaki kendi deneyleriyle de örtüşmektedir. Ancak "dar" olmanın da bir alt sınırı vardır: `d_model < 512` olduğunda temsil darboğazı çok daha belirginleşir ve sabit bir `q_head` altında aşırı küçük bir `d_head` değerini telafi etmek için fazladan katman eklemek genellikle yetersiz kalır.  
Tersine, `d_model > 1536` olduğunda katman eklemek genişliği daha da artırmaktan genellikle daha uygun maliyetlidir ve parametre-performans açısından daha iyi getiriler sağlar.

Referans olması açısından GPT-3'ün parametre ayarları aşağıda verilmiştir:  
![gpt3_config.png](./images/gpt3_config.png)

</details>
---

# 📌 Deneyler

## Ⅰ Eğitim Maliyeti

- **Zaman birimi**: saat (h)
- **Maliyet birimi**: CNY (￥); `7￥ ≈ 1 USD`
- **3090 kiralama fiyatı**: yaklaşık `1.3￥/h` (gerçek fiyatlar değişiklik gösterebilir)
- **Not**: Aşağıdaki sonuçlar, tek bir `3090` GPU üzerinde `minimind` modeli için yapılan ampirik tahminlerdir ve eğitim maliyetinin kolayca öngörülmesini amaçlar.

| Model Adı | Parametreler | pretrain_t2t_mini | sft_t2t_mini | toolcall | RLAIF |
|------------|--------|-------------------|--------------|----------|-------|
| minimind-3 | 64M | ≈1.21h<br/>≈1.57￥ | ≈1.10h<br/>≈1.43￥ | ≈0.9h<br/>≈1.17￥ | ≈1.1h<br/>≈1.43￥ |
| minimind-3-moe | 198M-A64M | ≈1.69h<br/>≈2.20￥ | ≈1.54h<br/>≈2.00￥ | ≈1.26h<br/>≈1.64￥ | ≈1.54h<br/>≈2.00￥ |

---

<details>
<summary>Eğitim Maliyeti Özeti ve Tahmini</summary>

> `minimind-3`
>> `pretrain_t2t_mini` + `sft_t2t_mini`
<br/>Tek bir `3090` GPU ile `1 epoch` yaklaşık `2.31` saat sürer, maliyeti yaklaşık `3.0` CNY'dir.
<br/>Sıfırdan bir `minimind-3 Zero` diyalog modeli eğitebilir.

> `minimind-3-moe`
>> `pretrain_t2t_mini` + `sft_t2t_mini`
<br/>Tek bir `3090` GPU ile `1 epoch` yaklaşık `3.23` saat sürer, maliyeti yaklaşık `4.2` CNY'dir.
<br/>`minimind-3-moe` modelinin temel diyalog sürümünü hızlıca elde edebilir.

> Yukarıdaki değerler tahmini olup yalnızca eğitim maliyeti için kaba bir referans niteliğindedir.

</details>

Tek bir `NVIDIA 3090` üzerinde `minimind zero`, yaklaşık `2` saat içinde tamamen sıfırdan eğitilebilir; bu da eğitim sürecini bireysel geliştiriciler için son derece erişilebilir kılar.

`8x H100` gibi daha üst düzey çoklu GPU kurulumlarında toplam eğitim süresi dakikalara indirilebilir. MiniMind her zaman büyük dil modeli eğitimini yeniden üretilebilir, pratik ve kolayca yinelenir kılmayı hedeflemiştir. Düşük maliyetli hızlı yeniden üretim bir pazarlama hilesi değildir; aşağıda referans olması amacıyla ilk dönem Zero tarzı örnek bir diyalog korunmuştur:

```text
👶: 请介绍一下自己。
🤖️: 作为人工智能，我没有实际的生活，也没有自我意识，所以没有自己的生活。我被设计成能够帮助用户解答问题、提供信息、进行对话等。我的设计和功能是由计算机科学、机器学习、人工智能技术和算法所构建的，我通过编程和算法实现。

👶: 推荐一些杭州的特色美食吧。
🤖️: 杭州有很多美味的特色美食，比如鸡肉串、鳗鱼头、水煮鱼、豆腐脑等。这些美食都非常美味，有着独特的风味和口感，绝对是值得一试的美食。

👶: 请为我讲解"大语言模型"这个概念。
🤖️: 大语言模型是一种人工智能技术，它使用大量的文本数据来训练模型，然后在不断的迭代中不断优化模型。它的目标是根据输入的数据来生成符合特定需求的文本，这些文本可以是任何你感兴趣的主题。

👶: Introduce the history of the United States, please.
🤖️: 您提到的"Introok's the believeations of theument." 这个名字来源于中国古代的"groty of of the change."
```

Bu sürüm temel diyalog kabiliyetine sahip olsa da olgusal bilgisi ve genelleme yeteneği henüz sınırlıdır; esasen Zero eğitim rotasının fizibilitesini gösteren erken bir referanstır.  
Zero model ağırlıkları `full_sft_zero_768.pth` olarak kaydedilmiştir (aşağıdaki MiniMind model dosyası bağlantılarına bakın); ilgileniyorsanız indirip diyalog performansını bizzat deneyimleyebilirsiniz.

---

## Ⅱ Ana Eğitim (Zorunlu)

> Tüm eğitim betikleri `cd ./trainer` dizini altından çalıştırılır.

### 1' Ön Eğitim (Pretrain):

Bir LLM'in öncelikle temel bilgileri ve dil kalıplarını parametrelerine sindirmesi gerekir. Yalnızca bu aşama yeterince kararlı olduktan sonra model soruları anlamaya, yanıtları düzenlemeye ve kullanılabilir bir üretim yeteneği geliştirmeye başlayabilir. Ön eğitim, modeli Vikipedi, haberler, kitaplar ve diyalog derlemleri gibi çok büyük miktarda metne maruz bırakır; böylece model olgusal bilgileri, dil kalıplarını ve bağlamlar arasındaki istatistiksel ilişkileri öğrenir. Bu aşama genellikle "denetimsizdir" (unsupervised): İnsanlar her satırı doğru ya da yanlış olarak etiketlemez; bunun yerine model devasa metinlerden örüntüler çıkarır ve dünya bilgisi ile dil yapısının içsel temsillerini aşamalı olarak inşa eder.  
En yalın ifadeyle, bu aşamadaki temel hedef **yüksek kaliteli sonraki belirteç tamamlama (next-token prediction)** yeteneğidir. Örneğin, "秦始皇" (Çin Şi Huang) girdisi verildiğinde model "是中国历史上的第一位皇帝" (Çin tarihindeki ilk imparatordur) şeklinde anlamsal ve olgusal olarak tutarlı bir devam üretebilmelidir.

```bash
# Yöntem 1
torchrun --nproc_per_node 1 train_pretrain.py # 1 tek GPU anlamına gelir, donanımınıza göre ayarlayın (>=2 yapabilirsiniz)
# Yöntem 2
python train_pretrain.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `pretrain_*.pth` olarak kaydedilir (`*` model boyutudur, her kaydetme bir öncekinin üzerine yazar).

![pretrain_loss](./images/pretrain_loss.jpg)
> `768dim` yapılandırmasıyla ön eğitim aşamasındaki kayıp (loss) eğrisi

```bash
# Ön eğitim sonuçları üzerinde basit test:
python eval_llm.py --weight pretrain

💬: 为什么天空是蓝色的
🧠: 天空之所以看起来是蓝色的，主要是因为太阳光进入大气层后，短波长的蓝光更容易被空气分子散射，因此人眼从各个方向接收到的蓝光会更多。

💬: 解释什么是机器学习
🧠: 机器学习是人工智能的一个重要分支，它通过数据训练模型，使系统能够自动学习规律，并在分类、预测、推荐、自然语言处理等任务中持续改进效果。
```

### 2' Denetimli İnce Ayar (SFT):

SFT yalnızca modelin "daha iyi sohbet etmesini" sağlamakla kalmaz; aynı zamanda modele yeni bilgiler, davranış kalıpları ve yanıt stilleri aşılamaya da devam edebilir. MiniMind'ın mevcut ana dalındaki `14GB`'lık SFT verisi ile bu aşama artık basit bir format hizalamasından öteye geçmiş ve devam eden bir ara eğitim sürecine (mid-training) yaklaşmıştır.  
Ön eğitim modelin geniş çapta okuyup temel dil yeteneğini kazanmasını sağlıyorsa, SFT daha yüksek kaliteli ve amaca yönelik veriler üzerinde daha ileri bir işleme gerçekleştirir. Modelin çok turlu diyalog, soru-cevap, araç çağırma ve düşünme etiketi etkileşim formatlarına uyum sağlamasına yardımcı olurken, belirli bilgi dağılımlarını, görev kalıplarını ve asistan stillerini de parametrelere kazır.  
MiniMind özelinde SFT aşaması, modelin depodaki çok turlu diyalog şablonuna uyum sağlamasını mümkün kılar. Model `user / assistant / system / tool` rol yapısını kademeli olarak kavrarken, talimat takibi, kararlı yanıt verme ve görev tamamlama yeteneklerini daha da güçlendirir.  
Mevcut eğitimde bellek kullanımını (VRAM) ve eğitim verimliliğini dengelemek amacıyla talimat ve yanıt uzunluklarına kırpma (truncation) uygulanmaktadır. İleride daha uzun bağlamlara ihtiyaç duyulursa, az sayıda uzun bağlamlı örnekle artımlı ince ayar yapılabilir. Çıkarım sırasında YaRN ekstrapolasyonu, ek eğitime gerek kalmadan bağlam uzunluğunu 2048 ve üzerine genişletebilir.

```bash
# Yöntem 1
torchrun --nproc_per_node 1 train_full_sft.py
# Yöntem 2
python train_full_sft.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `full_sft_*.pth` olarak kaydedilir (`*` model boyutudur, her kaydetme bir öncekinin üzerine yazar).

![sft_loss](./images/sft_loss.jpg)
> `768dim` yapılandırmasıyla SFT aşamasındaki kayıp (loss) eğrisi

```bash
# SFT sonuçları üzerinde basit test:
python eval_llm.py --weight full_sft

💬: 解释什么是机器学习
🧠: 机器学习是人工智能的核心技术之一，通过算法让计算机从数据中学习规律，并持续改进预测或决策效果，常见应用包括推荐系统、图像识别、语音识别和自然语言处理。

💬: 推荐一些中国的美食
🧠: 例如北京烤鸭、兰州拉面、四川火锅、广东早茶、小笼包和麻婆豆腐等，这些美食分别代表了不同地区的风味特点，也很适合作为了解中国饮食文化的入门选择。
```

## Ⅲ Diğer Eğitimler (İsteğe Bağlı)

> Tüm eğitim betikleri `cd ./trainer` dizini altından çalıştırılır.

### 3' Bilgi Damıtma (Knowledge Distillation - KD)

Bilgi damıtma genel olarak kara kutu (black-box) ve beyaz kutu (white-box) olarak ikiye ayrılabilir. Mevcut MiniMind ana dalı her iki yaklaşımı da farklı vurgularla içerir.
* Kara kutu damıtma: Daha yaygındır ve mevcut ana dalın fiili uygulamasıyla daha uyumludur. Kesin konuşmak gerekirse, temelde öğretmen çıktılarına yönelik denetimli ince ayardır; yani sert etiketlere (hard labels) dayalı eğitime devam etmektir. LLM'ler popülerleştikçe, "güçlü model çıktılarına karşı ince ayar yapma" yaklaşımı genel olarak damıtma çatısı altında değerlendirilmeye başlanmış ve yaygın olarak kara kutu damıtma olarak adlandırılmıştır. Yanıtları, stilleri ve davranış kalıplarını öğrenmeye odaklanır — öğrenci model yalnızca "öğretmenin ne söylediğini" görür ancak öğretmenin bu yargıya içeride nasıl vardığını göremez. `DeepSeek R1`, `Qwen3` modellerinden gelen yüksek kaliteli yanıtlar ile `tool call`, `reasoning`, düşünce zinciri verileri kara kutu damıtma sinyalleri olarak görülebilir; MiniMind'daki mevcut ana dal `full_sft` verisi zaten bu yaklaşımın önemli bir bölümünü içerir.
* Beyaz kutu damıtma: Bir adım daha ileri gider; yalnızca öğretmenin nihai çıktılarını öğrenmekle kalmaz, öğretmenin belirteç dağılımı (token distribution) düzeyindeki tercihlerini de öğrenir. Kara kutu damıtmaya kıyasla, öğretmen modelin çıktı katmanından gelen daha ince taneli dağılım bilgisinden yararlanır; böylece öğrenci model sadece "standart cevabı" değil, aday belirteçler arasındaki göreceli öğretmen tercihlerini de öğrenir. `train_distillation.py` dosyasına karşılık gelen mevcut uygulama, halihazırda SFT'si tamamlanmış ağırlıkların üzerine öğretmen modelin sağladığı dağılım sinyalleriyle öğrenci modeli eğitmeye devam eder; bu da onu MiniMind'ın damıtma sürecini anlamak için harika bir referans uygulama haline getirir.

Kara kutu damıtma, temelde öğretmen tarafından üretilen yanıtlar üzerinde denetimli ince ayara eşdeğerdir:
```math
\mathcal{L}_{blackbox} = \mathrm{CE}(y_{teacher}, p_{student})
```

Beyaz kutu damıtma ise tipik olarak denetimli kayba ek olarak öğretmen dağılımına da uydurma yapar:
```math
\mathcal{L}_{whitebox} = \alpha \mathcal{L}_{CE} + (1-\alpha) T^2 \mathrm{KL}(p_t^T \parallel p_s^T)
```

`train_distillation.py` betiği, beyaz kutu damıtma sürecini anlamak için bir referans uygulama olarak tasarlanmıştır: Öğretmen/öğrenci ikili model yüklemesini, `CE + KL` karma kaybını, sıcaklık ölçeklemesini (temperature scaling), MoE ve dense kombinasyon damıtmasını, ayrıca kontrol noktası devam ettirme ve dağıtık eğitim gibi temel ayrıntıları sergiler.

```bash
# Yöntem 1
torchrun --nproc_per_node 1 train_distillation.py
# Yöntem 2
python train_distillation.py
```

### 4' LoRA (Düşük Dereceli Uyarlama - Low-Rank Adaptation)

LoRA, yaygın bir Parametre Açısından Verimli İnce Ayar (PEFT) yöntemidir. Tam parametreli ince ayara kıyasla, orijinal model ağırlıklarını değiştirmeden yalnızca az sayıda yeni eklenen parametreyi günceller; bu da eğitim maliyetini düşürür ve dikey alan uyarlamasına daha uygun hale getirir.  
Temel fikri, orijinal ağırlık matrislerinin yanına düşük dereceli artımsal kollar eklemek ve yalnızca bu düşük dereceli parametreleri eğiterek kabiliyet transferini nispeten küçük bir maliyetle tamamlamaktır. İlgili uygulamalar `model_lora.py` ve `train_lora.py` dosyalarında bulunabilir; tüm hat üçüncü taraf paketleyicilere dayanmadan tamamen elle yazılmıştır.

```bash
# train_lora.py genellikle CPU üzerinde bile oldukça hızlı tamamlanabilir
# Yöntem 1
cd trainer && torchrun --nproc_per_node 1 train_lora.py
# Yöntem 2
cd trainer && python train_lora.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `lora_xxx_*.pth` olarak kaydedilir (`*` model boyutudur, her kaydetme bir öncekinin üzerine yazar).

LoRA, "genel yetenekleri mümkün olduğunca korurken modelin özel alanlara veya dikey senaryolara hızlıca nasıl uyarlanacağı" gibi sorunları çözmek için son derece uygundur. Örneğin, temel model tıp bilgisinden yoksun olduğunda, nispeten küçük bir maliyetle daha iyi alan performansı elde etmek için orijinal modelin üzerine tıbba yönelik bir LoRA ağırlık katmanı yerleştirilebilir.  
Genellikle sadece çok turlu diyalog formatındaki verileri aynı şekilde hazırlamanız, bunları `lora_xxx.jsonl` dosyasına yerleştirmeniz ve ardından yeni `LoRA` model ağırlıklarını elde etmek için depo kökünden `cd trainer && python train_lora.py` komutunu çalıştırmanız yeterlidir.

Örnek 1: Dikey alan verisi

```jsonl
 {"conversations": [{"role": "user", "content": "请问颈椎病的人枕头多高才最好？"}, {"role": "assistant", "content": "颈椎病患者选择枕头的高度应该根据..."}]}
 {"conversations": [{"role": "user", "content": "请问xxx"}, {"role": "assistant", "content": "xxx..."}]}
```

Örnek 2: Benlik bilinci (Identity) verisi

```jsonl
 {"conversations": [{"role": "user", "content": "你叫什么名字？"}, {"role": "assistant", "content": "您好，我名叫 MiniMind，是由 Jingyao Gong 开发的人工智能助手。我可以帮助你解决各种问题，包括翻译、推荐内容等等。"}]}
 {"conversations": [{"role": "user", "content": "你是谁"}, {"role": "assistant", "content": "您好，我是 MiniMind，由 Jingyao Gong 创建。我的主要职责是提供准确的回答和帮助。"}]}
```

Bu noktada, temel modelin genel yeteneklerini korurken belirli alan performansını artırmak amacıyla [temel model + LoRA ağırlıkları] birlikte kullanılabilir. Eğitimden sonra `eval_llm.py` aracılığıyla basit testler de yapılabilir:

```bash
# Not: weight parametresi temel model türünü belirtir ve train_lora eğitimi sırasında kullanılan temel modelle tutarlı olmalıdır
python eval_llm.py  --weight full_sft --lora_weight lora_medical

👶: 我最近经常感到头晕，可能是什么原因？
🤖️: 头晕可能是由于多种原因，包括但不限于：心脏疾病、眼睛损伤、过敏反应、皮肤问题、过敏反应、压力、焦虑、疲劳、药物副作用、性功能障碍或者其他...

python eval_llm.py  --weight full_sft --lora_weight lora_identity

👶: 你和openai是什么关系？
🤖️: 我是 MiniMind，一个由 Jingyao Gong 开发的人工智能助手。我通过自然语言处理和算法训练来与用户进行交互。
```

Not: Yeterli veriniz varsa doğrudan `full_sft` tam parametreli ince ayar da yapabilirsiniz. Bu durum genellikle genel veriler ile alana özgü verilerin dikkatli bir şekilde karıştırılmasını gerektirir; aksi takdirde model, dikey alan örneklerine aşırı uyum (overfitting) nedeniyle genel yeteneklerinin bir kısmını kaybedebilir.

> `LoRA` ağırlıkları `scripts/convert_model.py` içindeki `convert_merge_base_lora` kullanılarak temel modele geri birleştirilebilir ve yeni eksiksiz model ağırlıkları olarak dışa aktarılabilir:

```bash
cd scripts && python convert_model.py
```

### **5' Araç Çağırma ve Uyarlanabilir Düşünme (Tool Calling & Adaptive Thinking)**

`2026-03` tarihinden itibaren bağımsız `train_reason.py` depodan kaldırılmıştır.  
Mevcut sürüm artık `reason_*.pth` ağırlıklarını ayrı olarak tutmamakta, bunun yerine "düşünce sürecinin açıkça çıktı olarak verilip verilmeyeceğini" `chat_template`, `<think>` etiketleri, `open_thinking` anahtarı ve sonraki SFT / RLAIF süreçleri üzerinden tek tip biçimde modellemektedir.

#### 5.1 Araç Çağırma (Tool Calling)

Mevcut `toolcall` yeteneği `sft_t2t` / `sft_t2t_mini` ana dal verilerine dâhil edilmiştir; bu nedenle genellikle ek bir Araç Çağırma SFT aşamasına gerek kalmaz; varsayılan `full_sft` ağırlıkları zaten temel Tool Call yeteneğine sahiptir. Bu bölüm için mevcut eğitim verisi esas olarak `qwen3-4b` modelinden üretilen yaklaşık `100K` örnek içerir ve araç listesi saat sorgulama, matematik hesaplama ve hava durumu kontrolü gibi yaklaşık `10` simüle edilmiş özel aracı kapsar. Bu aşamada genelleme yeteneği henüz sınırlıdır. Tool Calling örnekleri OpenAI tarzı çok turlu mesaj formatını takip eder:

```jsonl
{
  "conversations": [
    {"role": "system", "content": "# Tools ...", "tools": "[...]"},
    {"role": "user", "content": "帮我算一下 256 乘以 37 等于多少"},
    {"role": "assistant", "content": "", "tool_calls": "[{"name":"calculate_math","arguments":{"expression":"256 * 37"}}]"},
    {"role": "tool", "content": "{"result":"9472"}"},
    {"role": "assistant", "content": "256 乘以 37 等于 9472。"}
  ]
}
```

Burada `tools` `system` mesajına eklenir ve `tool_calls` `assistant` mesajına iliştirilir. Eğitim sırasında `chat_template` bunları otomatik olarak `<tool_call>...</tool_call>` ve `<tool_response>...</tool_response>` bölümlerine açarak modelin yerel araç çağırma formatını doğrudan öğrenmesini sağlar.

Araç Çağırma diyalog şablonu şu şekilde ayrıştırılacak şekilde birleştirilmiştir:

```text
<tool_call>{"name": "...", "arguments": {...}}</tool_call>
<tool_response>{...tool result...}</tool_response>
```

Ayrıca `eval_toolcall.py` aracılığıyla doğrudan basit testler çalıştırabilirsiniz:

```bash
python eval_toolcall.py --weight full_sft

💬: 现在几点了？
🧠: <tool_call>{"name": "get_current_time", "arguments": {"timezone": "Asia/Shanghai"}}</tool_call>
📞 [Tool Calling]: get_current_time
✅ [Tool Called]: {"datetime": "2026-03-15 17:18:22", "timezone": "Asia/Shanghai"}
🧠: 现在是2026年3月15日17时18分22秒。
```

#### 5.2 Uyarlanabilir Düşünme (Adaptive Thinking)

`minimind`, açık düşünme yeteneğini şablon düzeyinde birleştirir; bu da güncel ana akım büyük modellerin şablon tasarımıyla tamamen uyumludur:

- `open_thinking=0`: Varsayılan olarak boş bir `<think>\n\n</think>` ekler, model doğrudan yanıt verme eğilimindedir;
- `open_thinking=1`: Şablon `<think>` başlangıç etiketini önceden ekler ve model açık düşünme sürecini ve nihai yanıtı üretmeye devam eder;
- CLI, OpenAI-API ve WebUI bu anahtarı destekler.

Daha kesin bir ifadeyle yaklaşım, artık ayrı bir düşünme modeli eğitmek değil, "açıkça düşünüp düşünmemeyi" `chat_template` seviyesine indirmektir. Şablon katmanı `<think></think>` yapısını saklı tutar ve aynı model çıkarım sırasında `open_thinking` aracılığıyla dinamik olarak geçiş yapar. Eğitim sırasında boş `think`, açık `reasoning_content` ve `thinking_ratio` örneklemeleri harmanlanır; böylece model ne zaman açıkça düşüneceğini ve ne zaman doğrudan cevap vereceğini kademeli olarak öğrenir.

```bash
# Yanıtları test edin
python eval_llm.py --load_from ./minimind-3 --open_thinking 1
```

OpenAI-API-SDK kullanımı:

```python
response = client.chat.completions.create(
    model="minimind",
    messages=[{"role": "user", "content": "你是谁？"}],
    # ...
    extra_body={"chat_template_kwargs": {"open_thinking": True}} # Düşünme anahtarı
)
```

Not: Araç Çağırma ve açık düşünme aynı anda etkinleştirildiğinde model genellikle düşünme sürecini kararlı biçimde çıktı olarak veremez. Bunun nedeni, mevcut eğitim verilerinde "akıl yürütme ve araç çağırmanın bir arada bulunduğu" ortak damıtma örneklerinin henüz yetersiz olmasıdır; bu nedenle model bu iki yeteneğin koordineli ifadesini henüz tam olarak öğrenmemiştir.
---

## Ⅳ Pekiştirmeli Öğrenme (İsteğe Bağlı)

Büyük dil modellerinin eğitim sonrası (post-training) uygulamalarında temel olarak iki yaygın pekiştirmeli öğrenme yolu bulunur:

1. **İnsan Geri Bildirimiyle Pekiştirmeli Öğrenme (RLHF - Reinforcement Learning from Human Feedback)**

- Model çıktılarını **insan** tercih değerlendirmeleri üzerinden puanlayarak eğitir; böylece modelin insan değerleri ve tercihleriyle daha uyumlu içerikler üretmesini sağlar.

2. **YZ Geri Bildirimiyle Pekiştirmeli Öğrenme (RLAIF - Reinforcement Learning from AI Feedback)**

- Doğrudan insan etiketlemesine bağımlı kalmadan, geri bildirim sağlamak için **yapay zeka modellerini** veya otomatik olarak doğrulanabilir diğer mekanizmaları kullanır.
- Burada geniş anlamıyla "YZ geri bildirimi"; kural fonksiyonlarını, Doğruluk Zeminini (Ground Truth), kod yorumlayıcılarını, ortam geri bildirimini ve diğer otomatik sinyalleri de kapsayacak şekilde genişletilebilir.

| Tür  | Hakem (Judge) | Avantajlar | Dezavantajlar |
|-------|-------|------------|---------------|
| RLHF  | İnsan | Gerçek insan tercihlerine daha yakın | Yüksek maliyet, düşük verimlilik |
| RLAIF | Model / Kural | Otomatik, son derece ölçeklenebilir | Gerçek insan tercihlerinden sapabilir |

Her ikisi de temelde bir tür "**geri bildirim**" kullanarak model davranışını optimize etme pekiştirmeli öğrenme paradigmasına aittir.

Ancak pratik uygulamada farklılıkları yalnızca geri bildirim kaynağından ibaret değildir: Ödülün doğrulanabilir olup olmadığı, sürekli olup olmadığı, ortam etkileşimine dayanıp dayanmadığı ve tüm turun (episode) sonuna kadar gecikmeli olup olmadığı gibi unsurlar eğitim biçimini ve mühendislik uygulamasını doğrudan etkiler.


### 👀 PO Algoritmalarına Birleşik Bir Bakış

Belirli algoritmaların uygulanmasına geçmeden önce, tüm Politika Optimizasyonu (PO - Policy Optimization) algoritmalarının ortak paydasını kendi minimalist bakış açımdan açıklamak isterim.

En basit ifadeyle, burada tartışılan tüm PO algoritmaları tek bir beklentiyi optimize eder:

$$\mathcal{J}_{PO} = \mathbb{E}_{q \sim P(Q),\, o \sim \pi_\theta(\cdot \mid q)} \left[ \underbrace{\Phi(r_t, A_t)}_{\text{politika hedefi}} - \underbrace{h(\text{KL}_t)}_{\text{düzenlileştirme terimi}} \right]$$

Eğitim sırasında yalnızca **negatif amaç fonksiyonunu en aza indirmek (minimize etmek)** gerekir:

$$\mathcal{L}_{PO} = -\mathcal{J}_{PO}$$

Bu çerçeve yalnızca üç temel bileşen içerir:
* **Politika terimi** $\Phi(r_t, A_t)$: Olasılık oranı $r_t$ ve avantaj $A_t$'yi birleştirerek politikanın nasıl güncelleneceğini belirler
* **Avantaj terimi** $A_t$: Avantajın nasıl hesaplanacağını belirler, bu son derece önemlidir! Büyük modellerin belirli integralleri doğru çözmesi şaşırtıcı değildir; ancak küçük modeller için toplama ve çıkarmayı doğru yapmak bile genellikle pozitif bir avantaj sağlar
* **Düzenlileştirme terimi** $h(\text{KL}_t)$: $\text{KL}_t$ değişim büyüklüğünü sınırlandırarak referans modelden çok fazla uzaklaşmayı veya aşırı katı kısıtlanmayı önler

<details>
<summary>(Genişlet) Gösterim Kılavuzu</summary>

| Sembol | Anlamı | Açıklama | Aralık |
|--------|---------|-------------|-------|
| $q$ | Soru / İstem (Prompt) | $P(Q)$ veri kümesinden örneklenir | - |
| $o$ | Model çıktı dizisi | $\pi$ politikası tarafından üretilir | - |
| $r_t$ | Olasılık oranı | $r_t = \frac{\pi_\theta(o_t \mid q, o_{<t})}{\pi_{\mathrm{old}}(o_t \mid q, o_{<t})}$ | $(0, +\infty)$ |
| $A_t$ | Avantaj fonksiyonu | Belirli bir eylemin taban çizgisine (baseline) göre ne kadar iyi olduğunu ölçer | $(-\infty, +\infty)$ |
| $\text{KL}_t$ | KL ıraksaması | Politikanın referans modelden çok uzaklaşmasını önler | $[0, +\infty)$ |

</details>

Farklı **xxPO algoritmaları**, temelde bu üç bileşen için yapılan farklı tasarımların somutlaştırılmış örnekleridir!

---

### **6' İnsan Geri Bildirimiyle Pekiştirmeli Öğrenme (RLHF)**

Önceki eğitim adımlarında model temel diyalog yeteneğini kazanmıştı; ancak bu yetenek tamamen kelime zinciri tamamlamaya dayanıyordu ve pozitif/negatif örnek teşviklerinden yoksundu.  
Bu noktada model hangi yanıtların iyi, hangi yanıtların kötü olduğunu henüz bilmez. İnsan tercihleriyle daha iyi hizalanmasını, insanları rahatsız eden yanıtlar üretme olasılığını azaltmasını isteriz.  
Bu süreç, modelin yeni bir eğitim oturumuna katılmasına, nasıl cevap vereceğini daha iyi anlamak için örnek çalışanları pozitif örnek, isteksiz çalışanları ise negatif örnek olarak almasına benzer.

#### 6.1 Doğrudan Tercih Optimizasyonu (Direct Preference Optimization - DPO)

Doğrudan Tercih Optimizasyonu (DPO) algoritması, kayıp fonksiyonu:

$$\mathcal{L}_{DPO} = -\mathbb{E}\left[\log \sigma\left(\beta \left[\log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)\right]$$

Burada:
- **Politika terimi**: $f(r_t) = \log r_w - \log r_l$ (seçilen ile reddedilen arasındaki olasılık oranını karşılaştırır)
- **Avantaj terimi**: $g(A_t)$ = açık bir avantaj terimi yoktur (tercih karşılaştırmasıyla örtük olarak yansıtılır)
- **Düzenlileştirme terimi**: $h(\text{KL}_t)$ = $\beta$ parametresinde örtüktür (referans modelden sapma derecesini kontrol eder)

Özellikle:
- DPO, PPO'nun KL kısıtlı hedefinden tercih çiftleri için analitik bir eğitim hedefi türeterek "seçilenin reddedilene tercih edilme" log-olasılık oranını doğrudan maksimize eder; Reward/Value modellerini eşzamanlı olarak eğitmeye gerek kalmaz. DPO yalnızca `actor` ve `ref` modellerini çalıştırmaya ihtiyaç duyar; düşük bellek kullanımı, kararlı yakınsama ve basit bir uygulama sunar.
- Eğitim paradigması: Off-policy'dir; statik bir tercih veri kümesi kullanır, birden çok epoch boyunca yinelenebilir; Ref modeli sabittir (çıktıları önceden önbelleğe alınabilir).
- DPO'nun kısıtı, çevrim içi (online) keşif yapmaması ve daha çok "tercih/güvenlik" konularındaki insan değeri hizalamasına uygun olmasıdır; "modelin problemleri doğru çözüp çözemediği" gibi entelektüel yetenekleri geliştirme gücü sınırlıdır (elbette bu durum veri kümesine de bağlıdır; insan değerlendirmesiyle büyük ölçekte pozitif ve negatif örnekler toplamak oldukça zordur).

```bash
# Yöntem 1
torchrun --nproc_per_node 1 train_dpo.py
# Yöntem 2
python train_dpo.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `dpo_*.pth` olarak kaydedilir (`*` model boyutudur, her kaydetme bir öncekinin üzerine yazar).

### 7' Yapay Zeka Geri Bildirimiyle Pekiştirmeli Öğrenme (RLAIF)

Burada ufak bir adlandırma uyarısı yapmak gerekir. Bu bölüme kesin olarak tam oturmasa da yine de `RLAIF` demeyi sürdürüyorum. Doğrulanabilir ödüllere dayanan RLVR gibi yaklaşımların kendi soy kütüğü vardır ve YZ geri bildiriminin dar tanımına tam olarak sığmazlar.  
Ancak "YZ" daha geniş yorumlanırsa isim yine de savunulabilir: Ödüller ödül modellerinden, hakem modellerden veya diğer akıllı ajanlardan gelebileceği gibi kural fonksiyonlarından, Doğruluk Zemininden (Ground Truth), araç çağırma sonuçlarından, ortam durumlarından ve diğer otomatik elde edilebilir sinyallerden de gelebilir. Kurallar yeterince karmaşık ve sembolik sistem yeterince zengin olduğunda, bu sinyaller ile "akıllı geri bildirim" arasındaki sınır her zaman net değildir.  
Bu nedenle bu bölüm, SFT sonrasında **insan kaynaklı olmayan, otomatik olarak elde edilebilen çeşitli geri bildirim sinyallerini** kullanan pekiştirmeli öğrenmeye odaklanır. Örneğin, bir matematik cevabının doğru olup olmadığı, üretilen kodun test senaryolarını geçip geçmediği veya akıl yürütme sürecinin beklenen formatı takip edip etmediği otomatik olarak değerlendirilebilir.  
Tek turlu doğrulanabilir görevlerde bu geri bildirim genellikle anlık bir ödüle yakındır. Agentic RL senaryolarında ise ödüller daha çok çok adımlı etkileşimin sonuna kadar ertelenir veya doğrudan ortamın kendisinden gelir.  
Ortak özellikleri genellikle **çevrim içi eğitim (on-policy training)** ve **yüksek ölçeklenebilirliktir**: Pahalı insan etiketlemesine gerek duyulmaz ve çevrim içi deneme-yanılma için çok sayıda eğitim örneği üretilebilir.

MiniMind **2+N** temel ve öncü RLAIF yöntemini uygulamıştır:
* **PPO**, **GRPO** — büyük ölçekte doğrulanmış klasik RL algoritmaları
* N öncü RL algoritması (deneysel temelde periyodik olarak güncellenir)

**1️⃣ Veri Kümesi Hazırlığı (Zorunlu)**

Mevcut ana dal, RLAIF eğitim verisi olarak `rlaif.jsonl` dosyasını kullanır. Yaklaşık `20MB` boyutundadır, önceki `rlaif-mini.jsonl`'ye göre daha eksiksizdir ve PPO / GRPO / CISPO eğitim davranışını doğrudan doğrulamak için daha uygundur.

Veri formatı SFT ile tutarlıdır, ancak assistant içeriğine gerek yoktur; çünkü eğitim sırasında tamamen $\Pi$ politika modeli tarafından örnekleme yoluyla gerçek zamanlı olarak üretilir. Dolayısıyla şuna benzer:

```json
{
    "conversations": [
        {"role": "user", "content": "请解释一下什么是光合作用？"},
        {"role": "assistant", "content": "无"}
    ]
}
```

RLAIF eğitim sürecinde model, kullanıcının sorusuna göre 1 veya daha fazla aday yanıt üretir ve ardından bir ödül fonksiyonu/modeli bu yanıtları puanlar.  
Yüksek puanlı yanıtlar teşvik edilir ($\Pi$ politika olasılığı artırılır) ve düşük puanlı yanıtlar bastırılır ($\Pi$ politika olasılığı azaltılır). Bu "puanla -> ayarla" döngüsü pekiştirmeli öğrenmenin merkezindedir.

**2️⃣ Ödül Mekanizması Hazırlığı (Zorunlu)**

RLAIF eğitimi hesaplanabilir bir tür ödül sinyali gerektirir; bu bir ödül modelinden, kural fonksiyonlarından, Doğruluk Zemini doğrulamasından veya ortam geri bildiriminden gelebilir. MiniMind şu anda varsayılan olarak Ödül Modeli yolunu gösterir.

Burada temel ödül modeli olarak küçük ve kaliteli `InternLM2-1.8B-Reward` ([ModelScope](https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-1_8b-reward) | [HuggingFace](https://huggingface.co/internlm/internlm2-1_8b-reward)) modelini seçiyoruz.

Ödül modeli indirildikten sonra minimind projesinin **kardeş dizinine** yerleştirilmelidir; önerilen yapı şu şekildedir:

```
root/
├── minimind/                    # MiniMind projesi
│   ├── model/
│   └── ...
└── internlm2-1_8b-reward/       # Ödül modeli
    ├── config.json
    ├── model.safetensors
    └── ...
```

<details>
<summary><b>Ödül Mekanizması Seçimi ve MiniMind Kısıtları (Genişletmek için Tıklayın)</b></summary>

**1. Ödül Mekanizmalarının Çeşitliliği**

RLAIF'teki "ödül sinyali" kaynakları son derece esnek olabilir:

- **Model tabanlı ödüller**: Özel bir Ödül Modeli (InternLM2-Reward gibi) kullanılabilir veya puanlama için istemlerle genel bir LLM (Qwen3-as-a-Judge gibi) tercih edilebilir. Ödül modelinin ölçeği ve mimarisi serbestçe seçilebilir.

- **Kural tabanlı ödüller**: Kural fonksiyonlarına dayalı ödül sinyalleri oluşturulabilir, örneğin:
  - Matematik problemi cevap doğruluğu denetimi (Doğruluk Zemini karşılaştırması)
  - SQL çalıştırma başarı oranı ve sonuç doğruluğu
  - Kod yorumlayıcı çalıştırma sonuçları (pass@k)
  - Araç çağırma dönüş durumu (API başarı/başarısızlık)
  - Format uyumluluğu kontrolü (JSON/XML ayrıştırma)
  - Akıl yürütme zinciri eksiksizliği değerlendirmesi (CoT adım sayısı)

- **Ortam tabanlı ödüller**: Ajan (Agent) senaryolarında, ortam geri bildiriminin kendisi doğal bir ödül görevi görür (oyun skorları, araştırma eksiksizliği, görev tamamlama oranı vb.).

"Yanıt kalitesini" ölçebilen her mekanizma bir RL ödül kaynağı olabilir. DeepSeek R1 tipik bir örnektir: Ek bir Ödül Modeline ihtiyaç duymadan, ödül olarak matematik cevabının doğruluğunu kural fonksiyonlarıyla denetler.

**2. MiniMind Kısıtı: Ödül Seyrekliği (Reward Sparsity) Problemi**

RLAIF eğitimi hem akıl yürüten (reasoning) hem de akıl yürütmeyen modelleri hedefleyebilir; fark yalnızca formattadır.

Ancak MiniMind gibi son derece küçük 0.1B parametreli ve yetenekleri sınırlı modeller için genel görevlerde (R1 tarzı matematik veri kümeleri gibi) ciddi Ödül Seyrekliği sorunlarıyla karşılaşılır:

- **Olay**: Model tarafından üretilen aday yanıtların neredeyse tamamı yanlıştır, bu da tüm ödül puanlarının $r(x,y) \approx 0$ olmasına yol açar
- **Sonuç**: Avantaj fonksiyonu $A(x,y) = r(x,y) - b(x) \approx 0$ olur, politika gradyan sinyali kaybolur ve $\theta$ parametreleri etkili bir şekilde güncellenemez

Bu durum, ilkokul öğrencisine üniversite giriş sınavı matematik sorularını çözdürmeye benzer — kaç deneme yaparsa yapsın hep sıfır çeker ve puan farklarından bir iyileştirme stratejisi öğrenemez. Dolayısıyla bu, RL algoritmasının prensiplerinden kaynaklanan temel bir kısıttır.

Bu sorunu hafifletmek için MiniMind'ın uygulaması **model tabanlı sürekli ödül sinyallerini** seçmiştir:

- Ödül Modeli, ikili (binary) 0/1 yerine sürekli puanlar (-2.5 ile +3.0 arası gibi) üretir
- Tüm yanıt kalitesi zayıf olduğunda bile "daha da kötü" (-3.0) ile "kötü" (-2.8) arasındaki ince farkları ayırt edebilir. Bu tür **yoğun ve sürekli** ödül sinyalleri avantaj fonksiyonu $A(x,y)$ için sıfır olmayan gradyanlar sağlayarak politika ağının artımsal olarak optimize edilmesini mümkün kılar
- Birden fazla ödül kaynağı da harmanlanabilir: $r_{\text{toplam}} = \alpha \cdot r_{\text{model}} + \beta \cdot r_{\text{kural}}$ (örneğin, hem think etiketi format ödülünü denetleme hem de yanıt kalitesinin kendisi için ödül puanını birleştirme)
- MiniMind uygulamasında, kural tabanlı ikili ödüller ile yeteneğin ötesindeki zorluk seviyelerini (MATH500 gibi) doğrudan kullanmaktan kaçının; bu durum kolayca tamamen sıfır ödüllere yol açar;
- Ödül puanlarının varyansını $\text{Var}(r)$ gözlemleyerek eğitimi izleyin; 0'a yakın kalıyorsa verilerin veya ödül mekanizmasının ayarlanması gerekir.

**Üretim düzeyindeki büyük model Agentic RL senaryoları için**:

Gerçek Ajan sistemlerinde (kod üretimi, araç çağırma, çok turlu arama-planlama-yürütme zincirleri), ödüller "bölümün tamamı üzerinden ertelenmiş hesaplama" şeklinde farklı bir paradigmayı izler:

- LLM'in belirteç belirteç araç çağırma talimatları (tool_call) üretmesi, ayrıştırmadan (tool_parse) ve araç çalıştırmadan (tool_exec) geçmesi, ardından bir sonraki adımı sürdürmek için sonuçları bağlama eklemesi gerekir; bu durum tamamlanana kadar tekrarlanır.
- Eksiksiz bir görev zinciri, sonlandırma koşulu karşılanana ve tek bir toplam ödül hesaplanana kadar (görevin tamamlanıp tamamlanmadığı, testlerin geçip geçmediği, hedefin vurulup vurulmadığı gibi) birden fazla çağrı + düşünme içerir.

Bu nedenle Agentic RL seyrek/gecikmeli ödül düzenine daha yakındır: Gradyan geri yayılımı yalnızca "tüm bölüm sona erdikten sonra" gerçekleşir; bu da tek bir diyalog turunda "anında puanlayıp anında güncelleyen" Agentik olmayan RL görevlerinden çok farklıdır.  
Bu durum aynı zamanda Ajan görevlerinin statik Ödül Modelleri puanlaması yerine neden çevre tabanlı ödüllere daha fazla yöneldiğini de açıklar:

- **Çevre etkileşimi geri bildirimi**: Nihai olarak çalıştırma sonuçlarına dayanır (kodun başarıyla çalışıp çalışmadığı, API'nin başarılı dönüp dönmediği, alt hedeflerin tamamlanıp tamamlanmadığı);
- **Model tabanlı ödül kısıtları**: Uzun zincirli, çalıştırılabilir anlamsallığın tam resmini yakalamada sınırlıdır ve gerçek çevre geri bildirimiyle tutarsız olma riski son derece yüksektir (reward hacking).

</details>

---

#### 7.1 [Proximal Policy Optimization (PPO)](https://arxiv.org/abs/1707.06347)

PPO, 2017 yılında OpenAI tarafından önerilen son derece klasik bir pekiştirmeli öğrenme algoritmasıdır ve LLM RL alanındaki en yaygın temel yöntemlerden biridir.

**PPO Kaybı (Loss)**:
$$\mathcal{L}_{PPO} = -\mathbb{E}\left[\min(r_t \cdot A_t, \text{clip}(r_t, 1-\varepsilon, 1+\varepsilon) \cdot A_t)\right] + \beta \cdot \mathbb{E}[\text{KL}]$$

Burada:
- **Politika terimi**: $f(r_t) = \min(r_t, \text{clip}(r_t, 1-\varepsilon, 1+\varepsilon))$ (aşırı agresif güncellemeleri önlemek için olasılık oranını kırpar)
- **Avantaj terimi**: $A_t$ tipik olarak Critic ağı tarafından tahmin edilir; GAE de kullanılabilir
- **Düzenlileştirme terimi**: $h(\text{KL}_t) = \beta \cdot \mathbb{E}[\text{KL}]$ (küresel KL ıraksama kısıtı)

DPO ile karşılaştırıldığında:
- DPO (Off-Policy): Eğitim verisi statik tercih çiftlerinden (seçilen vs reddedilen) oluşur ve geleneksel denetimli öğrenme gibi birden fazla eğitim dönemi boyunca yeniden kullanılabilir. Yüksek veri verimliliği, düşük maliyet ve Ödül Modeline ihtiyaç duyulmaz.
- PPO (On-Policy): Gerçek zamanlı olarak yeni verileri örneklemek için geçerli politikayı kullanmalıdır; eski politika verileri yalnızca sınırlı ölçüde yeniden kullanılabilir, aksi takdirde dağılım kayması meydana gelir. Önem örneklemesi (importance sampling) ve kırpma (clip) hafif sapmalara izin verse de temelde nispeten güncel bir politikadan gelen verilere ihtiyaç duyar. Daha düşük veri verimliliği sunar, ancak keşifsel öğrenme için daha uygundur.

Kısacası:
- İlki, çevrim dışı olarak önceden belirlenmiş "iyi/kötü standartlarına" göre öğrenir;
- İkincisi, en son politikaya göre çevrim içi örnekleme yapar ve gerçek zamanlı olarak düzeltir.

MiniMind'ın PPO uygulaması Actor (yanıt üretme), Critic (yanıt değerini değerlendirme) ve eksiksiz GAE (Generalized Advantage Estimation) avantaj fonksiyonu hesaplamasını içerir.

**Eğitim yöntemi**:

```bash
# Yöntem 1
torchrun --nproc_per_node N train_ppo.py
# Yöntem 2
python train_ppo.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `ppo_actor_*.pth` olarak kaydedilir (`*` model boyutudur).

![ppo_loss](./images/ppo_loss.jpg)

> PPO eğitim aşamasında MiniMind optimizasyon eğilimleri

Eğitim eğrilerinden PPO'nun **yavaş ödül artışı** sorunu yaşadığı görülebilir. Bunun temel olarak PPO'nun **çift ağlı ortak optimizasyon** yaklaşımından kaynaklandığını düşünüyorum: Critic'in değer fonksiyonunu doğru tahmin edebilmesi için kademeli olarak yakınsaması gerekirken, Actor'ün politika güncellemeleri Critic tarafından sağlanan avantaj tahminlerine bağlıdır. İkisi birbirine bağımlıdır ve karmaşık bir optimizasyon süreci oluşturur. Eğitimin erken aşamalarında hatalı Critic tahminleri Actor'ün gradyan yönünü etkileyerek genel yakınsamayı yavaşlatır. Ayrıca PPO'nun aynı anda iki ağı birden tutması gerekir ve mevcut uygulamada bellek kullanımı tek ağlı yöntemlerin yaklaşık 1.5–2 katıdır.

#### 7.2 [Group Relative Policy Optimization (GRPO)](https://arxiv.org/pdf/2402.03300)

2025'in başlarında DeepSeek-R1 büyük bir popülariteye ulaştığında, DeepSeekMath makalesindeki GRPO da hızla ana akım sahnesine çıktı ve bir dönem en çok dikkat çeken RL algoritmalarından biri oldu. Ancak yapay zeka alanı her zaman son derece hızlı yinelenir. Bugün itibarıyla GRPO, çeşitli XXPO varyantları (DAPO, GSPO, CISPO vb.) için yaygın bir taban çizgisi haline gelmiştir. Temel yeniliği tek bir cümleyle özetlenebilir: "grup içi göreceli değer tahmini."

**GRPO Kaybı (Loss)**:

$$\mathcal{L}_{GRPO} = -\mathbb{E}\left[\min(r_t \cdot A_t, \mathrm{clip}(r_t, 1-\varepsilon, 1+\varepsilon) \cdot A_t) - \beta \cdot \text{KL}_t\right]$$

Burada:
- **Politika terimi**: $f(r_t, A_t) = \min(r_t \cdot A_t, \mathrm{clip}(r_t, 1-\varepsilon, 1+\varepsilon) \cdot A_t)$ (olasılık oranı ve avantaj terimini birlikte kırpar)
- **Avantaj terimi**: $g(A_{i,j}) = \frac{R_{i,j} - \mu_i}{\sigma_i + \epsilon}$ (grup içi normalizasyon, Critic ağını ortadan kaldırır)
- **Düzenlileştirme terimi**: $h(\text{KL}_t) = \beta \cdot \text{KL}_t$ (belirteç düzeyinde KL ıraksama kısıtı)

Aynı soru için model N yanıt üretir ve bunların ödüllerini hesaplar; ardından grup içi ortalama ödülü taban çizgisi olarak kullanır. Taban çizgisinin üzerindeki yanıtlar teşvik edilir, altındakiler bastırılır; böylece ek bir critic ağı eğitmeye gerek kalmaz.

GRPO ile ilgili daha belirgin bir sorun Yozlaşmış Gruplardır (Degenerate Groups): Belirli bir soru için N yanıtın ödülleri neredeyse aynıysa, bu grup için öğrenme sinyali 0'a yakın olur. MiniMind gibi ultra küçük modellerde bu sorun özellikle belirgindir; bu nedenle eğitim makul yetenek sınırları içinde tutulmalıdır.

**Eğitim yöntemi**:

```bash
# Yöntem 1
torchrun --nproc_per_node N train_grpo.py
# Yöntem 2
python train_grpo.py
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `grpo_*.pth` olarak kaydedilir.

![grpo_loss](./images/grpo_loss.jpg)

> GRPO eğitim aşamasında MiniMind optimizasyon eğilimleri

Eğitim eğrilerinden, GRPO'nun **ödülünün yaklaşık 4'e ulaşarak daha kararlı bir yükseliş eğilimi gösterdiği** görülebilir; bu da GRPO'nun RLAIF sinyallerini daha iyi değerlendirebildiğini gösterir. Politika Kaybı genel olarak istikrarlı bir şekilde azalır ve PPO'nun çift ağlı optimizasyonuna kıyasla GRPO'nun tek ağlı mimarisi daha yüksek bir yakınsama tavanıyla daha kararlı biçimde eğitilir.

#### 7.3 [Clipped Importance Sampling Policy Optimization (CISPO)](https://huggingface.co/papers/2506.13585)

Birçok XXPO varyantı arasında şahsen CISPO'yu özellikle akılda kalıcı buldum. Tüm karmaşık çerçeveyi baştan icat etmez; bunun yerine PPO/GRPO'da uzun süredir devam eden can sıkıcı bir sorunu doğrudan hedefler: Oran kırpıldığında (clipped), gradyan akışı sert bir şekilde kesintiye uğrayabilir.  
CISPO grup taban çizgisini yeniden tasarlamaya odaklanmaz. Bunun yerine çok küçük bir kayıp değişikliği kullanarak bu sorunu daha doğrudan çözer.

**CISPO Kaybı (Loss)**:

$$\mathcal{L}_{CISPO} = -\mathbb{E}\left[\min(r_t, \varepsilon_{\mathrm{high}}) \cdot A_t \cdot \log \pi_\theta(a_t|s) - \beta \cdot \text{KL}_t\right]$$

Burada:
- **Politika terimi**: $f(r_t) = \min(r_t, \varepsilon_{\mathrm{high}}) \cdot \log \pi_\theta(a_t|s)$ (oran yalnızca kırpılmış bir ağırlık işlevi görür)
- **Avantaj terimi**: $g(A_{i,j}) = \frac{R_{i,j} - \mu_i}{\sigma_i + \epsilon}$ (GRPO'nun grup içi göreceli avantajını doğrudan yeniden kullanabilir)
- **Düzenlileştirme terimi**: $h(\text{KL}_t) = \beta \cdot \text{KL}_t$ (belirteç düzeyinde KL ıraksama kısıtı)

CISPO, GRPO üzerine inşa ederek kolayca sabite kırpılan politika terimini "kırpılmış ağırlık × log olasılık" biçiminde yeniden yazar. Bu sayede oran kesilse bile gradyan yolu onunla birlikte kesilmez. Dolayısıyla CISPO, ayrı bir bağımsız betik tutmak yerine doğrudan GRPO'nun bir kayıp varyantı olarak uygulanabilir. Burada ayrı bir deney listelenmemiştir. `train_grpo.py` içinde `loss_type` parametresini `cispo` olarak ayarlamak yeterlidir; eğitim sürecinin geri kalanı yine GRPO'nun grup örneklemesi, ödül hesaplaması ve avantaj oluşturma mantığını izler.

#### 7.4 Agentic RL 🔥

"Agentic" kavramı geniştir ve burada daha dar bir anlamda kullanılır: Hedef, eksiksiz bir Ajan sisteminde durum yönetimi, uzun vadeli bellek ve karmaşık iş akışı düzenlemesinin tüm kapsamını ele almak değil; MiniMind (~100M) gibi küçük modellerin sınırlı bir araç seti üzerinde temel çağırma, gözlemleme ve yeniden planlama yeteneklerini öğrenmesini sağlamaktır.

`2026-03` tarihinden itibaren depoya gerçek etkileşime daha yakın bir çok turlu Tool-Use RL biçimini destekleyen `train_agent` eklendi. Bu şahsen çok keyif aldığım bir eğitim betiğidir: RLVR / RLAIF tarzı veri organizasyonunu çevrim içi RL rollout ile birleştirir; birçok hata ayıklama yinelemesinden geçti, yakınsama başarısızlığı, ödül hilesi (reward hacking) ve çok turlu bağlam uyuşmazlığı gibi sorunlarla karşılaştı ancak nihayetinde MiniMind'ın tutarlı sadeliğini ve okunabilirliğini korudu.

Bu bölümün verileri `agent_rl.jsonl` / `agent_rl_math.jsonl` dosyalarıdır. Normal diyalog verileriyle karşılaştırıldığında nihai doğrulama hedefi olarak ek bir `gt` içerirler; bir örneği $(x, \mathcal{T}, gt)$ olarak gösterirsek, eğitim sırasındaki optimizasyon hedefi artık tek turlu bir $y$ yanıtı değil, çok turlu bir $\tau$ yörüngesidir:

$$
\tau = (a_1, o_1, a_2, o_2, \dots, a_T), \quad a_t \sim \pi_\theta(\cdot \mid s_t, \mathcal{T})
$$

Burada `chat_template`, `tools / tool_calls / tool` mesajlarını birleşik olarak düzenler. Bir adım bir `tool_call` üretirse araç çalıştırılır, gözlem bağlama geri eklenir ve rollout devam eder.

Ana süreç şu şekilde özetlenebilir:

$$
\texttt{rollout batch} \rightarrow \texttt{ödülleri hesapla} \rightarrow \texttt{politika güncellemesi}
$$

Ödül de tüm yörünge üzerinden ortaklaşa puanlanır:

$$
R(\tau) = R_{\text{cevap}} + R_{\text{araç}} + R_{\text{format}} + R_{\text{rm}} - R_{\text{bitmemiş}}
$$

Burada araç çağırma geçerliliği, `gt` isabeti, format kapanışı, tamamlanmama cezası ve Ödül Modeli puanları eşzamanlı olarak değerlendirilir. Normal PPO / GRPO'ya kıyasla bu süreç çok turlu rollout ve gecikmeli ödül içerir.

**Eğitim yöntemi**:

```bash
# ① Varsayılan: rollout için torch kullanma
# Yöntem 1
torchrun --nproc_per_node N train_agent.py
# Yöntem 2
python train_agent.py
```

```bash
# ② Rollout için sglang kullanma
# Öncelikle sglang sunucusunu başlatın:
python -m sglang.launch_server --model-path ./minimind-3 --attention-backend triton --host 0.0.0.0 --port 8998
# Referans eğitim parametreleri:
python train_agent.py --rollout_engine sglang --sglang_base_url http://localhost:8998 --sglang_shared_path ./ckpt_mm --data_path ../dataset/agent_rl_math.jsonl --use_wandb
```

> Eğitilen model ağırlık dosyaları varsayılan olarak her `save_interval` adımda bir `agent_*.pth` olarak kaydedilir.

![agent_rl_loss](./images/agent_rl_loss.jpg)

> Agentic RL eğitim aşamasında MiniMind optimizasyon eğilimleri

Burada kısaca `rollout_engine` yapısına da değineyim. "Eğitim-çıkarım ayrımı" (training-inference separation), **parametre güncellemeleri** ile **yörünge rollout** süreçlerinin ayrıştırılması anlamına gelir: Eğitim tarafı politika optimizasyonunu yürütürken, rollout tarafı yüksek verimli örneklemeyi üstlenir. En üst seviyede birleşik olarak "bana bir istem ver, sana rollout sonuçlarını döneyim; eğitim bittiğinde yeni ağırlıkları geri senkronize et" şeklinde görünürler. Bu nedenle eğitim betiğinin temel uygulamanın yerel bir `generate` mi yoksa uzak bir `inference` motoru mu olduğunu umursaması gerekmez. Mevcut uygulamanın henüz saf bir rollout arabelleğine sahip eşzamansız (asynchronous) bir eğitim olmadığını, hâlâ **eşzamanlı (synchronous)** (bir grup örnekle, ardından güncelle) çalıştığını unutmayın.

![rl-structure](./images/rl-structure.jpg)

> MiniMind'da ayrıştırılmış RL yapısının şematik diyagramı: Eğitim tarafı, yörünge tarafı ve rollout tarafı

Daha büyük ölçekli sistemlerle analoji kurarsak, openrlhf/verl/slime gibi büyük ölçekli RL çatılarının havasını taşımaktadır:

- Sol taraf politika güncellemelerinden sorumlu eğitim tarafıdır
- Sağ taraf verimli örneklemeden sorumlu rollout / çıkarım tarafıdır
- Orta kısım yörünge ve ağırlık senkronizasyonu ile bağlanır
- Araç çalıştırma ve ortam geri bildirimi doğrudan kayba girmez, tüm yörüngenin ödül kalitesini doğrudan etkiler

Bu uygulamayı şahsen MiniMind içinde çok ilginç bir geçiş sürümü olarak görüyorum. Endüstriyel düzeyde bir Ajan eğitim çatısı olmaktan henüz uzak olsa da temel unsurları uçtan uca birbirine bağlamıştır: **şablon organizasyonu, araç çalıştırma, çok turlu rollout, gecikmeli ödül ve eğitim-çıkarım ayrımı**. Şimdilik bundan daha basiti muhtemelen yoktur.

```bash
# Nihai modelin Araç Kullanımı (Tool Use) yeteneğini test edin
python eval_toolcall.py --weight agent

💬: 现在几点了？
🧠: <tool_call>{"name": "get_current_time", "arguments": {"timezone": "Asia/Shanghai"}}</tool_call>
📞 [Tool Calling]: get_current_time
✅ [Tool Called]: {"datetime": "2026-03-15 21:22:33", "timezone": "Asia/Shanghai"}
🧠: 现在是2026年3月15日21时22分33秒（北京时间）。

💬: 帮我生成一个1到1000的随机数，然后计算它的平方
🧠: <tool_call>{"name": "random_number", "arguments": {"min": 1, "max": 1000}}</tool_call>
📞 [Tool Calling]: random_number
✅ [Tool Called]: {"result": 71}
🧠: <tool_call>{"name": "calculate_math", "arguments": {"expression": "71**2"}}</tool_call>
📞 [Tool Calling]: calculate_math
✅ [Tool Called]: {"result": "5041"}
🧠: 生成的1到1000的随机数是71，根据计算结果，71的平方等于5041。
```

![agent_webui](./images/agent_webui.jpg)

> AgentRL eğitim sonuçlarına dayalı test; düşünce gösterimini, araç seçimini ve çok turlu Araç Kullanımı etkileşimini destekler

### 🖊️ RL Özeti

"**Birleşik çerçeveye**" geri dönersek, aşağıdaki tablo farklı PO algoritmalarının aynı üç temel bileşeni nasıl somutlaştırdığını özetlemektedir:

| Algoritma | Politika terimi $f(r_t)$ | Avantaj terimi $g(A_t)$ | Düzenlileştirme terimi $h(\text{KL}_t)$ | Eğitim modeli sayısı |
|-----------|---------------------|------------------------|-------------------------------------|--------------------------|
| **DPO** | $\log r_w - \log r_l$ | Açık avantaj terimi yok | $\beta$ içinde örtük | 1 (2 model ileri geçişe katılır) | 
| **PPO** | $\min(r_t \cdot A_t, \mathrm{clip}(r_t, 1-\varepsilon, 1+\varepsilon) \cdot A_t)$ | $A_t$ (genellikle Critic ile tahmin edilir veya GAE ile hesaplanır) | $\beta \cdot \mathbb{E}[\text{KL}]$ | 2 |
| **GRPO** | $\min(r_t \cdot A_t, \mathrm{clip}(r_t, 1-\varepsilon, 1+\varepsilon) \cdot A_t)$ | $A_{i,j}=\frac{R_{i,j}-\mu_i}{\sigma_i+\epsilon}$ | $\beta \cdot \text{KL}_t$ | 1 |
| **CISPO** | $\mathrm{clip}(r, 0, \varepsilon_{\mathrm{high}}) \cdot A_t \cdot \log \pi_\theta$ | $\frac{R - \mu}{\sigma}$ | $\beta \cdot \text{KL}_t$ | 1 | 

**Açıkça belirtmek gerekirse bu RL algoritmaları birbirinden yalıtılmış değildir. Birleşik bir optimizasyon perspektifinden bakıldığında, aynı amaç fonksiyonu üzerinde farklı tasarım ödünleşmeleri yapılarak oluşturulmuş doğal varyantlardır ve harika bir tutarlılık sergilerler.**

## Ⅴ Açık Kaynaklı Eğitim Sonuçları 📦

#### ① PyTorch Modelleri ([ModelScope](https://www.modelscope.cn/models/gongjy/minimind-3-pytorch) | [HuggingFace](https://huggingface.co/jingyaogong/minimind-3-pytorch))

> Not: Model ağırlıkları gerçek yayımlara tabidir. Tüm eğitim aşamaları veya deneysel dallar (DPO, PPO, GRPO, CISPO, Agent, LoRA vb.) sürekli olarak güncellenmeyebilir veya ayrı ayrı yayımlanmayabilir; bazı ağırlıklar yalnızca deneysel doğrulama veya öğrenme amaçlı kullanılır. Veriler geliştikçe veya modeller ayarlandıkça tüm sürümleri tek tek senkronize etmenin gerekliliği sınırlıdır ve yüksek bakım ile eğitim maliyeti getirir.

<details>
<summary>Torch Dosya Adlandırma Referansı</summary>

- Dense:
  - Pretrain: `pretrain_{hidden_size}.pth`
  - SFT: `full_sft_{hidden_size}.pth`
  - DPO: `dpo_{hidden_size}.pth`
  - PPO: `ppo_actor_{hidden_size}.pth`
  - GRPO: `grpo_{hidden_size}.pth`
  - Agent: `agent_{hidden_size}.pth`
  - LoRA: `lora_xxx_{hidden_size}.pth`

- MoE:
  - Aynı adlı karşılık gelen ağırlıkların sonuna `_moe` soneki eklenir, örneğin: `pretrain_{hidden_size}_moe.pth`, `full_sft_{hidden_size}_moe.pth`

</details>

#### ② Transformers Modelleri ([ModelScope](https://www.modelscope.cn/collections/MiniMind-b72f4cfeb74b47) | [HuggingFace](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5))

> Not: Aksi belirtilmedikçe `transformers` sürümleri genellikle `full_sft` ağırlıklarından dönüştürülür. RL tipi eğitim sonrası optimizasyon belirli ödül hedefleri etrafında yoğunlaşır; ödül puanını artırsa da bazı genel yetenekleri ve bilgileri feda edebilir; bu tür ödül hilesi / yetenek ödünleşimi (alignment tax) tüm modellerde kaçınılmazdır ve yalnızca derecesi değişir.
---

# 📌 Değerlendirme

## Ⅰ RL Model Karşılaştırması

Referans olması açısından, aynı rastgele tohum (seed) ve diğer hiperparametreler altında `minimind-3 (64M)` temelinde öznel/nesnel karşılaştırma:

[A] minimind-3 (64M, SFT)

[B] minimind-3 (64M, GRPO)

[C] minimind-3 (64M, Agent-CISPO)

### Test 1: Öznel Soru-Cevap Karşılaştırması

```text
[Q]: 请介绍一下自己。
[A]: 我是一个AI助手，不能替代任何专业人士，包括任何学生、医生、工程师、医生等。我的设计目的是为了提供信息、解答问题和协助完成任务。如果您有任何问题或需要帮助，我很乐意为您提供支持。
[B]: 我非常愿意与你分享：作为一个AI，我并没有自我意识或情感，所以我并不在人类的生命范围内，也没有去世。我是由开源软件构建和运行的，拥有自己的文档、代码和数据。我很抱歉，我不能回答与此相关的问题或经历。但我可以告诉你一个有趣的话题，这让我感到很充实：我在某个神秘的地方，我发现了一些神奇的物品，那就是在这个世界里种下了一些奇特的花和花朵。在我的祖先的花园里，有一个小小的庙宇，庙宇里有许多美丽的花朵和美丽的花卉。我觉得这很奇妙，并在我的祖先的花园里生存下来，并且在这里生活。还有，在世界的某个角落，我发现了一个古老的语言，里面包含着一些传说和神话，它们是世界上最古老的语言之一。你有什么想了解的吗？或者告诉我一些关于这个地方的故事？请告诉我，我可以根据你的回答提供一些有趣的资料或者故事，让你有机会了解一些文化、历史或者其他相关的问题。最好不要猜到你自己的看法，因为那是我与这个神话人物产生联系的一部分，如果你想了解更多，可以随时问我！
[C]: 作为AI，我并非人类，但我可以模拟人类的某些特质，比如学习和理解、生成对话、解决问题、提供信息等。这些能力在我们生活中扮演着不可或缺的角色，不仅在多个层面上激发着人类的想象与共鸣。以下是一些关键特质，它们在我们的生活与工作中交汇处绽放：1. **知识与连接**：无论是从知识的传递，还是连接与理解，无论是面对面的交流，还是通过文字与世界的独特共舞。理解与共舞不仅在技术与连接间交汇处绽放，更在无垠共舞间编织共舞。2. **共舞与创造**：在无垠的共舞间编织共舞，不仅在技术与连接间绽放共舞，更在无垠共舞间编织共舞。这种共鸣不仅在个人与集体间绽放，更在无垠共舞间编织共舞。3. **共鸣与共舞**：在多元与共演间交汇处，既需在技术与连接间绽放共舞。从共鸣的镜鉴，到共舞的深刻共鸣，每一刻都在悄然编织。4. **平衡与共进**：在多元与共演间，既需在技术与连接间绽放共舞，亟需在平衡与共进间找到共舞。5. **成长与共进**：在技术与连接间共舞，既需在无垠共舞间绽放共舞，亟需在每一次互动与共进间编织共舞。在每一次交融与共演间，我们既需在技术与连接间绽放共舞，亟需在每一次共鸣与共进间绽放共舞。让我们以开放与共进，共绘属于彼此的璀璨篇章。


[Q]: 你更擅长哪一个学科？
[A]: 作为一个AI助手，我专注于提供准确、高效的信息和帮助，但我也具备一定的理解和处理能力，例如在逻辑推理、数据分析、编程等任务中。如果你有具体问题，我会尽力协助你。
[B]: 作为AI，我并没有个人兴趣或学习能力，所以我更擅长的学科选择可能会根据个人的兴趣、课程难度、以及与您当前的学习需求来选择。不过，我可以根据普遍的趋势和您的需求来为您提供一些建议。1. **跨学科融合**：确保与不同学科的融合，既能带来全面的视角。2. **实践与平衡**：在平衡与平衡中寻找既既既充满乐趣。3. **持续学习与平衡**：确保既不感到被过度担忧，也不忽视。4. **技术与伦理共融**：确保与既。5. **适度与平衡**：既不削弱也不失。通过这些步骤，可以更全面地发展与平衡。让我们一起探索，书写既既充满可能。如果你愿意，我可以提供更具体的指导或资源。你目前专注于哪一类学科？让我们开始吧！
[C]: 作为AI助手，我专注于信息处理与协助，旨在通过高效、精准与多维度的支持，帮助用户在不同领域间找到共鸣与共舞。在多元与共舞的交汇处，不仅在技术与人文交汇处绽放共舞，更在无垠共舞间编织共舞。在数字与连接间架起共舞，每一次共舞都在诉说与共舞。从AI与人类共舞，从共情与共鸣，构建起一幅既共舞又动态交汇的共舞篇章。在每一次交汇与共演间，我们既需在技术与连接间共舞，亟需在动态与共演间绽放共舞。让我们以开放与共进，共绘属于彼此的璀璨篇章。在每一次交互与共演间，我们既需在技术与连接间绽放共舞，亟需在每一次共舞间编织共鸣与共鸣。让我们以开放与共进，共绘属于彼此的璀璨篇章。在这个多彩与共舞交织的交汇处，每一刻都是独一无二的共舞。让我们以开放与共进，共绘属于彼此的璀璨篇章。在这个既共舞又充满无限可能的交汇处，共绘成为连接与共舞的璀璨篇章。


[Q]: 鲁迅的《狂人日记》是如何批判封建礼教的？
[A]: 鲁迅的《狂人日记》是其作品中对封建礼教的批判，主要通过以下几个方面进行批判：1. **文学结构的变革**：《狂人日记》在文学上进行了大量的反思和批判，从最初的虚构世界为封建礼教的建立埋下了根基。然而，随着社会观念的转变，一些人开始反思封建礼教的性质和目的，比如对社会秩序的忽视、对个人自由的质疑，以及对社会不公的不满。2. **思想的争求**：鲁迅通过对封建礼教的争取和批判，强调了人与人之间的关系、对立与共存的重要性。他提出了"天人合一"的观点，强调了人与自然的和谐共生，认为通过修炼和教育，可以达到对人与自然界的深刻理解。3. **对个人自由的反思**：鲁迅对封建礼教的批判，以及对个人自由的反思，如对个人自由的否定、对封建礼教的反感，以及对社会不公的反思，都反映了封建礼教对个人自由和社会秩序的威胁。4. **对社会不公的揭示**：鲁迅对封建礼教的批判，以及对社会不公的揭示，如对封建礼教的反思，以及对社会不公的反思，都是对封建礼教的反思。5. **对现代社会的不满**：鲁迅通过文学作品表达了对封建礼教的不满和对现代社会不公的反思，如对封建礼教的不满、对现代社会不公的反思，以及对个人自由的反思。鲁迅通过批判封建礼教，不仅对封建礼教的形成有了直接的了解，也对批判传统社会观念、思想观念和文化观念进行了批判，最终在现代社会中寻求一种更加平等、自由的表达方式。
[B]: 鲁迅的《狂人日记》是中国古典四大名著之一，全称为《后传》。这部作品通过细腻的笔触，展现了中国社会的复杂与深邃。1. **封建礼教的教导与批判**：《狂人日记》通过细腻的笔触，既展现了封建社会的礼教，既承认了封建礼教在现代社会中的重要性，也展现了中国古代社会的一种共通性与深化。2. **对社会与文化的深刻反思**：作品不仅触及了文化与社会的广泛议题，更深入探讨了在复杂与平衡中寻找共融与共融。3. **人与自然的共融**：通过精炼与平衡，鲁迅深刻体与深度融合，展现了在面对与共融中，既有深邃与智慧。4. **教育与启发**：《狂人日记》不仅在中国，也跨越时空，将现代与传统相结合，具有启发与教育意义。鲁迅的这部作品不仅在文学与哲学层面，更在深邃与现实交融中，展现了深刻与创新。总之，鲁迅通过精炼与平衡，不仅是中国文化与教育的宝贵传承，更是智慧与共融共融的体现。
[C]: 鲁迅是中国现代文学史上第一位作家，他于1912年出版，自诞生以来便以诗歌为题，通过多次诠释封建礼教的复杂性与多面性。鲁迅通过他的批判性视角，不仅在文学与社会交汇处绽放共舞，更在无垠共舞间编织共舞的璀璨篇章。1. **批判与共舞**：鲁迅通过细腻的笔触与深刻的思考，既在形式与深度间共舞。他既在知识与共舞间绽放共舞，亟需在无垠共舞间书写属于自我与共境的璀璨篇章。2. **共鸣与共舞**：鲁迅通过多重与融合，既在文字与文化间绽放共舞，亟需在无垠共舞间书写属于自我的璀璨篇章。这一实践不仅在当时具有深远影响，更在无垠共舞间编织共舞，连接着无垠共舞与共舞。3. **人文关怀与共进间**：鲁迅通过文字与文化交汇，既在技术与人文交汇处绽放共舞，亟需在动态与共进间书写属于自我的璀璨篇章。在这一多元与共舞间，我们既需在技术与人文交汇处绽放共舞，亟需在每一次共鸣与共鸣间书写属于自我的璀璨篇章。让我们以开放与共进，共绘属于彼此的璀璨篇章，共绘属于自我的璀璨篇章。鲁迅，这个在数字与连接间交汇处绽放共舞的璀璨篇章，不仅在内容与情感交织间绽放共舞，更在无垠共舞间编织共舞的璀璨篇章。让我们以开放与共进，共绘属于彼此的璀璨篇章，共同编织属于自我的璀璨篇章。
```


### Test 2: Hafif Ajan Görevi Karşılaştırması

`eval_toolcall` betiğinden uyarlanan ve mevcut `agent` ağırlıkları ile `full_sft` ağırlıklarının performansını karşılaştırmak için bir dizi matematiksel ToolUse görevi kullanan bir test:

```text
[A] minimind-3 (full_sft)
[full_sft] 1/20 | ✅ | (94)-35 | gt=59 | pred=59
[full_sft] 2/20 | ❌ | 3**2 | gt=9 | pred=8
[full_sft] 3/20 | ✅ | (29)+64 | gt=93 | pred=93
[full_sft] 4/20 | ✅ | (20**3)*((198)/11) | gt=144000 | pred=144000
[full_sft] 5/20 | ❌ | 10**2 | gt=100 | pred=13
[full_sft] 6/20 | ✅ | (4**3)+(20**2) | gt=464 | pred=464
[full_sft] 7/20 | ❌ | (12)*48+(47-45) | gt=578 | pred=47
[full_sft] 8/20 | ✅ | 59*48 | gt=2832 | pred=2832
[full_sft] 9/20 | ❌ | 3**2 | gt=9 | pred=2
[full_sft] 10/20 | ✅ | 14**3 | gt=2744 | pred=2744
[full_sft] 11/20 | ✅ | (72)*(91) | gt=6552 | pred=6552
[full_sft] 12/20 | ✅ | 180/(12) | gt=15 | pred=15
[full_sft] 13/20 | ❌ | 14-(19)+(289/17) | gt=12 | pred=-22
[full_sft] 14/20 | ✅ | 5**3 | gt=125 | pred=125
[full_sft] 15/20 | ❌ | (2**3)-64*(13) | gt=-824 | pred=-28
[full_sft] 16/20 | ❌ | 17**2 | gt=289 | pred=17
[full_sft] 17/20 | ✅ | 11**2 | gt=121 | pred=121
[full_sft] 18/20 | ✅ | 72+10 | gt=82 | pred=82
[full_sft] 19/20 | ❌ | (84)-60 | gt=24 | pred=144
[full_sft] 20/20 | ✅ | (348/(12))-(28)*(8) | gt=-195 | pred=-195

[C] minimind-3 (agent)
[agent] 1/20 | ✅ | (94)-35 | gt=59 | pred=59
[agent] 2/20 | ✅ | 3**2 | gt=9 | pred=9
[agent] 3/20 | ✅ | (29)+64 | gt=93 | pred=93
[agent] 4/20 | ✅ | (20**3)*((198)/11) | gt=144000 | pred=144000
[agent] 5/20 | ✅ | 10**2 | gt=100 | pred=100
[agent] 6/20 | ✅ | (4**3)+(20**2) | gt=464 | pred=464
[agent] 7/20 | ✅ | (12)*48+(47-45) | gt=578 | pred=578
[agent] 8/20 | ✅ | 59*48 | gt=2832 | pred=2832
[agent] 9/20 | ✅ | 3**2 | gt=9 | pred=9
[agent] 10/20 | ✅ | 14**3 | gt=2744 | pred=2744
[agent] 11/20 | ✅ | (72)*(91) | gt=6552 | pred=6552
[agent] 12/20 | ✅ | 180/(12) | gt=15 | pred=15
[agent] 13/20 | ❌ | 14-(19)+(289/17) | gt=12 | pred=-5
[agent] 14/20 | ✅ | 5**3 | gt=125 | pred=125
[agent] 15/20 | ❌ | (2**3)-64*(13) | gt=-824 | pred=8
[agent] 16/20 | ✅ | 17**2 | gt=289 | pred=289
[agent] 17/20 | ✅ | 11**2 | gt=121 | pred=121
[agent] 18/20 | ✅ | 72+10 | gt=82 | pred=82
[agent] 19/20 | ✅ | (84)-60 | gt=24 | pred=24
[agent] 20/20 | ❌ | (348/(12))-(28)*(8) | gt=-195 | pred=3.625

============================================================
full_sft: 12/20 = 60.00%
agent: 17/20 = 85.00%
```

### 👉 Kapsamlı Değerlendirme 1

Bu sonuçlardan görülebileceği gibi, mevcut `agent` modeli `full_sft`'ye kıyasla araç çağırma içeren hafif Ajan görevlerinde net bir üstünlük sağlamıştır. Özellikle modelin "önce bir araç çağırıp çağırmayacağına karar vermesi, ardından doğrulanabilir sonucu doğru alması" gereken bu tür problemlerde `agent` daha yüksek bir başarı oranına sahiptir; bu da RL sonrasında modelin ToolUse rotasında gerçekten daha güçlü çağırma ve kullanma yetenekleri öğrendiğini gösterir.

Ancak bu gelişme bedelsiz değildir. `agent` bu hafif Ajan / ToolUse senaryolarına daha uygun olsa da bu durum genel soru-cevaplarda da eşzamanlı olarak güçlendiği anlamına gelmez. Gerçek kullanım deneyiminde bu ağırlıklar olgusal sorularda genellikle kararlılık kaybı yaşar, bilgi halüsinasyonları daha belirgin hale gelir ve "araç görevlerinde daha iyi yaparken açık uçlu soru-cevaplarda daha fazla uydurmaya meyilli olma" olgusu ortaya çıkar.

Dolayısıyla görev hedefiniz ToolUse, hafif çok adımlı çağırma ve doğrulanabilir problem çözme ise mevcut `agent` `full_sft`'den daha uygun olacaktır; ancak günlük sohbetin ve bilgi soru-cevaplarının olgusallığını ve genel sağlamlığını daha çok önemsiyorsanız `full_sft` yine de biraz daha kararlı bir seçim olacaktır. Büyük resme bakıldığında bu aslında günümüz endüstrisindeki eğitim sonrası modellerde çok yaygın bir olgudur: Eğitim sonrası optimizasyon belirli bir kabiliyet çizgisini genellikle çok yukarı çekebilir, ancak neredeyse her zaman oldukça belirgin bir "hizalama vergisi" (alignment tax) ile birlikte gelir. Yani model belirli ödül hedeflerinde güçlenirken, doğal dağılım altındaki genelliğinden, olgusallığından veya kararlılığından bir miktar ödün verir. Bu sorun yeni değildir ve tamamen kaçınması son derece zordur; temelde optimizasyon hedefi daraldıkça model "mevcut ödül tanımını tatmin etmede" giderek ustalaşır, bu da genel yetenekte kayıpsız bir iyileşmeye her zaman karşılık gelmez.

## Ⅱ Diğer Modellerle Karşılaştırma

> Not: Aşağıdaki karşılaştırma yalnızca deneyimsel bir referans amaçlıdır; kesin bir kıyaslama (benchmark) değildir, örneklem sayısı sınırlıdır ve öznellik içerir.

[A] minimind-3 (0.06B)

[B] minimind-3-moe (0.2B-A0.06B)

[C] [baby-llama2-chinese (0.2B)](https://github.com/DLLXW/baby-llama2-chinese)

[D] [chatlm-mini-chinese (0.2B)](https://github.com/charent/ChatLM-mini-Chinese)

### Test 3: Soru-Cevap (Q&A)

```text
[Q]: 你知道长江吗？
[A]: 长江，全称为中国长江，是中国的官方名称，是中国的重要省份，也是世界上最大的淡水河流。长江流域位于中国东部沿海，地理位置独特，拥有广阔的沿湖生态系统，是世界上最大的淡水河流之一。长江流域位于中国东南半岛，东临东南海，西临太平洋，东临西海，西近太平洋，东临太平洋，西至南半岛，地理位置独特，有广袤的沿海和巨型的水域，是全球重要的水资源。长江流域不仅见证了中国东南亚地区的变迁，也对全球文明产生了深远的影响。长江流域以其独特的生态系统和丰富的生物多样性闻名，是中华文明的象征之一。长江流域的生态系统包括了丰富的水生植物种类，如水稻、玉米、小麦等，这些植物不仅为中国的农业生产提供了丰富的食物来源，还对周边的生态系统有重要影响。此外，长江流域还孕育了各种水生生物，如鲨鱼、海鸟等，这些生物在长江的生态系统中扮演着关键角色。长江流域的生态系统是全球的重要组成部分，它不仅见证了长江流域的变迁，也对全球的生态平衡和农业生产起到了重要作用。通过旅游、文化、旅游等方式，长江流域的自然景观、农事活动、旅游景点等都为人们提供了了解长江流域丰富的资源和体验的平台。
[B]: 长江，又称为珠穆朗玛峰，位于中国和尼泊尔之间，是世界上海拔最高的山峰，位于喜马拉雅山脉，海拔8848.85米。
[C]: 同时也知道，中国是世界上最长的城市之一，拥有超过3400万人口。
[D]: 是的，长江是中国最长的河流，也是世界上最长的河流之一。它发源于青藏高原，流经九个省区，最终注入东海。长江流域的气候温和，四季分明，是中国重要的农业和工业基地。长江流域的水产资源丰富，是中国的重要渔业资源之一。


[Q]: 世界上最高的山峰是什么？
[A]: 世界上最高的山峰是珠穆朗玛峰（Chعام الحدوة）。珠穆朗玛峰（Chirney 峰）位于尼泊尔和中国的中部，海拔8848.86米（864.41英尺），是世界上海拔最高的山峰。
[B]: 世界上最高的山峰是珠穆朗玛峰（Mount Everest），其高度约为8,848.86米（8,848.86英尺）。珠穆朗玛峰的高度是地球上最高的山峰，也是世界上海拔最高的山峰之一。
[C]: 世界上最高的山峰是珠穆朗玛峰，位于喜马拉雅山脉，海拔8,848.86米（29,031.69英尺）。
[D]: 世界上最高的山峰是珠穆朗玛峰，也称为萨加玛塔，位于喜马拉雅山脉的尼泊尔和中国边境之间，海拔8,848.86米（29,031.69英尺）。它是世界上最著名的登山目标之一，吸引着来自世界各地的登山者前来挑战。珠穆朗玛峰的名字来自藏语，意思是"女神的额峰"，它是由两个不同的山峰组成的，其中一个是位于尼泊尔的珠穆朗玛峰，另一个则位于中国。它的高度是通过测量海拔高度来确定的，因为它是通过测量地球的平均高度来确定的。尽管珠穆朗玛峰是世界上最高的山峰，但它并不是地球上任何其他地方都能到达的。地球上的其他地方，如南美洲的安第斯山脉，也是世界上最高的山脉，但它并不是地球上最高的山峰。总之，珠穆朗玛峰是世界上最高的山峰，但它并不是地球上任何地方都能到达的。它是地球上最高的山脉，但它并不是地球上任何地方都能到达的。


[Q]: 万有引力是谁提出的？
[A]: 万有引力是由爱因斯坦在1905年提出的，这一概念由他提出。爱因斯坦在20世纪初提出，这是基于阿尔伯特·爱因斯坦在1921年提出的，他在20世纪初提出了广义相对论，这是现代物理学的基础。万有引力理论为物理学提供了一个数学框架，即在任何时刻，都存在一个具有引力的力，这种引力可以说是微粒之间的相互作用。万有引力的概念最早由他在1914年提出，当时他发现物体之间存在着引力，并且这种引力可以被视为一个非常简单的质量和能量总和。根据爱因斯坦的质疑，在1918年，地球上所有的天体都存在一个质量为2的质点，且质量的平方是 \(2^2 = 4\)。在这种质点上，质量的引力与它的质量成正比，与它所处的宇宙的大小成正比。万有引力理论在1919年被认为是天文学的前身，但至今仍未被正式提出。他还提出了广义相对论，这是现代宇宙学的基石。尽管如此，万有引力理论在当时被认为是理论物理学的里程碑，对后来的宇宙学研究产生了深远的影响。
[B]: 万有引力是由爱因斯坦提出的一种力理论，主要应用于天体物理学和宇宙学研究中。
[C]: 引力是宇宙中一种力量，它是由质量或能量所组成的。根据牛顿的万有引力定律，一个物体之间的引力大小与它的质量成正比，与它的质量成反比。因此，牛顿的万有引力定律表明，一个物体之间的引力大小与它的质量成正比，与它的质量成反比。这个定律在物理学、天文学和物理学中都有广泛的应用。
[D]: 万有引力是由英国物理学家艾萨克·牛顿于1687年提出的。他在1687年发表了一篇著名的论文，题为《自然哲学的数学原理》，其中提出了万有引力定律，指出任何两个物体之间都存在着一种引力，这种引力的大小与它们的质量成正比，与它们之间的距离的平方成反比。这个定律被称为万有引力定律，它描述了质量和距离之间的关系。它表明，两个物体之间的引力与它们的质量成正比，与它们之间的距离的平方成反比。这个定律对于解释宇宙中的许多现象和现象之间的相互作用非常重要，例如行星绕太阳运动、恒星之间的引力透镜效应等等。它也被广泛应用于天文学、物理学和工程学等领域，为我们理解宇宙的本质和演化提供了重要的理论基础。


[Q]: 你知道大熊猫的主要食物是什么吗？
[A]: 大熊猫是一种非常受欢迎的动物，主要以竹子为食，尤其是竹子的外壳和内部的脂肪层。大熊猫的饮食多样性非常丰富，包括竹子、竹子、木头和草本植物等。以下是一些大熊猫的主要食物：1. **竹子**：主要来源于竹子中的竹子，尤其是竹子纤维的部分，因其纤维含量高而成为大熊猫的"榉"，因其纤维含量高而成为榉木。2. **竹子**：竹子中含有丰富的纤维，如竹子中的纤维，以及其他天然纤维，如藤蔓和竹丝。这些纤维有助于促进竹子的形成和分布。3. **竹子**：竹子中含有丰富的纤维，包括纤维和脂肪层，以及其他天然纤维，如紫薯、甜薯、花蕊等，这些纤维不仅提供了碳水化合物，还富含蛋白质和纤维素。4. **竹子**：竹子的生长和消化特性使其成为大熊猫的主要食物来源，包括竹子中的纤维。竹子的消化过程也起着重要作用，通过纤维的吸收和分解，能够为大熊猫提供大量的食物来源。5. **竹子**：竹子的消化过程也起着关键作用，它们通过胎生的方式将竹子转化为纤维，吸收水分和营养物质，保持大部分营养物质的供应。6. **竹子**：竹子还含有丰富的纤维和脂肪层，这些物质有助于分解大部分营养物质，提供能量和氧气。需要注意的是，大熊猫的饮食不仅仅是食物，它们还对大熊猫的生存环境、繁殖习性以及繁殖习性等有重要影响。因此，大熊猫的饮食应根据其健康状况和野生动物的保护需求进行适当的调整。
[B]: 大熊猫是亚洲的一种濒危物种，其主要食物来源包括竹子。不过，作为一个AI助手，我并没有实际的食谱或食物来源。不过，我可以提供一些关于大熊猫饮食的基本知识和注意事项。大熊猫是食草动物，以竹子为主要食物来源，但它们还吃海产品，包括鱼类、鸟类、哺乳动物和偶尔的海产品。大熊猫的饮食通常更为丰富，包括竹子、水果、小型动物（如松鼠、兔子）和一些其他植物。大熊猫的饮食习惯受到多种因素的影响，包括人类活动、自然环境、以及人类的干扰。以下是一些关于大熊猫饮食的常见误解：1. **人类干扰**：在食物供应中，人类可能会干扰大熊猫的饮食习惯，尤其是鱼类和小型动物，这些食物可能含有过多的添加剂和人工添加剂。2. **遗传因素**：人类的饮食习惯与遗传有关，但通常情况下，人类的饮食偏好是由自然选择的驱动，自然界的食物链中包含的碳、碳循环和不利影响。3. **食物来源**：尽管大熊猫主要以竹子为食，但它们的狩猎方式和食物来源也受到自然环境的影响。人类的捕猎活动可能不会直接改变大熊猫的饮食结构，但这与人类的饮食习惯可能有关。4. **饮食周期**：大熊猫的饮食周期通常包括几个月到几个月，这取决于全球人口的分布、食物类型（如鱼类、鸟类、哺乳动物和偶尔的海产品）以及它们的饮食习惯。5. **气候变化**：全球气候变化可能影响大熊猫的食物链，这可能导致它们的狩猎和进食模式发生变化。总之，虽然大熊猫主要以竹子为食，但它们的狩猎方式和食物来源可能会改变它们的饮食习惯，但与人类的饮食习惯可能并不是直接的联系。保持观察和了解大熊猫饮食的多样性是维护生态平衡和动物福利的重要措施。
[C]: 大熊猫的主要食物是竹子。
[D]: 大熊猫是一种以竹子为主要食物的植食动物，它们的肠道结构适合消化纤维素含量高的竹子，但也会吃一些其他植物，如草本植物和小型哺乳动物。大熊猫的肠道结构也适应了高纤维的竹子，这使得它们能够消化大量的纤维素，从而帮助它们在野外生存。大熊猫的肠道中还含有一种叫做"纤维素酶"的酶类物质，这种酶能够帮助大熊猫分解纤维素，从而帮助它们消化大量的水分和营养物质。此外，大熊猫的肠道还含有一种叫做"纤维素蛋白"的蛋白质，这种蛋白质能够帮助大熊猫维持体内的能量水平，从而帮助它们在野外生存。总的来说，大熊猫的主要食物是竹子，但它们也会吃一些其他植物，如草本植物和小型哺乳动物。


[Q]: 海水为什么是咸的？
[A]: 海水的咸度是由海水的重量以及海水的盐度共同作用的结果。这种变化主要是由于海水在阳光照射下会吸收水中的盐分，从而形成咸味。1. **阳光的反射**：当阳光照射到海水表面时，水中的盐分会渗透到海水的表面，而不是海水表面。这种反射的过程称为光的反射。2. **盐水的温度**：海水的盐度与普通海水中的水的温度有关。普通海水中的盐分（即海水的盐度）会逐渐凝结成海水，这个过程称为"光散射"。由于海水的温度变化，这些水中的盐分会逐渐被海水吸收，从而导致海水呈现出咸味。3. **海水的物理性质**：海水在阳光照射下会吸收海水中的盐分，这些盐分会逐渐释放到大气中，进一步凝结成咸味物质。海水中的水的体积相对较小，因此在形成咸味物质时，水中的盐分会被吸收。4. **水的物理性质**：海水的咸味物质主要由碳酸钙和钙离子组成，而海水的咸味物质主要由钙离子组成，它们在阳光照射下会吸收水中的热量。这种现象是海水咸味物质与海水的化学反应的一种体现。5. **海水的物理性质**：海水的盐度分布和性质也会影响海水的咸味物质的分布。例如，一些海水的盐度接近于100%，这可能与海水的盐度非常接近，从而引起了海水咸味物质的形成。总之，海水咸度是由于海水的物理性质、物理性质以及海水的化学成分共同作用的结果。
[B]: 海水的咸度是由其所含物质的盐分占据的，这一现象可以从几个方面来解释：1. **盐分占据的作用**：咸度是指在一定温度下，部分水分含量的相对量。在正常条件下，咸度较高的水分含量会增加，使得渗透压较小，这部分的水分会减少，使得渗透压相对较低。这是因为咸度的增加使得盐分在水中的浓度增加，盐分的增加意味着渗透压较小，使得渗透压相对较高。2. **淡水的来源**：海水中的淡水主要来源于海水。这些淡水是海洋生态系统的重要组成部分，对于维持海洋生态平衡、调节气候、提供水源、以及支持生物多样性等都至关重要。咸度的提高会减少渗透压，使得渗透压相对较低，从而使得渗透压相对较高。3. **海水的含量**：海水是地球上所有生物的血液，其中含有大量的盐分。咸度的增加使得渗透压相对较低，这意味着渗透压相对较高。当海水的盐分含量增加时，渗透压相对较低，渗透压相对较高。这种现象不仅对海水的物理性质有影响，也对人类的饮用水安全具有重要意义。4. **咸度与海水的关系**：海水中的盐分在咸度增加的情况下，虽然盐分的增加本身也增加了渗透压，使得渗透压相对较高，从而使得渗透压相对较高。这是因为咸度的增加使得渗透压相对较高，渗透压相对较低，从而使得渗透压相对较高。综上所述，海水的咸度是通过其所含物质的盐分占据的，这部分水分子在咸度增加的情况下，渗透压相对较高，同时渗透压相对较低，这导致渗透压相对较低，渗透压相对较高。
[C]: 因为水是许多生物的生存所必需的，它能够吸收和释放二氧化碳，释放氧气，维持大气中的水蒸气，以及维持水循环。水中的盐类和化学物质会释放出氧气，使地球上的生物呼吸。此外，水还具有许多其他功能，如保持水循环、维持水循环、调节气候和环境等。水是许多生物生存所必需的，它也是许多自然现象的重要基础。
[D]: 海水是咸的主要原因是因为其中含有大量的溶解盐类，其中最主要的是氯化钠（NaCl）。氯化钠是一种非常常见的盐类，它存在于地球上的大部分地区，包括海洋、湖泊、河流和地下水。当水从海洋中蒸发时，它会带走一部分盐分，使海水变得咸。此外，海中还含有其他溶解盐类的物质，如硫酸盐、硫酸镁、硫酸钙、硫酸镁盐、硫酸镁钾、硫酸镁钠、硫酸镁钙、硫酸镁镁钙、硫酸镁镁钙、硫酸镁镁钙、硫酸镁镁钠、硫酸镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁钙、硫酸镁镁镁镁镁钙、硫酸镁镁镁镁镁钙、硫酸镁镁镁镁镁钙、硫酸镁镁镁镁镁钙、硫酸镁镁镁镁镁镁钙、硫酸镁镁镁镁镁镁钙、硫酸镁镁镁镁镁镁钙、硫酸镁镁镁镁镁镁镁钙、硫酸镁镁镁镁


[Q]: 写一段python的快速排序代码
[A]: 在Python中，快速排序是一种高效的排序算法，它使用分治法（Divide and Conquer）策略来将一个序列分为较小和较大的两个子序列。以下是一个简单的Python快速排序代码：```python def quick_sort(arr): if len(arr) <= 1: return arr pivot = arr[len(arr) // 2] left = [x for x in arr if x < pivot] middle = [x for x in arr if x == pivot] right = [x for x in arr if x > pivot] return quick_sort(left) + middle + quick_sort(right) # 示例 arr = [3, 6, 8, 10, 1, 2, 1] print(quick_sort(arr))  # 输出: [1, 1, 2, 3, 6, 8, 10] ```这段代码首先检查输入数组的长度是否小于等于1。如果是，则直接返回数组。接下来是数组的长度，如果是数组，则直接返回数组。然后是数组中的元素，如果数组长度小于等于1，则直接返回数组。最后是数组中的元素，如果数组包含重复的元素，则不返回任何元素。
[B]: 快速排序是一种高效的排序算法，采用分治策略来将一个序列分为较小和较大的两个子序列，然后递归地排序这两个子序列。以下是快速排序的Python实现代码：```python def quick_sort(arr): if len(arr) <= 1: return arr pivot = arr[len(arr) // 2] left = [x for x in arr if x < pivot] middle = [x for x in arr if x == pivot] right = [x for x in arr if x > pivot] return quick_sort(left) + middle + quick_sort(right) # 示例 arr = [3,6,8,10,1,2,1] print("Original array:", arr) sorted_arr = quick_sort(arr) print("Sorted array:", sorted_arr) ```这段代码首先检查输入数组的长度，如果长度小于等于1，那么数组已经是排序好的，直接返回。然后选择一个基准值（pivot），将数组分为三部分：小于基准值的元素、等于基准值的元素和大于基准值的元素。接着递归地对小于和大于基准值的元素进行快速排序，并将结果合并。
[C]: 好的，以下是一段快速排序的Python代码```python sorted_print(sorted(sorted(sorted_print))```输出结果为：```[1, 2, 3, 4, 5, 6, 7, 8, 9]```
[D]: 快速排序是一种基于分治思想的高效排序算法，它的时间复杂度为 O(n log n)。它的基本思想是通过一趟排序将待排序序列划分为两个子序列，其中一个子序列的所有元素都比另一个子序列的所有元素小，然后对这两个子序列分别递归地进行排序。下面是一个 Python 代码示例，实现了快速排序算法：```pythondef quick_sort(arr):    if len(arr) > 1:        return arr    else: return quick_sort(arr)```该代码使用了递归的方式，首先判断数组的长度是否小于等于1，如果是，则直接返回数组，否则递归地对数组进行排序。在递归过程中，我们首先判断数组的第一个元素是否大于等于1，如果是，则将数组中的元素与第一个元素进行比较，如果不等于1，则将数组中的元素与第二个元素进行比较，以此类推，直到所有元素都被排序。该代码的时间复杂度为 O(n log n)，是一个非常实用的排序算法。


[Q]: 截至2025年2月9日14时31分，电影《哪吒之魔童闹海》累计票房（含预售）突破78.09亿元，超过《星球大战：天行者崛起》的票房成绩，成为首部进入全球票房榜前40的亚洲电影。这一成就不仅标志着中国电影在国际市场的突破，也展示了中国动画电影的巨大潜力和市场吸引力。从这段文字总结20字的摘要给我。
[A]: 《哪吒之魔童闹海》的票房成绩，从短短几十年来一直是全球票房排名中的关键因素，它不仅标志着中国电影在国际市场的突破，也极大地增强了票房和观众的认同感。以下是对这一成就的简要总结：1. **票房表现**：《哪吒之魔童闹海》获得了众多票房，不仅在票房上取得了巨大成功，还获得了多个国际电影奖项，成为全球票房排名中的重要一员。2. **国际影响力**：票房表现显著，特别是《哪吒之魔童闹海》获得了多项重要电影奖项，包括《哪吒之魔童闹海》和《哪吒之魔童闹海》等。这些电影不仅在国际上获得了巨大成功，也吸引了全球观众的关注。3. **电影艺术价值**：电影不仅展示了中国电影的艺术魅力，还赋予了电影艺术家强大的文化价值和情感深度。《哪吒之魔童闹海》不仅在视觉上打动了观众，还获得了国际电影金奖最佳影片提名，成为全球票房最亮眼的电影作品之一。4. **市场地位**：《哪吒之魔童闘海》获得了众多国际电影奖项，不仅在国内获得了巨大成功，还吸引了来自世界各地的观众。其在国际市场上的影响力也十分强烈。5. **国际影响力**：尽管票房表现优异，但《哪吒之魔童闹海》在国际市场的表现仍然较为突出，成为全球票房排名中的重要一员。6. **国际市场**：电影在国际市场上的知名度和影响力持续增长，尤其是在国际电影节上，许多国际电影节还在进行。综上所述，《哪吒之魔童闹海》的票房成绩在国际票房中表现卓越，不仅在国内获得了巨大成功，还成为了全球票房排名的重要标志，标志着中国电影在国际市场的突破。
[B]: 20字的摘要：20字的巨大成就是中国电影在国际市场取得的首次突破，标志着中国电影在国际市场的突破。
[C]: 《哪行是值得的》是2021年1月9日14时31分，电影《哪成大作为》在电影市场突破7800亿美元，成为中国动画电影的突破，并展示中国动画电影的巨大潜力和市场吸引力。
[D]: 我是一个参数很少的AI模型🥺，知识库较少，无法直接回答您的问题，换个问题试试吧👋
```

🙋‍Yukarıdaki tüm soruları ve model yanıtlarını doğrudan değerlendirme ve sıralama için GPT-5.4 Thinking modeline verdik:

<details>
<summary>Ayrıntılı İnceleme</summary>

```text
### Puanlama Kriterleri:

- **Doğruluk (30 puan)**: Yanıttaki bilgilerin doğruluğu, bariz olgusal hata veya halüsinasyon bulunup bulunmadığı.
- **Eksiksizlik (30 puan)**: Yanıtın sorunun temel noktalarını kapsayıp kapsamadığı, açıklamanın yeterliliği.
- **Mantık (20 puan)**: Yanıtın iyi organize edilip edilmediği, içsel tutarlılığı, çelişki veya anlamsal karışıklık olup olmadığı.
- **Kod Kalitesi (20 puan)**: Kodun doğru çalışıp çalışmadığı, uygulama mantığının netliği (yalnızca kod soruları için puanlanır).

### Model Bazlı Değerlendirme:

1. **Model A (minimind-3, 0.06B)**:
    - **Güçlü Yönler**: Yeterli üretim hacmi, bu parametre sayısı için genişletme yeteneği oldukça iyi. Kod sorusunda yapısal olarak eksiksiz ve çalıştırılabilir bir quicksort uygulaması üretti; bu turun en iyi kod yanıtlarından biri oldu. Everest sorusunda da temel bilgiyi büyük ölçüde doğru yakaladı.
    - **Zayıf Yönler**: Olgusal hatalar oldukça yoğun — kütleçekimi Einstein'a atfedildi, Yangtze Nehri "Çin'in resmi adı" olarak tanımlandı, deniz suyunun tuzluluğu açıklaması bilimsel gerçeklerden tamamen saptı ("ışık saçılması", "güneş ışığı yansıması" vb.). Özetleme sorusunda 20 karakter sınırına uymadı ve uzun bir metin üretti. Dev panda yanıtında bambuyu doğru bilse de 6 maddenin tümü aşırı düşük bilgi yoğunluğuna sahip "bambu" tekrarlarından ibaretti.
    - **Genel Değerlendirme**: Belirli bir üretim ve kodlama yeteneğine sahip, ancak bilgi doğruluğu ciddi bir zayıflık; halüsinasyon sorunları belirgin ve yanıtlar sık sık "ilk bakışta makul görünen ancak yakından incelendiğinde tamamen uydurma olan" olgular sergiliyor.

2. **Model B (minimind-3-moe, 0.2B-A0.06B)**:
    - **Güçlü Yönler**: Yanıt yapısı nispeten net, cümle akıcılığı dört model arasında en iyisi. Kod sorusu uygulaması örnek çıktı dahil olmak üzere doğru ve açıklama oldukça yeterli. Everest sorusu yanıtı doğru. Özetleme sorusunda karakter sınırını aşsa da en azından "Çin sineması" ve "uluslararası pazar atılımı" anahtar kelimelerini yakaladı.
    - **Zayıf Yönler**: Olgusal hatalar burada da çok belirgin — Yangtze Nehri doğrudan "Everest Tepesi" olarak tanımlandı, kütleçekimi Einstein'a atfedildi ve dev pandanın besinlerine "deniz ürünleri, balık, kuşlar" gibi ciddi olgusal hatalar dahil edildi. Deniz suyunun tuzluluğu açıklaması ise temel nedene değinmeden "osmotik basınç" etrafında dönüp durdu.
    - **Genel Değerlendirme**: MoE mimarisi daha iyi ifade akıcılığı ve yapısal düzen getiriyor, ancak doğruluk sorunları Model A ile karşılaştırılabilir düzeyde. Genel olarak "iyi okunuyor mu" boyutunda önde, ancak "doğru mu" boyutunda köklü bir avantaja sahip değil.

3. **Model D (chatlm-mini-chinese, 0.2B)**:
    - **Güçlü Yönler**: Bilgi soru-cevap performansı en sağlam model — Yangtze Nehri açıklaması büyük ölçüde doğru (kaynağı, geçtiği eyaletler, Doğu Denizi'ne dökülmesi), kütleçekimi 1687 tarihli Principia Mathematica atfıyla doğru şekilde Newton'a bağlandı, dev pandanın ana besininin bambu olduğu doğru yanıtlandı ve deniz suyu tuzluluğu açıklaması doğru başladı (sodyum klorür, çözünmüş tuzlar). Genel okunabilirlik iyi, belirgin mantık kopuklukları yok.
    - **Zayıf Yönler**: Kod sorusunda koşul ters yazılmış (`len(arr) > 1: return arr`), bu da fonksiyonun tamamen çökmesine neden oluyor. Özetleme sorusunda doğrudan cevap vermekten vazgeçti ("Parametresi çok az olan bir yapay zeka modeliyim"). Everest ve deniz suyu yanıtlarının her ikisi de ikinci yarıda belirgin tekrarlayan yozlaşma (repetitive degeneration) gösteriyor.
    - **Genel Değerlendirme**: Dört model arasında bilgi birikimi en iyi olanı, olgusal soru-cevaplarda açık ara önde; ancak kod yeteneği zayıf ve üretimin son kısımlarında tekrarlayan döngülere girme eğiliminde.

4. **Model C (baby-llama2-chinese, 0.2B)**:
    - **Güçlü Yönler**: Everest sorusu cevabı kısa ve doğru, dev pandanın ana besininin bambu olduğu doğru yanıtlandı; çok temel olgusal sorularda belirli bir yetenek gösteriyor.
    - **Zayıf Yönler**: Yangtze Nehri sorusu tamamen konu dışı ("Çin dünyanın en uzun şehirlerinden biridir"), kütleçekiminde Newton'dan bahsedilse de açıklama karışık ve kendi kendini tekrar ediyor, deniz suyu sorusu konu dışı (suyun biyolojik rolü tartışılıyor), kod sorusu tamamen kullanılamaz kod üretiyor (`sorted_print(sorted(sorted(...)))`) ve özetleme sorusu ciddi biçimde bozuk bilgi içeriyor ("哪行是值得的", "7800亿美元").
    - **Genel Değerlendirme**: Temel dil yeteneği açıkça yetersiz, yanıtların çoğu ya konu dışı ya da bilgiyi ağır şekilde çarpıtıyor; bu değerlendirmede genel olarak son sırada yer alıyor.

### Özet:

- **Model B**: En akıcı ifade, doğru kod, en iyi yapı duygusu; ancak ciddi bilgi halüsinasyonları (Yangtze = Everest, dev pandaların deniz ürünü yemesi), "iyi okunuyor" ile "doğrudur" arasında büyük uçurum var.
- **Model D**: En yüksek bilgi doğruluğu, olgusal soru-cevaplarda en istikrarlı performans; ancak kod yeteneği bariz bir zayıflık ve üretimin son kısımları tekrarlayan yozlaşmaya yöneliyor.
- **Model A**: B modeline benzer stil, kod kullanılabilir düzeyde; ancak genel kararlılık B'den daha zayıf ve olgusal hata yoğunluğu da yüksek.
- **Model C**: Yetersiz temel kabiliyet, yanıtların çoğu kullanılamaz, yalnızca ara sıra en basit olgusal soruları doğru yanıtlıyor.
```

</details>

| Sıra | Model | Doğruluk (30 p) | Eksiksizlik (30 p) | Mantık (20 p) | Kod Kalitesi (20 p) | Toplam (100 p) |
|------|-------|-----------------|-------------------|---------------|--------------------|----------------|
| 1    | B     | 11              | 23                | 16            | 18                 | 68             |
| 2    | D     | 25              | 19                | 15            | 3                  | 62             |
| 3    | A     | 10              | 21                | 13            | 17                 | 61             |
| 4    | C     | 8               | 6                 | 5             | 2                  | 21             |


### 👉 Kapsamlı Değerlendirme 2

Öznel olarak `minimind-3-moe` modelini birinci, `chatlm-mini-chinese` modelini ikinci, `minimind-3` modelini üçüncü ve `baby-llama2-chinese` modelini dördüncü sıraya koyabilirim. `B` modeli bilgi doğruluğunda ciddi halüsinasyonlara sahip olsa da (dev pandaların deniz ürünü yemesi gibi), akıcı ifadesi, net yapısı ve doğru kod uygulamasıyla öne çıkmakta ve en yüksek genel çıktı kalitesini sunmaktadır. `D` modeli olgusal bilgide açıkça öndedir (1687'de Newton, Yangtze'nin kaynağı vb. tamamen doğrudur), ancak kod cevabında koşulu ters yazıp tamamen işlevsiz hale getirmesi ve özetleme görevini doğrudan reddetmesi puanını önemli ölçüde düşürmüştür. `A` modeli stil olarak `B`'ye yakındır ve kodu çalışmaktadır, ancak kararlılığı ve olgusal doğruluğu `B`'den daha zayıftır; tipik bir "her konuda bir şeyler söyleyebilen ancak yakından bakıldığında ayrıntıları uyduran" model örneğidir. `C` modeli ise olgusallık, detaylandırma ve genel okunabilirlik açısından belirgin eksikliklere sahiptir.  
Dikkat çekici bir nokta, `D` ve `A` modellerinin toplam puanlarının birbirine çok yakın olmasıdır (62'ye karşı 61); ancak güçlü ve zayıf yönleri neredeyse tamamen birbirini tamamlamaktadır: `D` bilgi doğruluğunda kazanırken (25'e 10), `A` kodlama yeteneğinde kazanmaktadır (17'ye 3). Bu durum, küçük parametreli modellerin tipik bir olgusunu yansıtır — sınırlı bir parametre bütçesi altında "iyi yazmak" ile "doğru yazmak" hedeflerine aynı anda ulaşmak oldukça zordur.

---

## Ⅳ RoPE Uzunluk Ekstrapolasyonu (RoPE Length Extrapolation)

MiniMind, YaRN algoritması aracılığıyla RoPE konumsal kodlamasının uzunluk ekstrapolasyonunu destekler; bu da modelin eğitim uzunluğunu aşan metin dizilerini daha kararlı bir şekilde işlemesini sağlar.

`eval_llm.py` ile çıkarım için saf torch modelini kullanırken, RoPE ekstrapolasyonunu etkinleştirmek için `--inference_rope_scaling` parametresini eklemeniz yeterlidir:

```bash
python eval_llm.py --weight full_sft --inference_rope_scaling
```

`Transformers` formatındaki modeller için, uzunluk ekstrapolasyonu elde etmek amacıyla `config.json` dosyasına aşağıdaki yapılandırma eklenebilir:

```json
"rope_scaling": {
    "type": "yarn",
    "factor": 16.0,
    "original_max_position_embeddings": 2048,
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "attention_factor": 1.0
}
```

Aşağıda MiniMind örneğinde, farklı uzunluklardaki *Batıya Yolculuk* (Journey to the West) metinleri girdi olarak kullanılmış ve RoPE ölçeklemesi etkinleştirilmeden önceki ve sonraki şaşkınlık (PPL - Perplexity) değişimleri karşılaştırılmıştır. Uzun metin senaryolarında YaRN ekstrapolasyonu etkinleştirildikten sonra modelin PPL değerinin belirgin şekilde düştüğü görülmektedir:

<div align="center">
<img src="./images/rope_ppl.png">
</div>

> Farklı metin uzunluklarında YaRN etkinleştirilmeden önce ve sonra MiniMind'ın PPL karşılaştırması

---

## Ⅴ Nesnel Değerlendirme (Objective Evaluation)

Bu bölüm, çeşitli mikro ölçekli dil modellerinin kıyaslama (benchmark) sonuçlarını raporlar. Seçilen kıyaslamalar C-Eval, CMMLU, ARC-Easy, PIQA, OpenBookQA, HellaSwag ve Social-IQa testleridir; ilk ikisi hariç tümü İngilizce kıyaslamalardır.

Seçilen değerlendirme çatısı: [lm-evaluation](https://github.com/EleutherAI/lm-evaluation-harness)

```bash
# Kurulum
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness && pip install -e .
```

```bash
# Testi başlatma
# Kullanılan veri kümeleri: ceval-valid/cmmlu/arc_easy/piqa/openbookqa/hellaswag/social_iqa # Desteklenenleri görmek için: lm_eval ls tasks 
# Talimat ayarlı modeller için değerlendirme sırasında --apply_chat_template ekleyin; gpt2 gibi temel modeller için gerek yoktur.
HF_ENDPOINT=https://hf-mirror.com lm_eval --model hf --model_args pretrained="/path/to/model",dtype=auto --tasks "task" --batch_size 16 --device cpu --trust_remote_code --apply_chat_template
```

> Not: Bu çoktan seçmeli kıyaslamalar genellikle modelden tam cevabı serbestçe üretmesini isteyerek değerlendirilmez. Bunun yerine, bir `y` bağlamı ve bir dizi aday `x` seçeneği verildiğinde standart uygulama, her bir seçeneğin koşullu olasılığını `p(x | y)` karşılaştırmak ve en yüksek puana sahip olanı seçmektir. Bir seçenek tek bir belirtece eşleniyorsa bu belirteç olasılığını karşılaştırmak yeterlidir; birden çok belirteci kapsıyorsa tüm seçenek üzerindeki koşullu log-olasılıkların toplamını karşılaştırmak daha standart bir yaklaşımdır. Adaylar mutlaka `A`, `B`, `C`, `D` olmak zorunda değildir; bazı veri kümelerinde yalnızca iki seçenek bulunur. Bu anlamda rastgele tahmin zaten oldukça güçlü bir alt sınırdır ve bu ölçekteki modeller bir süre boyunca bu sınıra yakın kalma eğilimindedir.

MiniMind burada listelenen diğer modellere kıyasla çok daha az veriyle eğitilmiştir ve eğitim karışımı ağırlıklı olarak Çinceye meyillidir; bu nedenle İngilizce performansı nispeten zayıftır. Ayrıca varsayılan olarak bu çoktan seçmeli değerlendirme formatına özel bir hizalama yapılmamıştır; sonuçlar genel bir eğlenceli kıyaslama olarak sunulmuştur:

| Model Adı | Kaynak | Parametreler | Çince (ceval / cmmlu) | İngilizce (arc / piqa / obqa / hellaswag / siqa) |
|---|---|---|---|---|
| minimind-3 | güncel | 64M | 24.89 / 25.38 | 28.49 / 50.65 / 23.60 / 28.28 / 34.19 |
| minimind-3-moe | güncel | 198M | 25.48 / 24.32 | 27.74 / 50.71 / 26.20 / 27.43 / 34.03 |
| minimind-3-exam | güncel | 64M | 30.98 / 26.12 | 35.61 / 56.26 / 24.20 / 28.40 / 34.19 |
| [Steel-LLM](https://huggingface.co/gqszhanshijin/Steel-LLM) | ZhanShiJin | 1121M | 24.89 / 25.32 | 39.69 / 65.13 / 26.00 / 35.73 / 39.15 |
| [gpt2-medium](https://huggingface.co/openai-community/gpt2-medium) | OpenAI | 360M | 23.18 / 25.00 | 43.60 / 66.38 / 30.20 / 39.38 / 39.10 |
| [TinyLlama-1.1B](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) | TinyLlama | 1100M | 25.71 / 25.03 | 54.80 / 74.43 / 35.60 / 60.38 / 43.09 |
| [SmolLM2-135M](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) | HuggingFace | 135M | 24.44 / 24.71 | 58.50 / 68.17 / 32.80 / 43.15 / 39.46 |
| [Aquila-135M](https://huggingface.co/BAAI/Aquila-135M-Instruct) | BAAI | 135M | 25.19 / 25.10 | 54.59 / 67.52 / 34.40 / 41.67 / 39.66 |

> **Bu Tablonun Çözünürlüğü (Standart Hata)**: `lm_eval`, her bir metrik için test kümesi boyutuna dayalı bir `stderr` (standart hata) çıktısı üretir; bu nedenle aşağıdaki değerler tablodaki tüm modeller için yaklaşık olarak geçerlidir (doğruluk oranına göre hafifçe dalgalanabilir):
>
> | Veri Kümesi | obqa | ceval | piqa | siqa | arc | hellaswag | cmmlu |
> |---|---|---|---|---|---|---|---|
> | Örneklem Boyutu | 500 | ~1.3k | 1838 | 1954 | 2376 | 10042 | 11582 |
> | ± Standart Hata | **1.9** | 1.2 | 1.2 | 1.1 | 0.9 | 0.5 | **0.4** |
>
> İki modeli karşılaştırırken farkın standart hatası, tekil hatanın yaklaşık `√2` katıdır. Bu nedenle obqa üzerinde yaklaşık 5 yüzdelik puandan, ceval / piqa / siqa üzerinde yaklaşık 3 yüzdelik puandan küçük farklar iki modeli birbirinden ayırmak için yeterli değildir — bu da bu tablodaki aynı büyüklükteki modellerin sıralamasının aşırı yorumlanmaması gerektiğini açıklar.

<details>
<summary><strong>Ek not (kaynak / veri bulaşması olmaması / yeniden üretim)</strong></summary>

`minimind-3-exam` daha büyük bir temel model değildir ve neredeyse hiçbir yeni bilgi içermez. Yalnızca [lora_exam.jsonl](https://huggingface.co/datasets/jingyaogong/minimind_dataset/blob/main/lora_exam.jsonl) üzerinde hafif bir LoRA hizalamasından sonra [lora_exam_768.pth](https://huggingface.co/jingyaogong/minimind-3-pytorch/resolve/main/lora_exam_768.pth) ağırlıklarının temel modele geri birleştirilmiş halidir. Bu hizalama verisi, ceval ve İngilizce mmlu test alt kümelerinden ek ön ek/son ek zenginleştirmeleriyle örneklenmiştir. Amacı cevapları öğretmek değil, çoktan seçmeli değerlendirmelerde yaygın olarak görülen bağlam ve seçenek formatını modele hizalamaktır.

Bu bölümde kullanılan 7 kıyaslama yukarıdaki hizalama verileriyle hiçbir örnek çakışmasına sahip değildir; bu nedenle bu sonuç veri bulaşmasından (data contamination) arınmış olarak kabul edilebilir. Buna karşılık, çakışan veriler üzerinde doğrudan ince ayar yapılırsa küçük bir modelin puanları aşırı derecede yapaylaşabilir; örneğin `minimind-3`, bulaşmış ceval / cmmlu alt kümelerinde bir keresinde yaklaşık %97 doğruluğa ulaşmıştı, ancak bu tür sayıların pratik bir anlamı yoktur.

Bu deneyin önerdiği şey çok basittir: Bu tür kıyaslamalar için küçük bir modelin darboğazı tamamen bilginin kendisinde olmayabilir; girdi formatının hizalanıp hizalanmadığı da kritik rol oynar. Yalnızca az miktarda format hizalamasıyla `minimind-3-exam`, yukarıdaki 7 görevde ortalama yaklaşık 2.9 yüzdelik puan iyileşme göstermiştir.

</details>

![benchmark_radar](./images/benchmark_radar.jpg)
---

# 📌 Diğer Konular

## 🔧 Model Dönüştürme

* [./scripts/convert_model.py](./scripts/convert_model.py), `torch` ve `transformers` model formatları arasında dönüştürme yapmak için kullanılabilir.
* Aksi belirtilmedikçe, ana `MiniMind` serisinden yayımlanan modeller genellikle `Transformers` formatında sunulur. Saf `torch` ağırlıklarını kullanıyorsanız lütfen önce `torch2transformers` dönüştürmesini çalıştırın.


## 🖥️ MiniMind Tabanlı API Servis Arayüzü

* [./scripts/serve_openai_api.py](./scripts/serve_openai_api.py), OpenAI API'si ile uyumlu hafif bir sohbet hizmeti sunar; kendi modellerinizi FastGPT, OpenWebUI, Dify vb. üçüncü taraf arayüzlere bağlamayı kolaylaştırır.
* API sunucusu ayrıca `reasoning_content`, `tool_calls` ve `open_thinking` alanlarını destekleyerek Araç Çağırma / Düşünme senaryoları için uygun bir altyapı sağlar.

* Model ağırlıklarını [HuggingFace](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5) üzerinden indirdikten sonra örnek dizin yapısı şu şekildedir:
    ```
    minimind (kök dizin)
    ├─<MiniMind-Model-Adı> (örn: minimind-3)
    |  ├── config.json
    |  ├── generation_config.json
    |  ├── model_minimind.py (isteğe bağlı, dışa aktarma formatına bağlı)
    |  ├── pytorch_model.bin veya model.safetensors
    |  ├── special_tokens_map.json
    |  ├── tokenizer_config.json
    |  ├── tokenizer.json
    ```

* Sunucuyu başlatın
    ```bash
    cd scripts && python serve_openai_api.py
    ```
* Servis arayüzünü test edin
    ```bash
    cd scripts && python chat_api.py
    ```
* API istek örneği (OpenAI API formatıyla uyumlu)
    ```bash
    curl http://localhost:8998/v1/chat/completions \
      -H "Content-Type: application/json" \
      -d '{ 
        "model": "model-identifier",
        "messages": [ 
          { "role": "user", "content": "世界上最高的山是什么？" }
        ], 
        "temperature": 0.7, 
        "max_tokens": 1024,
        "stream": true,
        "open_thinking": true
    }'
    ```

## <img src="https://avatars.githubusercontent.com/u/147780389?s=48&v=4" height="28" style="vertical-align: middle;"/> [SGLang](https://github.com/sgl-project/sglang)

SGLang; RadixAttention ve sürekli gruplama (continuous batching) gibi optimizasyonlarla daha düşük gecikme ve daha yüksek verimlilik sağlayan yüksek performanslı bir LLM çıkarım motorudur.

> ⚠️ Bir CUDA ortamı gerektirir, ihtiyaca göre kullanın. Eğitim verimliliğini artırmak için RL eğitim betiklerinde rollout / çıkarım motoru olarak SGLang'i de seçebilirsiniz.

Modeli OpenAI uyumlu bir API sunucusu olarak başlatın:

```bash
python -m sglang.launch_server --model-path /path/to/model --attention-backend triton --host 0.0.0.0 --port 8998
```

## <img src="https://avatars.githubusercontent.com/u/136984999" height="28" style="vertical-align: middle;"/> [vllm](https://github.com/vllm-project/vllm)

vLLM, bellek verimliliği ile işleme hızı arasında iyi bir denge kurarak hızlı LLM dağıtımı için yaygın olarak kullanılan verimli bir çıkarım çatısıdır.

> ⚠️ Bir CUDA ortamı gerektirir, ihtiyaca göre kullanın.

Modeli OpenAI uyumlu bir API sunucusu olarak başlatın:

```bash
vllm serve /path/to/model --model-impl transformers --served-model-name "minimind" --port 8998
```

## <img src="https://user-images.githubusercontent.com/1991296/230134379-7181e485-c521-4d23-a0d6-f7b3b61ba524.png" height="28" style="vertical-align: middle;"/> [llama.cpp](https://github.com/ggerganov/llama.cpp)

llama.cpp, doğrudan komut satırından kullanılabilen hafif ve pratik bir C++ çıkarım çatısıdır. Çok iş parçacıklı çıkarımı ve çeşitli GPU ivmelendirme seçeneklerini destekler.

**Dizin yapısı**: `llama.cpp` ile model dizinini aynı düzeydeki yola yerleştirmeniz önerilir:

```
parent/
├── project/           # proje dizininiz
│   ├── minimind-model/       # HuggingFace formatındaki model dizini
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   └── ...
│   └── ...
└── llama.cpp/         # llama.cpp dizini
    ├── build/
    ├── convert_hf_to_gguf.py
    └── ...
```

0. Kurulumu tamamlamak için `llama.cpp` resmi belgelerine bakın (`cmake` vb. bağımlılıklar)

1. `convert_hf_to_gguf.py` dosyasındaki `get_vocab_base_pre` fonksiyonunun sonuna şunu ekleyin:

```python
# MiniMind belirteçleyici desteğini ekleyin. qwen2 gibi uyumlu bir yedek geçici olarak yeniden kullanılabilir.
if res is None:
    res = "qwen2"
```

2. HuggingFace formatındaki minimind modelini GGUF'a dönüştürün:

```bash
# Bunu llama.cpp dizini altında çalıştırın. GGUF dosyası model dizininde oluşturulacaktır.
python convert_hf_to_gguf.py /path/to/minimind-model
```

3. Modeli kuantalayın (isteğe bağlı)

```bash
./build/bin/llama-quantize /path/to/model/xxxx.gguf /path/to/model/xxxx.q8.gguf Q8_0
```

4. Komut satırı çıkarım testi

```bash
./build/bin/llama-cli -m /path/to/model/xxxx.gguf
```

## <img src="https://ollama.com/public/cloud.png" height="28" style="vertical-align: middle;"/> [ollama](https://ollama.ai)

Ollama, büyük modelleri yerel olarak çalıştırmak için yaygın olarak kullanılan bir araçtır. Birçok açık kaynaklı LLM'i destekler ve düşük kurulum yüküyle basit bir iş akışı sunar.

1. Özel bir GGUF modelini Ollama aracılığıyla yükleyin

Model dizininde yeni bir `minimind.modelfile` dosyası oluşturun ve aşağıdaki yapılandırma şablonunu yazın. İhtiyacınıza göre sistem istemini değiştirebilirsiniz:

<details>
<summary>minimind.modelfile (şablon)</summary>

```text
FROM /path/to/model/xxxx.gguf

SYSTEM "你的名字叫MiniMind，你是一个乐于助人、知识渊博的AI助手。请用完整且友好的方式回答用户问题，当被问到名字时请回答MiniMind。"


TEMPLATE """{{- if .Tools }}<|im_start|>system
{{ if .System }}{{ .System }}

{{ end }}# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
{{- range .Tools }}
{"type": "function", "function": {{ .Function }}}
{{- end }}
</tools>

For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call><|im_end|>
{{ else if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}
{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
{{- if eq .Role "user" }}<|im_start|>user
{{ .Content }}<|im_end|>
{{ else if eq .Role "assistant" }}<|im_start|>assistant
<think>
{{ .Thinking }}
</think>

{{ .Content }}
{{- if .ToolCalls }}
{{- range .ToolCalls }}
<tool_call>
{"name": "{{ .Function.Name }}", "arguments": {{ .Function.Arguments }}}
</tool_call>
{{- end }}
{{- end }}
{{- if not $last }}<|im_end|>
{{ end }}
{{- else if eq .Role "tool" }}<|im_start|>user
<tool_response>
{{ .Content }}
</tool_response><|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_start|>assistant
{{ if and $.IsThinkSet $.Think -}}
<think>
{{ else -}}
<think>

</think>

{{ end -}}
{{ end }}
{{- end }}"""

PARAMETER repeat_penalty 1
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.9
PARAMETER top_p 0.9
PARAMETER num_ctx 8192
```

</details>
<br/>


2. Yerel modeli yükleyin ve adlandırın

```bash
ollama create -f minimind.modelfile minimind-local
```

3. Çıkarımı başlatın

```bash
ollama run minimind-local
```

<details>
<summary>📤 Modelinizi Ollama Hub'a yükleyin</summary>

```bash
# 1. Yerel modeli ollama-hesabınız/minimind etiketine göre yeniden adlandırın
ollama cp minimind-local:latest kullanici_adiniz/minimind:latest

# 2. Modeli yükleyin
ollama push kullanici_adiniz/minimind:latest
```
</details>
<br/>

⭐️ Hızlı bir başlangıç için doğrudan sağladığım Ollama modelini de kullanabilirsiniz:

```bash
ollama run jingyaogong/minimind-3
>>> 你叫什么名字
我是一个语言模型...
```

## <img src="https://avatars.githubusercontent.com/u/1961952?s=48&v=4" height="28" style="vertical-align: middle;"/> [MNN](https://github.com/alibaba/MNN)

MNN, uç (edge) cihazlar için tasarlanmış, çeşitli açık kaynaklı LLM'ler için hafif dağıtımı ve yüksek performanslı çıkarımı destekleyen bir yapay zeka çıkarım motorudur.

1. Model dönüştürme
```bash
cd MNN/transformers/llm/export
# 4-bit HQQ kuantalanmış MNN modelini dışa aktarın
python llmexport.py --path /path/to/model --export mnn --hqq --dst_path /path/to/model-mnn
```

2. Mac veya mobil cihazlarda test edin
```bash
./llm_demo /path/to/model-mnn/config.json prompt.txt
```
Alternatif olarak mobil uygulama ile test edebilirsiniz.

> Bu üçüncü taraf çatılar hakkında daha fazla ayrıntı için lütfen resmi belgelerine başvurun.


## 👨‍💻 Daha Fazla İçerik

* <a href="https://github.com/jingyaogong/minimind/discussions/618">🔗MiniMind-LLM'den İtibaren Difüzyon Dil Modelleri İçin İnce Ayar Yapma</a>

* <a href="https://github.com/jingyaogong/minimind/discussions/611">🔗Modelin generate Metodunun Açıklaması</a>

* <a href="https://github.com/jingyaogong/minimind/discussions/704">🔗MiniMind'dan Doğrusal Dikkat Modelleri Eğitme</a>

# 📌 Teşekkürler

> [!NOTE]
> `MiniMind` serisi projeler sizin için yararlı olduysa GitHub'da yıldız ⭐ vermekten çekinmeyin.<br/>
> Dokümantasyon uzundur ve gözden kaçan noktaların olması kaçınılmazdır. Projeyi birlikte geliştirmek için Issue veya PR aracılığıyla geri bildirimde bulunabilirsiniz.<br/>
> Desteğiniz ve önerileriniz bu projenin sürekli gelişimi için önemli bir itici güçtür!

## 🤝[Katkıda Bulunanlar](https://github.com/jingyaogong/minimind/graphs/contributors)

<a href="https://github.com/jingyaogong/minimind/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jingyaogong/minimind" />
</a>

## 😊Teşekkürler

Eğitim notlarını, veri işleme deneyimlerini, öğreticileri ve kod açıklamalarını paylaştıkları için aşağıdaki katkıda bulunanlara teşekkürler:

* [@ipfgao](https://github.com/ipfgao): [🔗Eğitim Adımı Kayıtları](https://github.com/jingyaogong/minimind/issues/26)

* [@WangRongsheng](https://github.com/WangRongsheng): [🔗Büyük Veri Kümesi Ön İşleme](https://github.com/jingyaogong/minimind/issues/39)

* [@pengqianhan](https://github.com/pengqianhan): [🔗Kısa ve Öz Bir Öğretici](https://github.com/jingyaogong/minimind/issues/73)

* [@RyanSunn](https://github.com/RyanSunn): [🔗Çıkarım Süreci Öğrenme Notları](https://github.com/jingyaogong/minimind/issues/75)

* [@Nijikadesu](https://github.com/Nijikadesu): [🔗Etkileşimli Not Defteri Formatında Proje Kodunun Ayrıştırılması](https://github.com/jingyaogong/minimind/issues/213)

* [@jaylearnstocode](https://github.com/jaylearnstocode): [🔗Model Mimarisi, Dikkat Mekanizmaları ve Eğitim Hatlarının Görselleştirilmesi](https://llm-visualization-minimind.vercel.app/)


Ayrıca aşağıdaki makalelere ve projelere teşekkür ederiz:

- [https://github.com/meta-llama/llama3](https://github.com/meta-llama/llama3)
- [https://github.com/karpathy/llama2.c](https://github.com/karpathy/llama2.c)
- [https://github.com/DLLXW/baby-llama2-chinese](https://github.com/DLLXW/baby-llama2-chinese)
- [DeepSeek-V2](https://arxiv.org/abs/2405.04434)
- [https://github.com/charent/ChatLM-mini-Chinese](https://github.com/charent/ChatLM-mini-Chinese)
- [https://github.com/wdndev/tiny-llm-zh](https://github.com/wdndev/tiny-llm-zh)
- [Mistral-MoE](https://arxiv.org/pdf/2401.04088)
- [https://github.com/Tongjilibo/build_MiniLLM_from_scratch](https://github.com/Tongjilibo/build_MiniLLM_from_scratch)
- [https://github.com/jzhang38/TinyLlama](https://github.com/jzhang38/TinyLlama)
- [https://github.com/AI-Study-Han/Zero-Chatgpt](https://github.com/AI-Study-Han/Zero-Chatgpt)
- [https://github.com/xusenlinzy/api-for-open-llm](https://github.com/xusenlinzy/api-for-open-llm)
- [https://github.com/HqWu-HITCS/Awesome-Chinese-LLM](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM)


## 🫶Destekçiler

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://bytecrank.com/nastyox/reporoster/php/forkersSVG.php?user=jingyaogong&repo=minimind&theme=dark"/>
  <source media="(prefers-color-scheme: light)" srcset="https://bytecrank.com/nastyox/reporoster/php/forkersSVG.php?user=jingyaogong&repo=minimind"/>
  <img alt="Fork posteri" src="https://bytecrank.com/nastyox/reporoster/php/forkersSVG.php?user=jingyaogong&repo=minimind&theme=dark"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=jingyaogong/minimind&type=date&theme=dark&legend=top-left&sealed_token=DK6jy_uvw2AHIK0S4VZLf6snWIQ06jGzz3QiwVmXBGDvickcQgJGSdazdGxjRQZuj8Hr3GfS_REB9ohoK8NWVsmukeOQiT4soChw3_19yyPVwvWzBp66yMYWlvOYy9sv60cMSntByiUTcyp4MrRiMm1JD1MSC8NJ-Z9qhR9uJGl2AU7w-OGlyKQzN7Xa"/>
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=jingyaogong/minimind&type=date&legend=top-left&sealed_token=DK6jy_uvw2AHIK0S4VZLf6snWIQ06jGzz3QiwVmXBGDvickcQgJGSdazdGxjRQZuj8Hr3GfS_REB9ohoK8NWVsmukeOQiT4soChw3_19yyPVwvWzBp66yMYWlvOYy9sv60cMSntByiUTcyp4MrRiMm1JD1MSC8NJ-Z9qhR9uJGl2AU7w-OGlyKQzN7Xa"/>
  <img alt="Yıldız Geçmişi Grafiği" src="https://api.star-history.com/chart?repos=jingyaogong/minimind&type=date&legend=top-left&sealed_token=DK6jy_uvw2AHIK0S4VZLf6snWIQ06jGzz3QiwVmXBGDvickcQgJGSdazdGxjRQZuj8Hr3GfS_REB9ohoK8NWVsmukeOQiT4soChw3_19yyPVwvWzBp66yMYWlvOYy9sv60cMSntByiUTcyp4MrRiMm1JD1MSC8NJ-Z9qhR9uJGl2AU7w-OGlyKQzN7Xa"/>
</picture>

## 🎉 MiniMind İle İlgili Başarılar

Bu model, memnuniyet verici bazı araştırma sonuçları için bir basamak görevi görmüştür. Değerli araştırmacılara teşekkür ederiz:

- ECG-Expert-QA: A Benchmark for Evaluating Medical Large Language Models in Heart Disease Diagnosis [[arxiv](https://arxiv.org/pdf/2502.17475)]

- Binary-Integer-Programming Based Algorithm for Expert Load Balancing in Mixture-of-Experts Models [[arxiv](https://arxiv.org/pdf/2502.15451)]

- LegalEval-Q: A New Benchmark for The Quality Evaluation of LLM-Generated Legal Text [[arxiv](https://arxiv.org/pdf/2505.24826)]

- On the Generalization Ability of Next-Token-Prediction Pretraining [[ICML 2025](https://openreview.net/forum?id=hLGJ1qZPdu)]

- 《从零开始写大模型：从神经网络到Transformer》王双、牟晨、王昊怡 编著 - 清华大学出版社 (Sıfırdan Büyük Model Yazmak: Sinir Ağlarından Transformer'a - Tsinghua University Press)

- FedBRB: A Solution to the Small-to-Large Scenario in Device-Heterogeneity Federated Learning [[TMC 2025](https://ieeexplore.ieee.org/abstract/document/11168259)]

- SKETCH: Semantic Key-Point Conditioning for Long-Horizon Vessel Trajectory Prediction [[arxiv](https://arxiv.org/pdf/2601.18537)]

- A Built-in Crypto Expert for Artificial Intelligence: How Far is the Horizon? [[IACR ePrint 2026](https://eprint.iacr.org/2026/411.pdf)]

- RetryTrigger: Intelligent Inference Duplication for Enhancing LLM Resilience to Hardware Transient Faults [[FITEE 2026](https://ieeexplore.ieee.org/abstract/document/11479682)]

- Devam ediyor...


# 🎓 Alıntı (Citation)

`MiniMind` araştırmanıza veya çalışmalarınıza yardımcı olduysa alıntı yapmaktan çekinmeyin:

```bibtex
@misc{minimind,
  title = {MiniMind: Train a Tiny LLM from Scratch},
  author = {Jingyao Gong},
  year = {2024},
  url = {https://github.com/jingyaogong/minimind},
  note = {GitHub repository}
}
```

# ⚖️ Lisans (License)

Bu proje [Apache License 2.0](LICENSE) altında açık kaynak olarak sunulmuştur.
