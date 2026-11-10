"""Fresh blind test of the K' half of shear-curvature volume transfer (follow-up of prereg 4c29d9754c, result 6e0923b413).

python scripts/k_shear_kp_hm.py
The joint K44 + K' claim failed on h3 (K' passed, K44 p 0.023). Splitting it after the fact is not allowed
(.orchestra/LESSONS.md 14), so the K' claim gets its own test on alloys whose shear was never computed: hm_fresh rows
with n_el >= 3, minus compositions already in h3 or a2. Same binaries (data/binary_kgrid.csv), same a2 protocol,
references at the cell's actual fractions. PASS: RMSE(rule) <= 0.9 RMSE(pair at V_ij) and sign-flip p < 0.005.
K44 is computed alongside and reported, not gated.
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

# the binaries, curvature protocol and test come from the h3 script; its sections 1-4 are already done, so loading it
# only rebuilds the splines and reprints the h3 result
spec = importlib.util.spec_from_file_location("kst", ROOT / "scripts" / "k_shear_transfer.py")
kst = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kst)
from harness import compute  # noqa: E402
from harness.features import parse_comp  # noqa: E402

ctx, spl, curvatures, test = kst.ctx, kst.spl, kst.curvatures, kst.test
OUT = ROOT / "data" / "hm_shear_clamped.csv"
SCRIPT = str(Path(__file__))
CLAIM = "Shear-curvature volume transfer, K' channel"

hm = pd.read_csv(ROOT / "data" / "hm_fresh_rows_fixed.csv")
seen = set(pd.read_csv(ROOT / "data" / "h3_fresh_rows_fixed.csv").comp_actual) | set(
    pd.read_csv(ROOT / "data" / "a2_shear_clamped.csv").comp)
hm = hm[(hm.n_el >= 3) & ~hm.comp_actual.isin(seen)].reset_index(drop=True)
comps = [parse_comp(s) for s in hm.comp_actual]
keep = [all(((a, b), "Kp") in spl for a, b, _, _ in ctx.pairs(c)) for c in comps]
hm, comps = hm[keep].reset_index(drop=True), [c for c, k in zip(comps, keep) if k]


def predict(c, ch, at_alloy):
    v0 = ctx.vegard(c)
    return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
               for a, b, xa, xb in ctx.pairs(c))


P = {ch: (np.array([predict(c, ch, True) for c in comps]), np.array([predict(c, ch, False) for c in comps]))
     for ch in ("K44", "Kp")}

# realistic scatter: the larger of the rule's K' residual on a2 (exploratory) and on h3 (now seen)
h3 = pd.read_csv(kst.TGT).set_index("comp").loc[kst.h3.comp_actual]
SIG = max(kst.SIG["Kp"], float(np.sqrt(np.mean((h3.Kp.values - kst.P["Kp"][0]) ** 2))))
regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    rng = np.random.default_rng(2)
    sim = lambda truth: np.mean([test(P["Kp"][truth] + rng.normal(0, SIG, len(comps)), *P["Kp"], 1000, i)[0]  # noqa: E731
                                 for i in range(300)])
    power, fp = sim(0), sim(1)
    print(f"n {len(comps)}, sigma {SIG:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: clamped mixing K' of random fcc alloys equals sum 4 x_i x_j K'_ij(V0) with binary "
                          f"curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij and "
                          f"sign-flip p < 0.005 on {len(comps)} hm_fresh alloys whose shear has never been computed",
                          SCRIPT, {"power": power, "false_pass": fp},
                          notes="fresh test after joint claim 4c29d9754c failed on K44 only (6e0923b413)")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for s, c in zip(hm.comp_actual, comps):
    if s in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
    x = compute.actual_fractions(alloy)
    assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
    r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
print("targets done", flush=True)

t = pd.read_csv(OUT).set_index("comp").loc[hm.comp_actual]
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
out = {}
for ch in ("Kp", "K44"):
    y = t[ch].values
    ok, gain, p = test(y, *P[ch])
    T = P[ch][0] - P[ch][1]
    k = float(T @ (y - P[ch][1]) / (T @ T))
    out[ch] = ok
    print(f"{ch}{'' if ch == 'Kp' else ' (not gated)'}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, "
          f"rule {rm(y - P[ch][0]):.2f} GPa, gain {gain:.2f}, p {p:.1e}, refit k {k:.2f}, rule better in "
          f"{int(np.sum(abs(y - P[ch][0]) < abs(y - P[ch][1])))}/{len(y)} -> {'pass' if ok else 'fail'}", flush=True)
ledger.record(f"{CLAIM}: {'PASS' if out['Kp'] else 'FAIL'} on {len(comps)} unseen hm_fresh alloys; K44 reported, "
              f"not gated: {'pass' if out['K44'] else 'fail'}", "L0", [str(OUT), str(kst.BIN), SCRIPT],
              notes=f"prereg {regs[0]['id']}")
