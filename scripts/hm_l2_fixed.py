"""L2 gate re-run on count-corrected data (scripts/fix_counts.py): actual whole-atom compositions, fixed references.

Delta = E_mix - sum x_i x_j W_ij; correction = sum 4 x_i x_j (dE_mix/dlnV)_ij ln(V0/V_ij), binary data from h1 only.
Gate (AGENTS.md): >= 40 rows, gain > 10% over the stronger of zero and const-by-n baselines, permutation p below
0.01 / 4 (four candidates were tested in this round). Null: correction shuffled within each n_el group.
"""

import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402
from harness.features import parse_comp  # noqa: E402

PARENT = "4c5076a083"  # MACE passes L1 for clamped E_mix(V) vs PBE
N_PERM, ALPHA = 20000, 0.01 / 4
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
W = {tuple(sorted(c)): 4 * e for c, e in zip(eq.c, eq.E_mix)}
D = {tuple(sorted(c)): d for c, d in zip(eq.c, eq.dE_dlnV)}


def corr(c):
    v0 = sum(x * pv[e] for e, x in c.items())
    return sum(4 * c[a] * c[b] * D[(a, b)] * np.log(v0 / (0.5 * (pv[a] + pv[b])))
               for a, b in combinations(sorted(c), 2))


def pair(c):
    return sum(c[a] * c[b] * W[(a, b)] for a, b in combinations(sorted(c), 2))


paths = [ROOT / "data" / "h3_fresh_rows_fixed.csv", ROOT / "data" / "hm_fresh_rows_fixed.csv"]
df = pd.concat([pd.read_csv(p)[["comp_actual", "n_el", "E_mix"]].rename(columns={"comp_actual": "comp"}).assign(src=p.stem)
                for p in paths])
df = df[df.n_el >= 3].reset_index(drop=True)
df["c"] = df.comp.map(parse_comp)
df["delta"] = df.E_mix - df.c.map(pair)
df["corr"] = df.c.map(corr)
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
base = min(rm(df.delta), rm(df.delta - df.groupby("n_el").delta.transform("mean")))
obs = rm(df.delta - df["corr"])
gain = 1 - obs / base
rng = np.random.default_rng(0)
groups = [g.index.values for _, g in df.groupby("n_el")]
d, c = df.delta.values, df["corr"].values
hits = 0
for _ in range(N_PERM):
    cp = c.copy()
    for idx in groups:
        cp[idx] = rng.permutation(cp[idx])
    hits += rm(d - cp) <= obs
p = (hits + 1) / (N_PERM + 1)
passed = bool(len(df) >= 40 and gain > 0.1 and p < ALPHA and 1 / (N_PERM + 1) < ALPHA)
print(f"rows {len(df)} ({df.src.value_counts().to_dict()}), baseline {base*1000:.1f}, rule {obs*1000:.1f} meV, "
      f"gain {gain:.2f}, permutation p {p:.2e} (alpha {ALPHA})  ->", "L2 PASS" if passed else "L2 FAIL")
out = ROOT / "data" / "hm_l2_rows_fixed.csv"
df.drop(columns="c").to_csv(out, index=False)
if False:  # re-evaluation; recorded below as an L0 note on 05f01df6ec
    ledger.record("Zero-parameter volume-transfer rule for multicomponent mixing energy: E_mix ~= sum_{i<j} x_i x_j "
                  "[W_ij + 4 (dE_mix/dlnV)_ij ln(V0/V_ij)], binary inputs only (50:50 E_mix and its log-volume slope at "
                  "the binary Vegard volume V_ij), V0 alloy Vegard volume. Clamped random fcc, MACE omat. "
                  f"Two holdouts pooled, n={len(df)}: RMSE {base*1000:.1f} -> {obs*1000:.1f} meV/atom, gain {gain:.2f}, "
                  f"within-n permutation p {p:.1e}. The apparent positive multicomponent excess (HM) is this volume "
                  "transfer; no fixed-volume many-body excess remains in random alloys (HM2-T2 failed).",
                  "L2", [str(out)], notes="parent L1 4c5076a083; pre-registered 6560a94ce0", parent=PARENT)
ledger.record(f"Re-evaluation of L2 05f01df6ec on count-corrected data: {'PASS' if passed else 'FAIL'} (n={len(df)}, "
              f"baseline {base*1000:.1f} -> rule {obs*1000:.1f} meV, gain {gain:.2f}, p {p:.1e})", "L0", [str(out)],
              notes="numerics correction (atom-count reference error, found by Astra and Opus in round R1)")
