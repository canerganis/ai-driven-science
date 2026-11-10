"""Shear-curvature volume transfer (swarm S1, open front, Opus): a new observable for the champion's mechanism.

python scripts/k_shear_transfer.py
Claim: the clamped mixing shear curvatures of random fcc alloys are pair sums of 50:50 binary curvatures taken at the
alloy's own volume, K_alloy(V0) = sum 4 x_i x_j K_ij(V0), with no parameter. Baseline: the same pair sum at each
binary's own Vegard volume V_ij.
Order, so that the test is blind:
 1. binaries: K44, K' of the 50:50 binaries (SQS seeds 0-2) on a ln(V/V_ij) grid -> data/binary_kgrid.csv
 2. predictions on the h3_fresh compositions (comp_actual, n_el >= 3; K never computed there), power by simulation,
    pre-registration in the ledger
 3. targets: the same a2 protocol on those alloys, references at the cell's actual fractions -> data/h3_shear_clamped.csv
 4. test: per channel RMSE(rule) <= 0.9 RMSE(pair at V_ij) and paired sign-flip p < 0.005 (two channels); PASS needs
    both channels. Secondary (reported, not gated): Opus's prior on median dlnK/dlnV of binaries with |K| > 10 GPa,
    K44 in [-5, -1.5], K' in [-6, -2].
"""

import datetime as dt
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

from harness import compute, ledger  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.context import context  # noqa: E402
from harness.features import parse_comp  # noqa: E402

AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
BIN, TGT = ROOT / "data" / "binary_kgrid.csv", ROOT / "data" / "h3_shear_clamped.csv"
ctx = context()
calc = compute.calculator()
SCRIPT = str(Path(__file__))


def e_strained(atoms, v_atom, F):
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    a.calc = calc
    t = time.perf_counter()
    e = a.get_potential_energy() / len(a)
    time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
    return e


def F_of(name, s):
    if name == "K44":
        F = np.eye(3)
        F[0, 1] = s
        return F
    return np.diag([np.exp(s), np.exp(-s), 1.0])


def curvatures(alloy, x, v):
    """K44, Kp (GPa) of E_mix with references at fractions x, all at volume v and the same deformation."""
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
    out = {}
    for name in ("K44", "Kp"):
        em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
                                                         for el, xi in x.items()) for s in AMPS]
        c2 = np.polyfit(AMPS, em, 2)[0]
        out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
    return out


