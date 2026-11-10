# AI driven Science: fiziksel metalurji formül harness'ı

Güncel bulgular, çalışan işler ve sıradaki adımlar: `STATUS.md`.

Amaç: HEA ve fiziksel metalurjide mekanik özellikler için mevcut formüllerin eksik kaldığı yerleri bulmak ve düzeltme terimi önermek. "Yeni fizik" iddiası ancak aşağıdaki merdivenden geçerse yazılır.

## Döngü

1. `harness/compute.py` ile veri üret (MACE-MP, relaks + elastik sabitler). Her satır kompozisyon, yapı, model, seed ve tarih taşır.
2. `harness/baselines.py` içindeki bilinen formülü (rule of mixtures, Pugh, Cauchy, Varvenne-Curtin) aynı veride çalıştır.
3. `harness/discover.py` yalnız artığı (hedef eksi baseline) açıklamaya çalışır. Sonuç CV hatası, null model ve permütasyon testiyle karşılaştırılır.
4. Her bulgu `claims/claims.jsonl` içine `harness/ledger.py` ile seviye ve kanıt yoluyla yazılır.

Literatür taraması sona bırakılmaz: aday ön kayda girmeden önce valency ile kısa bir öncül iş araması yapılır ve `claims/literature.jsonl` içine yazılır. Bilinen bir sonucun yeniden adlandırılması olan aday düşürülür; L4 yalnız son kontrol olarak kalır. Türetme ajanları (Astra, Opus) `.orchestra/` üzerinden çalışır, rezerv test verisini görmez ve önermeden önce `.orchestra/LESSONS.md` okur.

Aday boşa elenmez. Ön kayıt `ledger.register` ile yapılır ve `harness/power.py` ile ölçülmüş güç ister: hipotez doğruyken gerçekçi gürültüyle geçme olasılığı en az 0.8, hipotez yanlışken en fazla 0.05. Başarısız test `ledger.verdict` ile kapanır ve bağımsız bir denetimden sonra sebebi yazılır: `hypothesis`, `design` veya `numerics`. Yalnız `hypothesis` adayı emekliye ayırır, diğer ikisi adayı `open_candidates()` kuyruğuna geri koyar. Karışım enerjisi veya eğrilik hesaplayan PBE koşularında saf referanslar alaşımla aynı kesmeyi kullanır (`Settings(ecut_elements=...)`).

## Keşif turu (arena)

`scripts/discovery_round.py` bir tur koşar:
1. `harness/anomaly.py` şampiyonun eğitim verisinde nerede yanıldığını yazar.
2. Astra ve Opus bu sorunları, sınırları ve aday biçimini (`candidates/README.md`) alır. Prompt kısa tutulur, nasıl düşünecekleri onlara kalır.
3. Paralel türetirler, sonra birbirlerinin adaylarını eleştirip literatür kontrolü yaparlar.
4. `harness/arena.py` her adayı mühürlü holdout'ta (`data/sealed/`, hedefler karıştırılmış) şampiyona karşı güç, ön kayıt ve test ile değerlendirir.

Şampiyonu geçen aday yeni şampiyon adayı olur, L2 ve üstüne normal merdivenle çıkar.

## İddia merdiveni

| Seviye | Şart |
|---|---|
| L0 | Hipotez. Veri yok. |
| L1 | Hesap yığını kalibre: saf elementlerde deneysel elastik sabitlere karşı hata ölçülmüş (`data/calibration_*.csv`). |
| L2 | ML verisinde artıkta yapı var: düzeltme terimi CV ile baseline'ı geçiyor, permütasyon p < 0.01. |
| L3 | Aynı terim bağımsız veride tutuyor: DFT veya deneysel holdout, farklı kompozisyon ailesi. |
| L4 | Literatür kontrolü yapıldı (valency araması, sorgular ve sonuçlar kayıtlı), terim daha önce önerilmemiş. |

