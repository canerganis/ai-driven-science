# Durum (2 Kasım 2026)

Tek giriş noktası. Ayrıntı ve kanıt defterde (`claims/claims.jsonl`, kimlikler aşağıda), dersler `.orchestra/LESSONS.md` içinde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabahına ait ve eskidir ("iki bağımsız holdout" ifadesi d26bd71285 ile düzeltildi).

## Bulgular

| # | Bulgu | Seviye | Kanıt | Açık olan |
|---|---|---|---|---|
| 1 | **K' hacim transferi.** Rastgele fcc alaşımın karışım K' değeri = Σ 4 x_i x_j K'_ij(V0), ikililer alaşım hacminde. İki kör sette hata yarıya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c → 6e0923b413 (ortak iddia K44 yüzünden FAIL); hm_fresh: 67a358fc59 → d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883 → 86767e478d), ama sızıntısız 150 alaşımda 1.10 [0.94, 1.26] (kayıtsız; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 alaşım, k 1.14 [1.10, 1.18], kural yine hatayı 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatası yok). k kompozisyona bağlı (keşifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddiası düştü; büyük hacim farkında transfer eksik kalıyor. PBE yok. Literatür (tam metin): kısmen biliniyor; hacim adımı, kör test ve K'/K44 karşıtlığı bulunamadı. "Hacim transferli regular-solution / kesik tensörel CE kuralı" diye yazılmalı, Marker 2017 okunmadan yazılmamalı. |
| 2 | **Enerji hacim transferi: DÜŞTÜ.** Standart Muggianu (saf elementler kendi hacminde) aynı işi yapıyor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde düzeltme). Eski metin: E_mix hatası 36.4 → 13.1 meV, yalnız hm_fresh (n 94) gerçekten kördü. Tam hesapta k 0.94 ile 0.98; 0.81 doğrusallaştırma etkisi. | L2 (05f01df6ec, düzeltme d26bd71285) | 1708d0db77, k_direct | Fikrin özü Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE düzenli hücre L3'ü FAIL (8541e914ea). |
| 3 | **K44 Co'suz alaşımlarda transfer oluyor** (ön kayıt e410c96a32 → d9460850ce, 120 taze alaşım, kazanç 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazanç 0.11). Eski gözlem: Aynı kural K44'te zayıf: kazanç 0.12 ile 0.20, k 0.69 ile 0.86. En kötü hatalar Co'ca zengin alaşımlarda. | gözlem | LESSONS 14 ile 16 | Neden açık; bağımsız denetim yapılmadı. Keşif bakışı (görülmüş 269 satır, kayıt değil): "E_F'de yüksek DOS" açıklaması desteklenmiyor, artık Pd/Pt/Ni/Rh/Ir/Co oranıyla iki kanalda da benzer büyüyor (K44/K' rms oranı 1.15 ile 1.4). En büyük hatalar iki kanalda da Co'lu alaşımlarda (|r44| ile Co r 0.33): sıradaki şüpheli Co manyetizması. K44'ün hacim kayması da küçük, kazanç için az yer var (a2: pair 3.56 → kural 2.66, K' 5.67 → 1.80). |
| 3b | **Ortak kayma tabanı.** Hacim kuralının K44 ve K''te kaçırdığı kısım aynı ve kompozisyona ait: K44 - K' kuralı geçiyor (kazanç 0.49), hücreler arası r 0.75, bilinen ön gerilme özdeşliği çıkarılınca r 0.67, k 0.99. K44'ün "tutmaması" bu tabandan. | L0, üç ön kayıtlı PASS (b86e0d8a40, fd786169e3, ede47f1d65), üçü de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | İkili referanslardan gelen ortak hata dışlanmadı (iki bağımsız ikili paneli gerekli). Fiziksel anlamı açık; MACE only. |
| 4 | **MACE karışım kayma eğriliğinde L1'den geçmiyor.** 8 düzenli L1_2 hücrede K' işareti 8/8 doğru, K44 işareti 5/8 (Au3Ir PBE −32.4, MACE +3.2 GPa); medyan sapma K' için %47, K44 için %56. K' kuralı yalnız MACE içinde gösterilmiş sayılır. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho bitti (0ce1deb7de); draft_v5 5.1'e işlendi. |
| 5 | **H-iso.** Hücre içi işaret okumasıyla PASS (n 6, medyan K44/K' 0.94), tek işaret okumasıyla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: hücre bazında izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, açık) | `scripts/hiso_l12_v2.py` | Kontroller bitti (0ce1deb7de): cutoff etkisiz, okuma değişmedi; Ag3Rh K44 k-yakınsak değil, verdict numerics olarak açık kalıyor. |

Yanlışlanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapanışı) ve gerekçeleri defterde `verdict on ...` kayıtlarında.

## Çalışan işler

