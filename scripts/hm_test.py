"""Apply the pre-registered HM criteria (ledger c542fcd2d5) to the h3 holdout. No tuning."""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402
from harness.features import parse_comp  # noqa: E402

h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
h1["c"] = h1.comp.map(parse_comp)
eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
W = {tuple(sorted(c)): 4 * e for c, e in zip(eq.c, eq.E_mix)}


def pair(c):
    els = sorted(c)
    return sum(c[a] * c[b] * W[(a, b)] for i, a in enumerate(els) for b in els[i + 1:])


def sat(c):  # Astra closure, frozen from astra_nonadd.md
    d = 0.0
    for i, xi in c.items():
        q = [xj * max(0.0, -W[tuple(sorted((i, j)))]) for j, xj in c.items() if j != i]
        d += 0.5 * xi * (sum(q) - math.sqrt(sum(v * v for v in q)))
    return d


def ci(v, rng):
    m = [rng.choice(v, len(v)).mean() for _ in range(2000)]
    return np.percentile(m, [0.5, 99.5])


path = ROOT / "data" / "h3_fresh_rows.csv"
df = pd.read_csv(path)
df["c"] = df.comp.map(parse_comp)
df["delta"] = df.E_mix - df.c.map(pair)
df["sat"] = df.c.map(sat)
rng = np.random.default_rng(0)
multi, bins = df[df.n_el >= 3], df[df.n_el == 2]
lo, hi = ci(multi.delta.values, rng)
blo, bhi = ci(bins.delta.values, rng)
primary = bool(lo > 0)
control = bool(blo <= 0 <= bhi)
rm = lambda e: float(np.sqrt(np.mean(e ** 2)))  # noqa: E731
r0, rc, rs = rm(multi.delta), rm(multi.delta - 0.0143), rm(multi.delta - multi.sat)
secondary = bool(rs < 0.9 * r0 and rs < 0.9 * rc)
print(f"multi n={len(multi)} mean {multi.delta.mean()*1000:+.1f} meV, 99% CI [{lo*1000:+.1f}, {hi*1000:+.1f}]")
print(f"binary n={len(bins)} mean {bins.delta.mean()*1000:+.1f} meV, 99% CI [{blo*1000:+.1f}, {bhi*1000:+.1f}]")
print(multi.groupby("n_el").delta.agg(["count", "mean", "std"]).mul([1, 1000, 1000]).round(1).to_string())
print(f"RMSE meV: zero {r0*1000:.1f}, const {rc*1000:.1f}, Astra closure {rs*1000:.1f}")
print("PRIMARY", primary, "CONTROL", control, "SECONDARY", secondary)
out = ROOT / "data" / "hm_test_rows.csv"
df.drop(columns="c").to_csv(out, index=False)
ledger.record(f"HM test on h3 holdout: primary {'passes' if primary else 'fails'} (multi n={len(multi)}, mean "
              f"{multi.delta.mean()*1000:+.1f} meV, 99% CI [{lo*1000:+.1f}, {hi*1000:+.1f}]); binary control "
              f"{'ok' if control else 'FAILS'}; Astra closure {'passes' if secondary else 'fails'}",
              "L0", [str(out)], notes="criteria fixed in c542fcd2d5")