L2 kapısı kodda: en az 40 satır, kütüphane boyutuna göre Bonferroni düzeltmeli permütasyon p, CV kazancı > %10. Veriyi üreten model o özellik ve o kafes için L1'den geçmiş olmalı (fcc B, G için MAE ≤ %15). Mevcut durum: `medium-omat-0` fcc için geçer, hiçbir model bcc shear için geçmez (C44 bias yaklaşık -%45).

Modül artıkları rule of mixtures'a (Voigt, üst sınır) karşı değil, Reuss alt sınırına karşı fit edilir. Voigt'e karşı artık modül uyumsuzluğuyla trivial biçimde ilişkilidir: ilk fcc verisinde r = -0.89 çıktı, Reuss'a karşı -0.17'ye düştü. Hacim için baseline Vegard'dır.

L2 altı hiçbir şey "keşif" diye raporlanmaz. MACE-MP elastik sabitleri sistematik olarak yumuşak tahmin eder; bu sapma L1'de ölçülür ve düzeltme teriminin bu sapmadan kaynaklanmadığı gösterilmeden L3'e çıkılmaz.

## DFT katmanı (L3)

QE 7.6, WSL `Ubuntu-22.04` içinde micromamba env `qe` (sudo gerekmez). Pseudopotansiyel SSSP 1.3.0 PBE efficiency, `~/pseudo/sssp_eff_1.3`, md5 `a58f1b33...`. `harness/dft.py` her pw.x koşusunu `data/dft_runs/<tag>/` altında tutar ve biten koşuyu tekrar çalıştırmaz.

Yakınsama (Nb, `data/dft_convergence_Nb.csv`): `kspacing=0.10`, `ecut_scale=1.25`, MV smearing 0.01 Ry. Daha kaba k ile Nb C44 2 ile 28 GPa arasında oynuyor, bu yüzden 0.10 alt sınırdır.

`harness/validate.py` L3 kapısı: ML verisinde sabitlenen terim ve katsayı, aile örtüşmesi olmayan en az 15 DFT satırında, yalnız kesişimli düzeltmeye göre %10'dan fazla kazanç sağlamalı. DFT'de yeniden fit edilen katsayının %95 güven aralığı sıfırı dışlamalı ve eğitim katsayısının 0.5 ile 2 katı arasında olmalı. Defter, L2 ve üstündeki her kaydın bir alt seviyede ebeveyni olmasını zorunlu tutar.

## Çalıştırma

```bash
./.venv/Scripts/python scripts/run_smoke.py
```

## Denetim

Her PASS, kullanıcıya bulgu diye raporlanmadan önce bağımsız bir denetimden geçer: testi yazmayan model kodu ve veriyi okur, sızıntı, ortak gürültü, ölçüt kayması ve seçim etkisi arar, sonucu deftere `audit` notuyla yazar. Hedef hücreler ile girdi hücreleri (ikililer, referanslar) asla aynı SQS seed'ini paylaşmaz: `compute.py:56` yerleşimi yalnız (seed, n) ile belirler, ortak seed ortak gürültü demektir (S2 denetimi). Hedefler seed 100 ve üstünü kullanır. Her sürü turunda `audit` cephesi koşar.

## Kurallar

Veri dosyalarının üzerine yazma, yeni dosya üret. Elle girilen deneysel değerler kaynağıyla `harness/reference.py` içinde durur. `reports/` ve `research_notes/` kullanıcıya aittir, izinsiz değiştirme.

## Keşif sürüsü

`scripts/swarm.py` her cephe (`.orchestra/fronts/*.md`) için bir Astra ve bir Opus koşar, en fazla 4 ajan aynı anda. `dataset:` satırı arena veri kümesiyse adaylar arenaya gider, değilse öneri (iddia, sayısal tahmin, test, çürütücü) olarak `.orchestra/swarm/S<n>/proposals.jsonl` içine yazılır ve testi harness sahibi koşar. Her cephede diğer model eleştirir ve öncül iş kontrol eder. Çok aday arenada m'yi büyütür; eleştiride düşen aday m'ye sayılmaz.
