"""Is the refit k ~ 0.8 of the volume-transfer rule regression dilution from noisy seed-0 binary inputs?

python scripts/k_dilution.py   (diagnostic on the already-used holdouts; no ledger promotion from this)
Binary inputs from three SQS seeds (h1 = seed 0, data/binary_seeds.csv = seeds 1, 2).
  k_naive : OLS slope of delta on T built from seed 0 (as in hm_l2.py)
  k_IV    : instrumental-variable slope, T(seed 0) instrumented by T(seed 1): cov(y, T1) / cov(T0, T1)
  k_avg   : OLS slope with T built from the 3-seed mean inputs
"""

import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness.features import parse_comp  # noqa: E402

pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))].assign(seed=0)
bs = pd.read_csv(ROOT / "data" / "binary_seeds.csv")
allb = pd.concat([eq[["comp", "seed", "E_mix", "dE_dlnV"]], bs[["comp", "seed", "E_mix", "dE_dlnV"]]])
allb["pair"] = allb.comp.map(lambda s: tuple(sorted(parse_comp(s))))
piv = allb.pivot_table(index="pair", columns="seed", values=["E_mix", "dE_dlnV"])
D = {s: piv["dE_dlnV"][s].to_dict() for s in (0, 1, 2)}
D["avg"] = piv["dE_dlnV"].mean(axis=1).to_dict()
W = {s: (4 * piv["E_mix"][s]).to_dict() for s in (0, 1, 2)}
W["avg"] = (4 * piv["E_mix"].mean(axis=1)).to_dict()
sdD = piv["dE_dlnV"].std(axis=1, ddof=1)
sdE = piv["E_mix"].std(axis=1, ddof=1)
print(f"binary seed scatter: sd(E_mix) median {sdE.median()*1000:.1f} meV, sd(dE/dlnV) median {sdD.median()*1000:.1f} "
      f"meV (spread of dE/dlnV across pairs {piv['dE_dlnV'][0].std()*1000:.0f} meV)")


def T(c, s):
    v0 = sum(x * pv[e] for e, x in c.items())
    return sum(4 * c[a] * c[b] * D[s][(a, b)] * np.log(v0 / (0.5 * (pv[a] + pv[b]))) for a, b in combinations(sorted(c), 2))


def pair(c, s):
    return sum(c[a] * c[b] * W[s][(a, b)] for a, b in combinations(sorted(c), 2))


d = pd.read_csv(ROOT / "data" / "hm_l2_rows.csv")
d["c"] = d.comp.map(parse_comp)
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
rng = np.random.default_rng(0)
for src in ("h3_fresh_rows", "hm_fresh_rows", None):
    s = d if src is None else d[d.src == src]
    T0, T1, Ta = (s.c.map(lambda c: T(c, k)).values for k in (0, 1, "avg"))
    y0 = (s.E_mix - s.c.map(lambda c: pair(c, 0))).values
    ya = (s.E_mix - s.c.map(lambda c: pair(c, "avg"))).values
    ols = lambda y, x: np.cov(y, x)[0, 1] / np.var(x, ddof=1)  # noqa: E731
    iv = lambda y, x, z: np.cov(y, z)[0, 1] / np.cov(x, z)[0, 1]  # noqa: E731
    boot = []
    for _ in range(2000):
        i = rng.integers(0, len(s), len(s))
        boot.append(iv(y0[i], T0[i], T1[i]))
    lo, hi = np.percentile(boot, [2.5, 97.5])
    print(f"{src or 'pooled':14s} n={len(s)}  k_naive {ols(y0, T0):.2f}  k_IV {iv(y0, T0, T1):.2f} [{lo:.2f}, {hi:.2f}]  "
          f"k_avg {ols(ya, Ta):.2f}  RMSE rule seed0 {rm(y0 - T0)*1000:.1f}, avg inputs {rm(ya - Ta)*1000:.1f} meV")
