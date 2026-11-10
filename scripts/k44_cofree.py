"""Does the K44 volume-transfer rule hold once Co is out? (follow-up of LESSONS 14-16, literature 2026-10-31)

python scripts/k44_cofree.py
K44 transferred weakly on h3, hm_fresh and under mpa; the largest residuals sit in Co alloys in both channels
(exploratory, seen rows: |r44| vs Co r 0.33). Hypothesis: the K44 failure is a Co effect (fcc Co is magnetic, MACE
has no spin), not a property of the C44 strain. Fresh compositions (random, never computed, n_el 3-5 from the nine
elements, every element >= 10%) in two sets: Co-free (gated) and with Co >= 15% (reported, not gated).
PASS (Co-free K44): RMSE(rule) <= 0.9 RMSE(pair at V_ij) and sign-flip p < 0.005, same test as k_shear_transfer.py.
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

ctx, spl, curvatures, test = kst.ctx, kst.spl, kst.curvatures, kst.test
OUT = ROOT / "data" / "k44_cofree_clamped.csv"
SCRIPT = str(Path(__file__))
CLAIM = "K44 volume transfer without Co"
ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
N = 108

seen = set()
for f in ("a2_shear_clamped", "h3_shear_clamped", "hm_shear_clamped"):
    seen |= set(pd.read_csv(ROOT / "data" / f"{f}.csv").comp)
for f in ("h3_fresh_rows_fixed", "hm_fresh_rows_fixed"):
    seen |= set(pd.read_csv(ROOT / "data" / f"{f}.csv").comp_actual)


def draw(rng, with_co):
    while True:
        k = int(rng.integers(3, 6))
        pool = [e for e in ELS if e != "Co"]
        els = sorted(([*rng.choice(pool, k - 1, replace=False), "Co"]) if with_co else rng.choice(pool, k, replace=False))
        cnt = 11 + rng.multinomial(N - 11 * k, rng.dirichlet(np.ones(k)))
        c = {e: n / N for e, n in zip(els, cnt)}
        s = ";".join(f"{e}:{c[e]:.4f}" for e in sorted(c))
        if (not with_co or c["Co"] >= 0.15) and s not in seen and all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)):
            seen.add(s)
            return s, c


rng = np.random.default_rng(20261101)
sets = {"cofree": [draw(rng, False) for _ in range(120)], "co": [draw(rng, True) for _ in range(60)]}


def predict(c, at_alloy):
    v0 = ctx.vegard(c)
    return sum(4 * xa * xb * float(spl[((a, b), "K44")](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
               for a, b, xa, xb in ctx.pairs(c))


P = {k: (np.array([predict(c, True) for _, c in v]), np.array([predict(c, False) for _, c in v])) for k, v in sets.items()}

# realistic scatter: the rule's K44 residual on the seen Co-free alloys (a2, h3, hm)
res = []
for f in ("a2_shear_clamped", "h3_shear_clamped", "hm_shear_clamped"):
    d = pd.read_csv(ROOT / "data" / f"{f}.csv")
    for s, y in zip(d.comp, d.K44):
        c = parse_comp(s)
        if len(c) >= 3 and "Co" not in c and all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)):
            res.append(y - predict(c, True))
SIG = float(np.sqrt(np.mean(np.square(res))))
regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    r2 = np.random.default_rng(3)
    sim = lambda truth: np.mean([test(P["cofree"][truth] + r2.normal(0, SIG, len(sets["cofree"])),  # noqa: E731
                                      *P["cofree"], 1000, i)[0] for i in range(300)])
    power, fp = sim(0), sim(1)
    print(f"seen Co-free n {len(res)}, sigma {SIG:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: clamped mixing K44 of Co-free random fcc alloys equals sum 4 x_i x_j K44_ij(V0) "
                          f"with binary curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij "
                          f"and sign-flip p < 0.005 on {len(sets['cofree'])} fresh random Co-free alloys; "
                          f"{len(sets['co'])} Co >= 15% alloys reported, not gated",
                          SCRIPT, {"power": power, "false_pass": fp},
                          notes="hypothesis: K44 failure (LESSONS 14-16) is a Co effect; exploratory hint from seen rows")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for name, v in sets.items():
    for s, c in v:
        if s in done:
            continue
        alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
        x = compute.actual_fractions(alloy)
        assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
        r = {"set": name, "comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
             "time": dt.datetime.now().isoformat(timespec="seconds")}
        pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
print("cofree targets done", flush=True)

t = pd.read_csv(OUT).set_index("comp")
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
out = {}
for name, v in sets.items():
    for ch in ("K44", "Kp"):
        y = t.loc[[s for s, _ in v], ch].values
        rule = P[name] if ch == "K44" else (
            np.array([sum(4 * xa * xb * float(spl[((a, b), "Kp")](np.log(ctx.vegard(c) / ctx.pair[(a, b)]["V"])))
                          for a, b, xa, xb in ctx.pairs(c)) for _, c in v]),
            np.array([sum(4 * xa * xb * float(spl[((a, b), "Kp")](0.0)) for a, b, xa, xb in ctx.pairs(c)) for _, c in v]))
        ok, gain, p = test(y, *rule)
        T = rule[0] - rule[1]
        k = float(T @ (y - rule[1]) / (T @ T))
        out[(name, ch)] = ok
        print(f"{name} {ch}{' (gated)' if (name, ch) == ('cofree', 'K44') else ''}: pair at V_ij {rm(y - rule[1]):.2f}, "
              f"rule {rm(y - rule[0]):.2f} GPa, gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}",
              flush=True)
ledger.record(f"{CLAIM}: {'PASS' if out[('cofree', 'K44')] else 'FAIL'} on {len(sets['cofree'])} fresh Co-free alloys; "
              f"not gated: Co K44 {'pass' if out[('co', 'K44')] else 'fail'}, Co-free Kp "
              f"{'pass' if out[('cofree', 'Kp')] else 'fail'}, Co Kp {'pass' if out[('co', 'Kp')] else 'fail'}",
              "L0", [str(OUT), str(kst.BIN), SCRIPT], notes=f"prereg {regs[0]['id']}")
