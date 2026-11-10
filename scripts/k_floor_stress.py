"""Does the shared shear floor survive removal of the clamped pre-stress? (Astra audit of fd786169e3, finding 4)

python scripts/k_floor_stress.py
At the Vegard volume a clamped cell is not stress free. For the deformations of k_shear_transfer.py the energy
curvatures carry the initial stress (tensile positive): K44 = C44 + s_yy and K' = C' + (s_xx + s_yy)/2, both -P when
hydrostatic. This is a known identity, so a floor made of it is not new physics. Here the unstrained stress of every
cell (300 targets of k_floor_cells.csv, pures, binary grid seeds 0-2) is computed and subtracted from target and
binary curvatures alike (mixing stress = cell minus x-weighted pures at the same volume), then the floor test of
fd786169e3 is repeated on the corrected values.
PASS (floor is beyond pre-stress): cross-cell corr(e44_a, e'_b) of corrected residuals >= 0.5 and the joint fit
K44c_a - pair44c = k T44c + b e'c_b gives k in [0.7, 1.3], b in [0.6, 1.3].
"""

import datetime as dt
import sys
import time
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import importlib.util  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

from harness import ledger  # noqa: E402

spec = importlib.util.spec_from_file_location("kst", ROOT / "scripts" / "k_shear_transfer.py")
kst = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kst)
from harness import compute  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.features import parse_comp  # noqa: E402

ctx, calc = kst.ctx, kst.calc
CELLS, BIN = ROOT / "data" / "k_floor_cells.csv", kst.BIN
OUT_T, OUT_B = ROOT / "data" / "k_floor_stress_targets.csv", ROOT / "data" / "k_floor_stress_binaries.csv"
SCRIPT = str(Path(__file__))
CLAIM = "Shared shear floor beyond pre-stress"


def stress(atoms, v_atom):
    """Unstrained stress (GPa, tensile positive) of the cell scaled to v_atom."""
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    t = time.perf_counter()
    s = a.get_stress(voigt=False) * GPA
    time.sleep(time.perf_counter() - t)  # 50% duty cycle
    return s


@lru_cache(maxsize=None)
def pure_stress(el, v):
    return stress(bulk(el, "fcc", a=4.0, cubic=True), v)


def corr44(s):
    return s[1, 1]


def corrp(s):
    return 0.5 * (s[0, 0] + s[1, 1])


def mix(atoms, x, v):
    s = stress(atoms, v) - sum(xi * pure_stress(el, v) for el, xi in x.items())
    return corr44(s), corrp(s)


cells = pd.read_csv(CELLS)
comps = list(dict.fromkeys(cells.comp))
C = {s: parse_comp(s) for s in comps}


