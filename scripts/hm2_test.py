"""Apply the pre-registered HM2 criteria (ledger 6560a94ce0) to data/hm_fresh_rows.csv. No tuning."""

import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402
from harness.features import parse_comp  # noqa: E402

pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
W = {tuple(sorted(c)): 4 * e for c, e in zip(eq.c, eq.E_mix)}
D = {tuple(sorted(c)): d for c, d in zip(eq.c, eq.dE_dlnV)}
C2 = {tuple(sorted(c)): d / 2 for c, d in zip(eq.c, eq.d2E_dlnV2)}
CN = {3: 0.005915, 4: 0.019090, 5: 0.028691}


def terms(c):
    v0 = sum(x * pv[e] for e, x in c.items())
    pair = vol = astra = quad = 0.0
    for a, b in combinations(sorted(c), 2):
        vij = 0.5 * (pv[a] + pv[b])
        L = np.log(v0 / vij)
        pair += c[a] * c[b] * W[(a, b)]
        vol += 4 * c[a] * c[b] * D[(a, b)] * L
        quad += 4 * c[a] * c[b] * C2[(a, b)] * L**2
        astra += c[a] * c[b] * W[(a, b)] * ((vij / v0) ** (5 / 3) - 1)
    return pair, vol, 2.1038433882662124 * astra, vol + quad


path = ROOT / "data" / "hm_fresh_rows.csv"
df = pd.read_csv(path)
df["c"] = df.comp.map(parse_comp)
df[["pair", "vol", "astra", "corr4"]] = [terms(c) for c in df.c]
df["delta"] = df.E_mix - df.pair
df["resid"] = df.delta - df.vol
m = df[df.n_el >= 3].copy()
cn = m.n_el.map(CN)
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
r_d, r_c, r_v, r_a = rm(m.delta), rm(m.delta - cn), rm(m.resid), rm(m.delta - m.astra)
t1 = bool(r_v <= 0.9 * r_d and r_v <= 0.9 * r_c)
t3 = bool(r_a < 0.9 * r_d and r_a < 0.9 * r_c)
rng = np.random.default_rng(0)
boot = [rng.choice(m.resid.values, len(m)).mean() for _ in range(2000)]
lo, hi = np.percentile(boot, [0.5, 99.5])
t2 = bool(lo > 0)
print(f"n={len(m)}  RMSE meV: Delta {r_d*1000:.1f}, const-by-n {r_c*1000:.1f}, vol-corrected {r_v*1000:.1f}, Astra {r_a*1000:.1f}")
print(f"residual mean {m.resid.mean()*1000:+.1f} meV, 99% CI [{lo*1000:+.1f}, {hi*1000:+.1f}];  SQS seed sd median {df.E_sd.median()*1000:.1f} meV")
print(m.groupby("n_el")[["delta", "vol", "resid"]].mean().mul(1000).round(1).to_string())
b = df[df.n_el == 2]
print(f"binaries n={len(b)} delta mean {b.delta.mean()*1000:+.1f}, resid mean {b.resid.mean()*1000:+.1f} meV")
out = ROOT / "data" / "hm2_test_rows.csv"
df.drop(columns="c").to_csv(out, index=False)
r4 = rm(m.delta - m.corr4)
pr = float(np.corrcoef(m.delta, m.corr4)[0, 1])
ks = []
for _ in range(2000):
    s = m.sample(len(m), replace=True, random_state=int(rng.integers(1 << 31)))
    ks.append(float(s.delta @ s.corr4 / (s.corr4 @ s.corr4)))
klo, khi = np.percentile(ks, [2.5, 97.5])
per_n = (m.delta - m.corr4).groupby(m.n_el).mean()
t4 = bool(r4 <= 0.6 * r_c and pr >= 0.8 and klo <= 1 <= khi and klo >= 0.7 and khi <= 1.3 and (per_n.abs() <= 0.010).all())
bo = b[b.c.map(lambda c: max(c.values()) > 0.501)]
print(f"T4 Opus quadratic: RMSE {r4*1000:.1f} (limit {0.6*r_c*1000:.1f}), r {pr:.3f}, k CI [{klo:.2f}, {khi:.2f}], "
      f"resid by n {(per_n*1000).round(1).to_dict()}; off-50:50 binaries RMSE {rm(bo.delta)*1000:.1f} -> {rm(bo.delta-bo.corr4)*1000:.1f}")
print("T1", t1, "T2", t2, "T3", t3, "T4", t4)
ledger.record(f"HM2-T4 Opus volume transfer on second holdout: {'passes' if t4 else 'fails'} (RMSE {r4*1000:.1f} vs limit "
              f"{0.6*r_c*1000:.1f}, r {pr:.2f}, k CI [{klo:.2f},{khi:.2f}])", "L0",
              [str(ROOT / 'data' / 'hm2_test_rows.csv')], notes="criteria fixed in d6da56412c")
ledger.record(f"HM2 on second holdout (n={len(m)}): T1 volume transfer {'passes' if t1 else 'fails'} "
              f"(RMSE {r_d*1000:.1f} -> {r_v*1000:.1f} meV); T2 fixed-volume residual {'passes' if t2 else 'fails'} "
              f"(mean {m.resid.mean()*1000:+.1f}, 99% CI [{lo*1000:+.1f}, {hi*1000:+.1f}]); T3 Astra {'passes' if t3 else 'fails'}",
              "L0", [str(out)], notes="criteria fixed in 6560a94ce0")