- **H-iso kontrolleri (PBE, 2 çekirdek, sıralı):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir değişmedi (K44 −54.75 → −54.71, K' −57.39 → −57.42). Ag3Rh K' kararlı (−17.97 → −17.44) ama K44 −7.04 → −3.64 GPa, oran 0.39 → 0.21: Ag3Rh K44 k-yakınsak değil. Medyan K44/K' 0.942 → 0.941, işaretler aynı, H-iso okuması değişmiyor. rho koşusu 2 Kasım 13:43'te reboot ile 8/18'de kesildi; 3 Kasım 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`). Ag3Rh ecutrho ×1.5: K44 −7.038 → −7.039, K' −17.967 → −17.967, cutoff etkisiz. Pt3Cu ecutrho ×1.5: K44 23.829 → 23.829, K' 9.128 → 9.127, cutoff etkisiz; negative rho yüksek cutoff'ta da var (psödopotansiyel kaynaklı görünüyor). Defter 0ce1deb7de.
- **W1 (Wu/Marker boşluğu):** `scripts/k_asym_w1.py`. İkililer kendi Vegard hacminde ve asimetrik (BV-asym, Wu/Marker analoğu) ile bizim kural (VV-sym) ve birleşimi (VV-asym) 80 taze, eşit oranlı olmayan hedefte; H1, H2, H3 K' üzerinde, alpha 0.005/3. Astra tasarım denetimi 4 tur (`.orchestra/audits/w1_design*_astra.md`): ilk üç NO-GO (asym kolunun sym'e eşit olması dahil), dördüncü GO WITH FIXES, düzeltmeler uygulandı. 9 Kasım'da kullanıcı isteğiyle durduruldu (215 ikili satır, Ag-Ni'de; ön kayıt yok, hedef yok). Aynı komut kaldığı yerden devam eder. Sıra: `python scripts/k_asym_w1.py` (ikililer, 1746 + 216 tanı hesabı, güç, ön kayıt), sonra `python scripts/k_asym_w1.py targets`.

## Sıradaki adımlar

1. H-iso kontrolleri bitti (0ce1deb7de). Kesinleştirmek için Ag3Rh K44'ün kspacing 0.06 ile yakınsatılması gerekir; makale için şart değil, verdict numerics olarak açık.
2. K' kuralı için PBE (L3). **Tasarım uyarısı:** düzenli 4 atomlu hücreler enerji kuralında PBE'de +10 meV'lik sabit hacim çok cisim terimi taşıdığı için yanlış test çıktı (d440b9eb7b, 8541e914ea). K' için de düzenli hücre kullanılacaksa bu önce düşünülmeli; doğru alan PBE SQS hücreleri (32 atom ve üstü) ve bu laptopta günler sürer, kiralık sunucu seçeneği var.
3. PBE hızlandırma: Cu3Ir'de smearing ve k-ağı gevşetmeyi referansa karşı test et.
4. ~~Veri düzeltmesi~~ yapıldı (2 Kasım): `scripts/fix_counts2.py` → `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 üçlüde −0.31 ile −0.71 meV, R ve B_chem yeniden). hm3 ve diğerlerinde 1/3 yok, yeni mühür gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumalı.
5. L4 (2 Kasım): son tarama ve Astra denetimi yapıldı (`claims/literature.jsonl` satır 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma türevi, özgül uygulama bulunmadı. Wu 2021 tezi okundu (satır 65): ikili EMTO'dan bcc üçlülere excess C' ve C44 aktarımı var, ama her bileşim kendi hacminde; Vegard hacmi adımı yok. L4 taraması kapandı (arama sınırlı), en yakın öncül olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kuralın MACE içinde tutmasının model yanlılığı olabileceğini düşündürüyor; PBE aktarım testi bu yüzden daha önemli.
5b. Deney verisi (ajan taraması 1 Kasım): bu dokuz elementte ölçülmüş tek kristal alaşım sabitleri yalnız kapalı erişimde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bileşenli ölçüm yok. Kütüphane PDF'i gerekli.
5c. ~~nspin hatası~~ düzeltildi (2 Kasım): `extra={'system.nspin': 1}` artık başlangıç momenti koymuyor, Co girdisinde nspin 1 doğrulandı.
6. Makale: `paper/draft_v5.md` (v4 artı model yanlılığı sınırı, madde 6, ve Soyemi, Chong kaynakları; arşiv henüz v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) bütün kapsam ve sayı düzeltmeleri uygulandı. Arşiv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest doğru; arşivden `chain.py` ve `fix_counts2.py` birebir üretiyor). Gönderim için kalan: yazarın son okuması, Zenodo'ya arşiv yükleme ve DOI'yi metne yazma, ChemRxiv gönderimi. Bunları yazar yapar. Dense/rho sonucu v5 5.1'e işlendi (9 Kasım); v5 arşivi `paper/repro_20261109.zip`.

## Harness haritası

| Parça | Yer |
|---|---|
| Hesap (MACE, SQS, curvature) | `harness/compute.py`, `harness/context.py` (ikili V_ij, Vegard) |
| PBE | `harness/dft.py` (`Settings(kpts=..., ecut_elements=...)` zorunlu) |
| Defter, ön kayıt, güç | `harness/ledger.py`, `harness/power.py` |
| Arena (mühürlü holdout) | `harness/arena.py`, `data/sealed/`, `candidates/` |
| Ajanlar | `scripts/discovery_round.py` (arena turu), `scripts/swarm.py` (cepheler `.orchestra/fronts/`) |
| K' testleri | `scripts/k_shear_transfer.py` (h3), `k_shear_kp_hm.py` (hm_fresh), `k_shear_mpa.py` (model değişimi); veri `data/binary_kgrid*.csv`, `data/*_shear_clamped*.csv` |
| Enerji kuralı | `scripts/hm_l2_fixed.py`, `scripts/k_direct.py`, `candidates/champion_volume_transfer.py` |

Veri kümeleri: h1 (keşif, görülmüş), h3 (model seçiminde kullanıldı, K için kördü), hm_fresh (enerji ve K' için kördü, artık görüldü), hm3fix (mühürlü, ajanlar görmez).
