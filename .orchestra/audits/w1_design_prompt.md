Görev: scripts/k_asym_w1.py test tasarımını, hesap başlamadan önce eleştir. Dosya değiştirme.

Bağlam: Wu 2021 (NCSU tezi, Eq 5.1) ve Marker 2017, ikili verilerden çok bileşenli excess C' ve C44'ü bileşim asimetrisiyle (Redlich-Kister, Muggianu) modelliyor ama her ikiliyi kendi denge hacminde tutuyor. Bizim kural (paper/draft_v5.md) yalnız 50:50 ikilileri alaşımın Vegard hacminde okuyor. W1 ikisini aynı veride karşılaştırıyor ve birleştiriyor (H1, H2; betiğin docstring'i). Okuman gerekenler: scripts/k_asym_w1.py, scripts/k_shear_transfer.py, harness/context.py, harness/ledger.py, harness/power.py, .orchestra/LESSONS.md.

Sorular:
1. OV-asym kolu Wu/Marker yaklaşımının adil bir temsilcisi mi? Özellikle: üç noktadan tam L0-L2, hacim olarak ikilinin Vegard hacmi (relakse denge hacmi değil), clamped hedef. Adaletsizlik varsa nasıl düzeltilmeli?
2. H1 ve H2 güç hesabı (gürültü = kuralın hm hedeflerindeki artığı) gerçekçi mi, sızıntı veya ölçüt kayması var mı? Hedef SQS seed 100, ikililer 0-2.
3. Hedef bileşim çekimi, Co'nun 40/80 satırda olması, alpha 0.0025: sorun var mı?
4. k_shear_transfer'ı import etmek yan etki yaratıyor mu?
5. Kodda hata (RK çözümü, Muggianu işareti x_a - x_b, spline'ın ln V ekseni, grid kapsamı) var mı?

Sonunda: VERDICT GO / GO WITH FIXES / NO-GO ve gerekli düzeltmelerin listesi.