# 1. binaries
done = set(map(tuple, pd.read_csv(BIN)[["pair", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
for (A, B), p in sorted(ctx.pair.items()):
    for seed in (0, 1, 2):
        alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
        for d in GRID:
            if (f"{A}-{B}", str(seed), str(d)) in done:
                continue
            v = p["V"] * np.exp(d)
            r = {"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "V": v, **curvatures(alloy, {A: 0.5, B: 0.5}, v)}
            pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
    print("binary", A, B, flush=True)

g = pd.read_csv(BIN).groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
spl = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}

# 2. predictions, power, pre-registration
h3 = pd.read_csv(ROOT / "data" / "h3_fresh_rows_fixed.csv")
h3 = h3[h3.n_el >= 3].reset_index(drop=True)
comps = [parse_comp(s) for s in h3.comp_actual]
keep = [all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in comps]
h3, comps = h3[keep].reset_index(drop=True), [c for c, k in zip(comps, keep) if k]


def predict(c, ch, at_alloy):
    v0 = ctx.vegard(c)
    return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
               for a, b, xa, xb in ctx.pairs(c))


P = {ch: (np.array([predict(c, ch, True) for c in comps]), np.array([predict(c, ch, False) for c in comps]))
     for ch in ("K44", "Kp")}


def test(y, rule, pair, n_perm=4000, seed=0):
    e_r, e_p = y - rule, y - pair
    gain = 1 - np.sqrt(np.mean(e_r**2)) / np.sqrt(np.mean(e_p**2))
    d = e_p**2 - e_r**2
    rng = np.random.default_rng(seed)
    null = np.array([(d * rng.choice([-1, 1], len(d))).mean() for _ in range(n_perm)])
    p = (np.sum(null >= d.mean()) + 1) / (n_perm + 1)
    return gain >= 0.10 and p < 0.005, float(gain), float(p)


# Realistic scatter = the rule's residual on the exploratory a2 rows (h1 compositions, n_el >= 3), the arena's
# convention. A first design used the pair sum's residual there (4 GPa, includes the transfer signal itself) and had
# power 0.45, so it was not registered and no target was computed (ledger design note).
a2 = pd.read_csv(ROOT / "data" / "a2_shear_clamped.csv")
a2c = [parse_comp(s) for s in a2.comp]
a2k = [len(c) >= 3 and all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in a2c]
a2, a2c = a2[a2k], [c for c, k in zip(a2c, a2k) if k]
SIG = {ch: float(np.sqrt(np.mean((a2[ch].values - [sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"])))
                                                        for a, b, xa, xb in ctx.pairs(c)) for c, v in zip(a2c, a2.V0)])**2)))
       for ch in ("K44", "Kp")}
regs = [e for e in ledger.entries() if e["claim"].startswith("Shear-curvature volume transfer") and "prereg" in e["notes"]]
if not regs:
    if not any(e["claim"].startswith("Design note, shear-curvature transfer") for e in ledger.entries()):
        ledger.record("Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory "
                      "a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, "
                      "seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = "
                      f"rule residual on a2 {SIG}, the arena convention", "L0", [SCRIPT, str(BIN)],
                      notes="design; before registration")
    rng = np.random.default_rng(1)
    sim = lambda truth: np.mean([all(test(P[ch][truth] + rng.normal(0, SIG[ch], len(comps)),  # noqa: E731
                                          *P[ch], 1000, i)[0] for ch in P) for i in range(200)])
    power, fp = sim(0), sim(1)
    print(f"n {len(comps)}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal "
                          f"sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if "
                          f"in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on {len(comps)} h3_fresh "
                          f"alloys whose K has never been computed", SCRIPT, {"power": power, "false_pass": fp},
                          notes="proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first")
    print("registered", reg["id"], flush=True)
    regs = [reg]

# 3. targets
done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
for s, c in zip(h3.comp_actual, comps):
    if s in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
    x = compute.actual_fractions(alloy)
    assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
    r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
print("targets done", flush=True)

# 4. test
t = pd.read_csv(TGT).set_index("comp").loc[h3.comp_actual]
res = {}
for ch in ("K44", "Kp"):
    y = t[ch].values
    ok, gain, p = test(y, *P[ch])
    rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
    T = P[ch][0] - P[ch][1]
    k = float(T @ (y - P[ch][1]) / (T @ T))
    res[ch] = ok
    print(f"{ch}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, rule {rm(y - P[ch][0]):.2f} GPa, "
          f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}", flush=True)
sl = {}
for ch in ("K44", "Kp"):
    vals = [float(spl[((tuple(k.split('-'))), ch)](0, 1) / spl[((tuple(k.split('-'))), ch)](0))
            for k in g.pair.unique() if abs(spl[((tuple(k.split('-'))), ch)](0)) > 10]
    sl[ch] = (len(vals), float(np.median(vals)) if vals else float("nan"))
print("secondary: median dlnK/dlnV of binaries with |K| > 10 GPa:", sl, flush=True)
passed = all(res.values())
if __name__ == "__main__":  # k_shear_kp_hm.py imports this file for its splines; the h3 result is recorded once
    ledger.record(f"Shear-curvature volume transfer: {'PASS' if passed else 'FAIL'} on {len(comps)} unseen h3 alloys "
              f"(K44 {'pass' if res['K44'] else 'fail'}, Kp {'pass' if res['Kp'] else 'fail'}); binary slope prior {sl}",
              "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")
