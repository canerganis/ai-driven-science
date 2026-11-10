"""Fresh test of the shared-floor picture of shear transfer (LESSONS 18; Opus, swarm S2 k44 front).

python scripts/k_aniso_fresh.py
Seen so far (k44_cofree Co set, blind by file timestamp only): the residual of the volume-transfer pair rule is the
same in both shears, so the anisotropy A = K44 - K' transfers as sum 4 x_i x_j A_ij(V0) and K44 transfers with k ~1
once e' = K' - rule' is a covariate. Here both are pre-registered in the ledger on 150 new random alloys (half with
Co >= 15%), drawn with a new seed and never computed. Targets use SQS seed 100: binaries use seeds 0-2, and compute.py:56
makes the site permutation depend only on (seed, n), so a shared seed leaks configuration noise (S2 audit, ledger
withdrawal of 9cfc8edaf0). Plain K44 per Co set is reported, not gated.
PASS needs all three: (1) A rule: RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005; (2) corr(e44, e') >= 0.5;
(3) joint fit K44 - pair44 = k T44 + b e': k and b both in [0.7, 1.3].
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

ctx, curvatures, test = kst.ctx, kst.curvatures, kst.test
g = kst.g.copy()
g["A"] = g.K44 - g.Kp
spl = {(tuple(k.split("-")), ch): kst.CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp", "A")}
OUT = ROOT / "data" / "k_aniso_s100_clamped.csv"
SCRIPT = str(Path(__file__))
CLAIM = "Shared shear floor, disjoint seeds"
ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
N = 108

seen = set()
for f in ("a2_shear_clamped", "h3_shear_clamped", "hm_shear_clamped", "k44_cofree_clamped"):
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
        if (not with_co or c["Co"] >= 0.15) and s not in seen:
            seen.add(s)
            return s, c


rng = np.random.default_rng(20261102)
comps = [draw(rng, i % 2 == 1) for i in range(150)]


def pr(c, ch, at):
    v = ctx.vegard(c)
    return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"]) if at else 0.0))
               for a, b, xa, xb in ctx.pairs(c))


P = {ch: (np.array([pr(c, ch, 1) for _, c in comps]), np.array([pr(c, ch, 0) for _, c in comps])) for ch in ("K44", "Kp", "A")}


def judge(y44, yp):
    okA, gain, p = test(y44 - yp, *P["A"])
    e44, ep = y44 - P["K44"][0], yp - P["Kp"][0]
    r = float(np.corrcoef(e44, ep)[0, 1])
    k, b = np.linalg.lstsq(np.c_[P["K44"][0] - P["K44"][1], ep], y44 - P["K44"][1], rcond=None)[0]
    return okA and r >= 0.5 and 0.7 <= k <= 1.3 and 0.7 <= b <= 1.3, gain, p, r, float(k), float(b)


# realistic noise, from the rows already computed (seen): K' residual of the rule, and the A residual on top of it
seenrows = pd.concat([pd.read_csv(ROOT / "data" / f"{f}.csv") for f in ("h3_shear_clamped", "hm_shear_clamped", "k44_cofree_clamped")])
sc = [parse_comp(s) for s in seenrows.comp]
ep_s = seenrows.Kp.values - np.array([pr(c, "Kp", 1) for c in sc])
eA_s = (seenrows.K44 - seenrows.Kp).values - np.array([pr(c, "A", 1) for c in sc])
SP, SA = 1.2 * float(np.std(ep_s)), 1.2 * float(np.std(eA_s))  # x1.2: seen rows carry the seed leak
regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
if not regs:
    r2 = np.random.default_rng(4)

    def sim(truth):
        hits = []
        for i in range(300):
            ep = r2.normal(0, SP, len(comps))
            yp = P["Kp"][0] + ep
            y44 = (P["K44"][0] if truth == 0 else P["K44"][1]) + ep + r2.normal(0, SA, len(comps))
            if truth == 1:
                yp = P["Kp"][1] + ep
            hits.append(judge(y44, yp)[0])
        return float(np.mean(hits))

    power, fp = sim(0), sim(1)
    print(f"n {len(comps)}, sigma K' {SP:.2f}, sigma A {SA:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
    reg = ledger.register(f"{CLAIM}: in clamped random fcc alloys the volume-transfer pair rule misses a part common to "
                          f"K44 and K'; PASS if on {len(comps)} new random alloys (half Co >= 15%) (1) A = K44 - K' rule "
                          f"sum 4 x_i x_j A_ij(V0) has RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005, (2) "
                          f"corr(e44, e') >= 0.5, (3) joint fit K44 - pair44 = k T44 + b e' gives k, b in [0.7, 1.3]",
                          SCRIPT, {"power": power, "false_pass": fp},
                          notes="Opus swarm S2 k44 front; seen confirmation on k44_cofree Co set (LESSONS 18)")
    print("registered", reg["id"], flush=True)
    regs = [reg]

done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for s, c in comps:
    if s in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=100)
    x = compute.actual_fractions(alloy)
    r = {"comp": s, "n_el": len(c), "co": c.get("Co", 0.0), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
print("aniso targets done", flush=True)

t = pd.read_csv(OUT).set_index("comp").loc[[s for s, _ in comps]]
ok, gain, p, r, k, b = judge(t.K44.values, t.Kp.values)
print(f"A rule gain {gain:.2f}, p {p:.1e}; corr(e44, e') {r:.2f}; joint k {k:.2f}, b {b:.2f} -> {'PASS' if ok else 'FAIL'}",
      flush=True)
for lab, m in (("Co-free", t.co.values == 0), ("Co", t.co.values > 0)):
    T, Y = (P["K44"][0] - P["K44"][1])[m], (t.K44.values - P["K44"][1])[m]
    _, gn, pp = test(t.K44.values[m], P["K44"][0][m], P["K44"][1][m])
    print(f"not gated, plain K44 {lab} (n {m.sum()}): gain {gn:.2f}, p {pp:.1e}, k {T @ Y / (T @ T):.2f}", flush=True)
ledger.record(f"{CLAIM}: {'PASS' if ok else 'FAIL'} on {len(comps)} new alloys (A gain {gain:.2f}, p {p:.1e}, corr {r:.2f}, "
              f"k {k:.2f}, b {b:.2f})", "L0", [str(OUT), str(kst.BIN), SCRIPT], notes=f"prereg {regs[0]['id']}")