def build_rule(bc):
    g = bc.groupby(["pair", "dlnV"])[["K44c", "Kpc"]].mean().reset_index()
    sp = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44c", "Kpc")}

    def pr(c, ch, at):
        v = ctx.vegard(c)
        return sum(4 * xa * xb * float(sp[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"]) if at else 0.0))
                   for a, b, xa, xb in ctx.pairs(c))
    return pr


def judge(pr, ta, tb):
    cs = [C[s] for s in comps]
    R44, P44, RP = (np.array([pr(c, "K44c", 1) for c in cs]), np.array([pr(c, "K44c", 0) for c in cs]),
                    np.array([pr(c, "Kpc", 1) for c in cs]))
    T44 = R44 - P44
    e44a, epa, e44b, epb = ta.K44c.values - R44, ta.Kpc.values - RP, tb.K44c.values - R44, tb.Kpc.values - RP
    r = 0.5 * (np.corrcoef(e44a, epb)[0, 1] + np.corrcoef(e44b, epa)[0, 1])
    k, b = np.linalg.lstsq(np.r_[np.c_[T44, epb], np.c_[T44, epa]],
                           np.r_[ta.K44c.values - P44, tb.K44c.values - P44], rcond=None)[0]
    same = 0.5 * (np.corrcoef(e44a, epa)[0, 1] + np.corrcoef(e44b, epb)[0, 1])
    return bool(r >= 0.5 and 0.7 <= k <= 1.3 and 0.6 <= b <= 1.3), float(r), float(k), float(b), float(same)


# Power from the fd786169e3 design, with the pre-stress part P (rms 0.66 GPa from the S3 floor-front pressure rows,
# Astra's approximate check) shared by both channels. H: compositional floor F sd 2.4 beyond P. Null: the whole
# floor is pre-stress (sd 2.5) and is removed exactly; what remains is channel-specific (sd 0.8) plus cell noise.
regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    rng = np.random.default_rng(7)
    n = len(comps)

    def sim(h):
        F = rng.normal(0, 2.4 if h else 0.0, n)
        g44, gp = rng.normal(0, 0.8, n), rng.normal(0, 0.8, n)
        y = []
        for _ in range(2):
            y += [F + g44 + rng.normal(0, 1.08, n), F + gp + rng.normal(0, 0.70, n)]
        r = 0.5 * (np.corrcoef(y[0], y[3])[0, 1] + np.corrcoef(y[2], y[1])[0, 1])
        return r >= 0.5

    power, fp = float(np.mean([sim(True) for _ in range(1000)])), float(np.mean([sim(False) for _ in range(1000)]))
    print(f"n {n}, power {power:.3f}, false pass {fp:.3f} (corr gate; k, b gates as in fd786169e3)", flush=True)
    reg = ledger.register(f"{CLAIM}: after subtracting the clamped initial mixing stress (K44 - s_yy, K' - (s_xx + "
                          f"s_yy)/2) from targets and binaries alike, the fd786169e3 floor test still passes on the "
                          f"same {n} compositions x 2 cells: cross-cell corr >= 0.5, joint k in [0.7, 1.3], b in "
                          f"[0.6, 1.3]", SCRIPT, {"power": power, "false_pass": fp},
                          notes="Astra audit of fd786169e3, finding 4; known identity K = C + initial stress")
    print("registered", reg["id"], flush=True)
    regs = [reg]

# binaries: unstrained mixing stress on the grid, seeds 0-2, the cells of k_shear_transfer.py
done = set(map(tuple, pd.read_csv(OUT_B)[["pair", "seed", "dlnV"]].astype(str).values)) if OUT_B.exists() else set()
for (A, B), p in sorted(ctx.pair.items()):
    for seed in (0, 1, 2):
        alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
        x = compute.actual_fractions(alloy)
        for d in kst.GRID:
            if (f"{A}-{B}", str(seed), str(d)) in done:
                continue
            s44, sp = mix(alloy, x, p["V"] * np.exp(d))
            pd.DataFrame([{"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "s44": s44, "sp": sp}]).to_csv(
                OUT_B, mode="a", header=not OUT_B.exists(), index=False)
print("binary stress done", flush=True)

done = set(map(tuple, pd.read_csv(OUT_T)[["comp", "cell"]].values)) if OUT_T.exists() else set()
for _, r in cells.iterrows():
    if (r.comp, r.cell) in done:
        continue
    c = C[r.comp]
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=int(r.seed))
    s44, sp = mix(alloy, compute.actual_fractions(alloy), ctx.vegard(c))
    pd.DataFrame([{"comp": r.comp, "cell": r.cell, "s44": s44, "sp": sp,
                   "time": dt.datetime.now().isoformat(timespec="seconds")}]).to_csv(
        OUT_T, mode="a", header=not OUT_T.exists(), index=False)
print("target stress done", flush=True)

bc = pd.read_csv(BIN).merge(pd.read_csv(OUT_B), on=["pair", "seed", "dlnV"])
bc["K44c"], bc["Kpc"] = bc.K44 - bc.s44, bc.Kp - bc.sp
t = cells.merge(pd.read_csv(OUT_T), on=["comp", "cell"])
t["K44c"], t["Kpc"] = t.K44 - t.s44, t.Kp - t.sp
ta, tb = (t[t.cell == i].set_index("comp").loc[comps] for i in (0, 1))
ok, r, k, b, same = judge(build_rule(bc), ta, tb)
print(f"corrected: cross-cell corr {r:.2f} (same-cell {same:.2f}); joint k {k:.2f}, b {b:.2f} -> "
      f"{'PASS' if ok else 'FAIL'}; rms target pre-stress K44 {np.sqrt(np.mean(t.s44**2)):.2f}, "
      f"K' {np.sqrt(np.mean(t.sp**2)):.2f} GPa", flush=True)
ledger.record(f"{CLAIM}: {'PASS' if ok else 'FAIL'} (corrected cross-cell corr {r:.2f}, same-cell {same:.2f}, k {k:.2f}, "
              f"b {b:.2f})", "L0", [str(OUT_T), str(OUT_B), str(CELLS), SCRIPT], notes=f"prereg {regs[0]['id']}")
