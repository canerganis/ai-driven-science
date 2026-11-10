"""Does the K' volume transfer hold with k = 1 under a second model? Equivalence test (Astra, audit of 6bc0e190a8).

python scripts/k_mpa_equiv.py
omat gives k 1.08 twice. mpa gave 1.33 (86767e478d, seed-0 targets and binaries) and then 1.10 [0.94, 1.26] on 150
leak-free alloys (unregistered). Here, under medium-mpa-0: 1200 new compositions, 200 in each stratum Co yes/no x
3/4/5 elements, two target cells each (seeds 10000 + 2i, + 1); two independent binary panels (seeds 20-22 and
23-25, the k_shear_transfer.py grid). Cross-panel estimator, so binary noise does not bias k:
  k = sum[T_A (y - p_B) + T_B (y - p_A)] / (2 sum T_A T_B),  y = mean of the two cells.
CI by bootstrap over compositions and over binary seeds within each panel.
PASS (practical equivalence): the 90% CI lies inside [0.90, 1.10]. Reported: the 95% CI and whether it excludes 1.
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
GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
PANELS = {"A": (20, 21, 22), "B": (23, 24, 25)}
BIN, TGT = ROOT / "data" / "k_mpa_equiv_binaries.csv", ROOT / "data" / "k_mpa_equiv_targets.csv"
ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
N = 108
ctx = context()
calc = compute.calculator()
SCRIPT = str(Path(__file__))
CLAIM = "K' transfer k = 1 under medium-mpa-0"


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


seen = set()
for f in ROOT.glob("data/*.csv"):
    if "sealed" in str(f):
        continue
    try:
        h = pd.read_csv(f, nrows=0).columns
        col = "comp_actual" if "comp_actual" in h else "comp" if "comp" in h else None
        if col:
            seen |= set(pd.read_csv(f, usecols=[col])[col].astype(str))
    except Exception:
        pass


def draw(rng, k, with_co):
    while True:
        pool = [e for e in ELS if e != "Co"]
        els = sorted([*rng.choice(pool, k - 1, replace=False), "Co"] if with_co else rng.choice(pool, k, replace=False))
        cnt = 11 + rng.multinomial(N - 11 * k, rng.dirichlet(np.ones(k)))
        c = {e: n / N for e, n in zip(els, cnt)}
        s = ";".join(f"{e}:{c[e]:.4f}" for e in sorted(c))
        if s not in seen:
            seen.add(s)
            return s, c


rng = np.random.default_rng(20261103)
comps = [draw(rng, k, co) for co in (False, True) for k in (3, 4, 5) for _ in range(200)]
C = [c for _, c in comps]
PAIRS = sorted({(a, b) for c in C for a, b, _, _ in ctx.pairs(c)})
# flattened pair terms over compositions: composition index, pair index, weight 4 x_i x_j, ln V0/V_ij
TI, TP, TW, TD = (np.array(v) for v in zip(*[(i, PAIRS.index((a, b)), 4 * xa * xb,
                                              np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"]))
                                             for i, c in enumerate(C) for a, b, xa, xb in ctx.pairs(c)]))


def predict(curves):
    """curves: (n_pairs, len(GRID)) -> (rule, pair-at-V_ij) over compositions."""
    at, at0 = np.empty(len(TI)), np.empty(len(TI))
    for p in range(len(PAIRS)):
        m = TP == p
        if m.any():
            sp = CubicSpline(GRID, curves[p])
            at[m], at0[m] = sp(TD[m]), sp(0.0)
    return np.bincount(TI, TW * at, len(C)), np.bincount(TI, TW * at0, len(C))


def khat(y, A, B):
    (rA, pA), (rB, pB) = A, B
    TA, TB = rA - pA, rB - pB
    return float((TA @ (y - pB) + TB @ (y - pA)) / (2 * TA @ TB))


def ci(y, curvesA, curvesB, n_boot, seed):
    """curvesX: array (3 seeds, n_pairs, len(GRID)). Bootstrap compositions and seeds within each panel."""
    r = np.random.default_rng(seed)
    ks = []
    for _ in range(n_boot):
        A = predict(curvesA[r.integers(0, 3, 3)].mean(0))
        B = predict(curvesB[r.integers(0, 3, 3)].mean(0))
        i = r.integers(0, len(y), len(y))
        ks.append(khat(y[i], (A[0][i], A[1][i]), (B[0][i], B[1][i])))
    return np.percentile(ks, [5, 95]), np.percentile(ks, [2.5, 97.5])


regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    # Power with the old mpa seed-0 binaries as the "true" curves: target scatter about the rule 2.36 GPa (150-alloy
    # residual, 6bc0e190a8), halved in variance by two cells; binary seed scatter of K' 0.71 GPa per seed (S2 audit).
    g = pd.read_csv(ROOT / "data" / "binary_kgrid_mpa.csv")
    true = np.array([g[g.pair == f"{a}-{b}"].sort_values("dlnV").Kp.values for a, b in PAIRS])
    rt, pt = predict(true)
    r2 = np.random.default_rng(8)

    def sim(k):
        y = pt + k * (rt - pt) + r2.normal(0, 2.36 / np.sqrt(2), len(C))
        cA = true[None] + r2.normal(0, 0.71, (3, *true.shape))
        cB = true[None] + r2.normal(0, 0.71, (3, *true.shape))
        lo, hi = ci(y, cA, cB, 100, int(r2.integers(1 << 30)))[0]
        return 0.90 <= lo and hi <= 1.10

    power, fp = float(np.mean([sim(1.0) for _ in range(60)])), float(np.mean([sim(1.15) for _ in range(60)]))
    print(f"n {len(C)}, power {power:.3f}, false pass (k 1.15) {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: on {len(C)} new compositions (Co yes/no x 3/4/5 elements, 200 each, two cells) "
                          f"with two independent mpa binary panels, the cross-panel k of the K' volume-transfer rule "
                          f"has a 90% CI inside [0.90, 1.10]", SCRIPT, {"power": power, "false_pass": fp},
                          notes="Astra audit of 6bc0e190a8; old mpa k 1.33 (86767e478d), leak-free 150 alloys 1.10")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(map(tuple, pd.read_csv(BIN)[["pair", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
for A, B in PAIRS:
    for seed in PANELS["A"] + PANELS["B"]:
        alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
        x = compute.actual_fractions(alloy)
        for d in GRID:
            if (f"{A}-{B}", str(seed), str(d)) in done:
                continue
            v = ctx.pair[(A, B)]["V"] * np.exp(d)
            pd.DataFrame([{"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "Kp": kp(alloy, x, v)}]).to_csv(
                BIN, mode="a", header=not BIN.exists(), index=False)
    print("binary", A, B, flush=True)

done = set(map(tuple, pd.read_csv(TGT)[["comp", "cell"]].values)) if TGT.exists() else set()
for i, (s, c) in enumerate(comps):
    for cell in (0, 1):
        if (s, cell) in done:
            continue
        alloy = compute.solid_solution(c, "fcc", reps=3, seed=10000 + 2 * i + cell)
        x = compute.actual_fractions(alloy)
        pd.DataFrame([{"comp": s, "cell": cell, "co": c.get("Co", 0.0), "n_el": len(c),
                       "Kp": kp(alloy, x, ctx.vegard(c)), "time": dt.datetime.now().isoformat(timespec="seconds")}]
                     ).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
print("equiv targets done", flush=True)

b = pd.read_csv(BIN)
curves = {p: np.array([[b[(b.pair == f"{x}-{z}") & (b.seed == s)].sort_values("dlnV").Kp.values for x, z in PAIRS]
                       for s in PANELS[p]]) for p in PANELS}
t = pd.read_csv(TGT).groupby("comp").Kp.mean()
y = t.loc[[s for s, _ in comps]].values
A, B = predict(curves["A"].mean(0)), predict(curves["B"].mean(0))
k = khat(y, A, B)
(l90, h90), (l95, h95) = ci(y, curves["A"], curves["B"], 2000, 0)
ok = 0.90 <= l90 and h90 <= 1.10
print(f"k {k:.3f}, 90% CI [{l90:.3f}, {h90:.3f}], 95% CI [{l95:.3f}, {h95:.3f}] -> {'PASS' if ok else 'FAIL'}; "
      f"95% CI {'excludes' if not l95 <= 1 <= h95 else 'contains'} 1", flush=True)
for lab, m in (("Co-free", np.array([c.get("Co", 0) == 0 for c in C])), ("Co", np.array([c.get("Co", 0) > 0 for c in C]))):
    print(f"  {lab}: k {khat(y[m], (A[0][m], A[1][m]), (B[0][m], B[1][m])):.3f}", flush=True)
ledger.record(f"{CLAIM}: {'PASS' if ok else 'FAIL'} (k {k:.3f}, 90% CI [{l90:.3f}, {h90:.3f}], 95% CI [{l95:.3f}, "
              f"{h95:.3f}])", "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")
