"""Is the shared shear floor a property of the composition or of the cell? (audit of b86e0d8a40, Astra)

python scripts/k_floor_cells.py
b86e0d8a40 passed, but K44 and K' came from the same seed-100 cell, so a residual shared by the two channels can be
single-cell configuration noise. Here every composition of that test gets two new cells with seeds unique to that
cell (2000 + 2i, 2001 + 2i), so no two cells share a permutation field and none shares one with the binaries (0-2).
A composition-level floor shows up across cells; cell noise does not.
PASS needs both: (1) cross-cell corr(e44 of cell a, e' of cell b), averaged over (a,b) and (b,a), >= 0.5; (2) the
joint fit K44_a - pair44 = k T44 + b e'_b, pooled over both orders, gives k in [0.7, 1.3] and b in [0.6, 1.3].
"""

import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import importlib.util  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from harness import ledger  # noqa: E402

spec = importlib.util.spec_from_file_location("kst", ROOT / "scripts" / "k_shear_transfer.py")
kst = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kst)
from harness import compute  # noqa: E402
from harness.features import parse_comp  # noqa: E402

ctx, curvatures = kst.ctx, kst.curvatures
spl = kst.spl
SRC = ROOT / "data" / "k_aniso_s100_clamped.csv"
OUT = ROOT / "data" / "k_floor_cells.csv"
SCRIPT = str(Path(__file__))
CLAIM = "Shared shear floor is compositional"

comps = list(pd.read_csv(SRC).comp)


def pr(c, ch, at):
    v = ctx.vegard(c)
    return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"]) if at else 0.0))
               for a, b, xa, xb in ctx.pairs(c))


C = [parse_comp(s) for s in comps]
R44, P44, RP = (np.array([pr(c, "K44", 1) for c in C]), np.array([pr(c, "K44", 0) for c in C]),
                np.array([pr(c, "Kp", 1) for c in C]))
T44 = R44 - P44


def judge(y44a, ypa, y44b, ypb):
    e44a, epa, e44b, epb = y44a - R44, ypa - RP, y44b - R44, ypb - RP
    r = 0.5 * (np.corrcoef(e44a, epb)[0, 1] + np.corrcoef(e44b, epa)[0, 1])
    X = np.r_[np.c_[T44, epb], np.c_[T44, epa]]
    Y = np.r_[y44a - P44, y44b - P44]
    k, b = np.linalg.lstsq(X, Y, rcond=None)[0]
    return bool(r >= 0.5 and 0.7 <= k <= 1.3 and 0.6 <= b <= 1.3), float(r), float(k), float(b)


# Power. H: a composition floor F (sd 2.4) shared by both channels, channel-specific composition terms (sd 0.8) and
# independent cell noise of the measured size (K44 1.44, K' 0.79 GPa; S2 audit). Null: no shared composition term;
# the same-cell correlation (~0.75, as observed) comes from cell noise u (sd 2.2) shared by the two channels of a cell.
regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    rng = np.random.default_rng(5)
    n = len(C)

    def draw(h):
        if h:
            F, g44, gp = rng.normal(0, 2.4, n), rng.normal(0, 0.8, n), rng.normal(0, 0.8, n)
            cell = lambda: (rng.normal(0, 1.44, n), rng.normal(0, 0.79, n))  # noqa: E731
        else:
            F, g44, gp = np.zeros(n), rng.normal(0, 1.0, n), rng.normal(0, 1.0, n)

            def cell():
                u = rng.normal(0, 2.2, n)
                return u + rng.normal(0, 0.6, n), u + rng.normal(0, 0.4, n)
        out = []
        for _ in range(2):
            n44, np_ = cell()
            out += [R44 + F + g44 + n44, RP + F + gp + np_]
        return out

    power = float(np.mean([judge(*draw(True))[0] for _ in range(300)]))
    fp = float(np.mean([judge(*draw(False))[0] for _ in range(300)]))
    print(f"n {n}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: the residual shared by K44 and K' (b86e0d8a40) belongs to the composition, not "
                          f"the cell; PASS if on two new cells per composition (unique seeds) for the {n} compositions "
                          f"of b86e0d8a40 the cross-cell corr(e44_a, e'_b) >= 0.5 and the joint fit K44_a - pair44 = "
                          f"k T44 + b e'_b gives k in [0.7, 1.3], b in [0.6, 1.3]",
                          SCRIPT, {"power": power, "false_pass": fp},
                          notes="Astra audit of b86e0d8a40 (.orchestra/audits/b86e0d8a40_astra.md), finding 2")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(map(tuple, pd.read_csv(OUT)[["comp", "cell"]].values)) if OUT.exists() else set()
for i, (s, c) in enumerate(zip(comps, C)):
    for cell in (0, 1):
        if (s, cell) in done:
            continue
        alloy = compute.solid_solution(c, "fcc", reps=3, seed=2000 + 2 * i + cell)
        x = compute.actual_fractions(alloy)
        r = {"comp": s, "cell": cell, "seed": 2000 + 2 * i + cell, **curvatures(alloy, x, ctx.vegard(c)),
             "time": dt.datetime.now().isoformat(timespec="seconds")}
        pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
print("floor cells done", flush=True)

t = pd.read_csv(OUT)
a = t[t.cell == 0].set_index("comp").loc[comps]
b = t[t.cell == 1].set_index("comp").loc[comps]
ok, r, k, bb = judge(a.K44.values, a.Kp.values, b.K44.values, b.Kp.values)
same = 0.5 * (np.corrcoef(a.K44 - R44, a.Kp - RP)[0, 1] + np.corrcoef(b.K44 - R44, b.Kp - RP)[0, 1])
print(f"cross-cell corr {r:.2f} (same-cell {same:.2f}); joint k {k:.2f}, b {bb:.2f} -> {'PASS' if ok else 'FAIL'}",
      flush=True)
ledger.record(f"{CLAIM}: {'PASS' if ok else 'FAIL'} (cross-cell corr {r:.2f}, same-cell {same:.2f}, k {k:.2f}, "
              f"b {bb:.2f})", "L0", [str(OUT), str(SRC), SCRIPT], notes=f"prereg {regs[0]['id']}")
