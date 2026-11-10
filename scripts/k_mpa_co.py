"""Is the model dependence of the K' coefficient a Co effect? (swarm S3 cobalt front, Opus opus_2)

python scripts/k_mpa_co.py
86767e478d: under medium-mpa-0 the K' volume transfer holds but the refit k is 1.33 [1.11, 1.51], against 1.08 under
omat. Seen split of those rows: Co-free k 1.05 (n 55), Co alloys 1.48 (n 39). Here with mpa on the 150 compositions
of b86e0d8a40 (75 Co-free, 75 with Co >= 15%; never computed with mpa), one cell each with a seed unique to the cell
(3000 + i), disjoint from the mpa binaries (seed 0). Geometry (V_ij, Vegard V0) is the omat one, as in k_shear_mpa.py.
PASS needs all three on K': (1) Co-free: RMSE(rule) <= 0.9 RMSE(pair at V_ij), sign-flip p < 0.005 and the
bootstrap 95% CI of k contains 1; (2) k(Co) - k(Co-free) >= 0.15; (3) its bootstrap 95% CI excludes 0.
"""

import datetime as dt
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-mpa-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

from harness import compute, ledger  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.context import context  # noqa: E402
from harness.features import parse_comp  # noqa: E402

assert compute.MODEL == "medium-mpa-0"
AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
SRC, OUT = ROOT / "data" / "k_aniso_s100_clamped.csv", ROOT / "data" / "k_mpa_co.csv"
ctx = context()
calc = compute.calculator()
SCRIPT = str(Path(__file__))
CLAIM = "Model dependence of K' transfer is a Co effect"


def e_strained(atoms, v_atom, F):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    a.calc = calc
    t = time.perf_counter()
    e = a.get_potential_energy() / len(a)
    time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
    return e


def kp(alloy, x, v):
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
    F = lambda s: np.diag([np.exp(s), np.exp(-s), 1.0])  # noqa: E731
    em = [e_strained(alloy, v, F(s)) - sum(xi * e_strained(pures[el], v, F(s)) for el, xi in x.items()) for s in AMPS]
    return np.polyfit(AMPS, em, 2)[0] / 2 / v * GPA


g = pd.read_csv(ROOT / "data" / "binary_kgrid_mpa.csv")
spl = {tuple(k.split("-")): CubicSpline(s.dlnV, s.Kp) for k, s in g.groupby("pair")}
src = pd.read_csv(SRC)
comps, C, co = list(src.comp), [parse_comp(s) for s in src.comp], src.co.values > 0
rule = np.array([sum(4 * xa * xb * float(spl[(a, b)](np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"])))
                     for a, b, xa, xb in ctx.pairs(c)) for c in C])
pair = np.array([sum(4 * xa * xb * float(spl[(a, b)](0.0)) for a, b, xa, xb in ctx.pairs(c)) for c in C])
T = rule - pair
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731


def kfit(m, y):
    return float(T[m] @ (y[m] - pair[m]) / (T[m] @ T[m]))


def judge(y, n_boot=1000, seed=0):
    rng = np.random.default_rng(seed)
    m0, m1 = ~co, co
    d = (y[m0] - pair[m0]) ** 2 - (y[m0] - rule[m0]) ** 2
    p = (np.sum(np.array([(d * rng.choice([-1, 1], len(d))).mean() for _ in range(2000)]) >= d.mean()) + 1) / 2001
    gain = 1 - rm(y[m0] - rule[m0]) / rm(y[m0] - pair[m0])
    i0, i1 = np.flatnonzero(m0), np.flatnonzero(m1)
    bs0, bsd = [], []
    for _ in range(n_boot):
        a, b = rng.choice(i0, len(i0)), rng.choice(i1, len(i1))
        k0 = T[a] @ (y[a] - pair[a]) / (T[a] @ T[a])
        bs0.append(k0)
        bsd.append(T[b] @ (y[b] - pair[b]) / (T[b] @ T[b]) - k0)
    lo, hi = np.percentile(bs0, [2.5, 97.5])
    dlo, dhi = np.percentile(bsd, [2.5, 97.5])
    k0, k1 = kfit(m0, y), kfit(m1, y)
    ok = gain >= 0.10 and p < 0.005 and lo <= 1 <= hi and k1 - k0 >= 0.15 and dlo > 0
    return bool(ok), dict(gain=gain, p=p, k0=k0, ci0=(lo, hi), k1=k1, dci=(dlo, dhi))


regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    # realistic scatter: the mpa rule's K' residual on the 94 hm alloys after the refit (seen, 86767e478d)
    hm = pd.read_csv(ROOT / "data" / "hm_shear_clamped_mpa.csv")
    hc = [parse_comp(s) for s in hm.comp]
    hr = np.array([sum(4 * xa * xb * float(spl[(a, b)](np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"])))
                       for a, b, xa, xb in ctx.pairs(c)) for c in hc])
    hp = np.array([sum(4 * xa * xb * float(spl[(a, b)](0.0)) for a, b, xa, xb in ctx.pairs(c)) for c in hc])
    ht = hr - hp
    kh = ht @ (hm.Kp.values - hp) / (ht @ ht)
    SIG = float(np.std(hm.Kp.values - hp - kh * ht))
    r2 = np.random.default_rng(6)
    sim = lambda k0, k1: np.mean([judge(pair + np.where(co, k1, k0) * T + r2.normal(0, SIG, len(T)), 300, i)[0]  # noqa
                                  for i in range(200)])
    power, fp = float(sim(1.05, 1.48)), float(sim(1.33, 1.33))
    print(f"n {len(T)} (Co {co.sum()}), sigma {SIG:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: under medium-mpa-0 the K' rule on the {len(T)} compositions of b86e0d8a40 (cells "
                          f"with unique seeds 3000+i) gives, for Co-free alloys, gain >= 0.10, p < 0.005 and a k CI "
                          f"containing 1, and k(Co >= 15%) - k(Co-free) >= 0.15 with bootstrap CI above 0",
                          SCRIPT, {"power": power, "false_pass": fp},
                          notes="swarm S3 cobalt front, Opus opus_2 (seen split of 86767e478d: 1.05 vs 1.48)")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for i, (s, c) in enumerate(zip(comps, C)):
    if s in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=3000 + i)
    x = compute.actual_fractions(alloy)
    r = {"comp": s, "seed": 3000 + i, "co": c.get("Co", 0.0), "Kp": kp(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
print("mpa co targets done", flush=True)

y = pd.read_csv(OUT).set_index("comp").loc[comps].Kp.values
ok, d = judge(y, 4000, 0)
print(f"Co-free: gain {d['gain']:.2f}, p {d['p']:.1e}, k {d['k0']:.2f} [{d['ci0'][0]:.2f}, {d['ci0'][1]:.2f}]; "
      f"Co: k {d['k1']:.2f}; diff CI [{d['dci'][0]:.2f}, {d['dci'][1]:.2f}] -> {'PASS' if ok else 'FAIL'}", flush=True)
ledger.record(f"{CLAIM}: {'PASS' if ok else 'FAIL'} (Co-free gain {d['gain']:.2f}, k {d['k0']:.2f} "
              f"[{d['ci0'][0]:.2f}, {d['ci0'][1]:.2f}]; Co k {d['k1']:.2f}; diff CI [{d['dci'][0]:.2f}, {d['dci'][1]:.2f}])",
              "L0", [str(OUT), str(ROOT / "data" / "binary_kgrid_mpa.csv"), SCRIPT], notes=f"prereg {regs[0]['id']}")
