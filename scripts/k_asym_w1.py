"""W1: where the binaries are read versus how their composition dependence is represented.

python scripts/k_asym_w1.py            binaries, compositions, power, registration (stops before targets)
python scripts/k_asym_w1.py targets    targets and test, only for hypotheses already registered
Prior binary-to-multicomponent elastic models (Marker 2017 CALPHAD; Wu 2021 Eq. 5.1) model the composition dependence
of each binary (Redlich-Kister, Muggianu) but keep each binary at its own volume. Our rule uses 50:50 binaries only,
read at the alloy's Vegard volume. W1 compares the two representations on one observable and combines them. It is not
a reimplementation of Wu or Marker: their binaries sit at relaxed equilibrium volumes and their targets are equilibrium
Cij; here every arm and the target are clamped mixing curvatures (k_shear_transfer.curvatures convention), so the arm
BV-asym is an analogue of their representation, not their model (Astra design review, w1_design_astra.md).
Arms, per channel (K' primary, K44 secondary, Co and Co-free subgroups both reported):
  BV-asym  binaries at x_A = 0.25, 0.5, 0.75, each at its own (binary) Vegard volume; exact L0, L1, L2 per pair;
           Muggianu  K = sum x_a x_b [L0 + L1 (x_a - x_b) + L2 (x_a - x_b)^2]
  VV-sym   sum 4 x_a x_b K_ab(0.5; V0), V0 the alloy Vegard volume                          (our rule, unchanged)
  VV-asym  BV-asym with every binary curvature read at V0
  BV-sym   sum 4 x_a x_b K_ab(0.5; V_ab)                                                       (reported only)
Hypotheses on K', each registered only if power >= 0.8 and false pass <= 0.05; three tests, alpha 0.005 / 3:
  H1  RMSE(VV-sym)  <= 0.9 RMSE(BV-asym)   parameter-free rule against the asymmetric binary-volume representation
  H2  RMSE(VV-asym) <= 0.9 RMSE(VV-sym)    does adding the asymmetry help once the volume is right
  H3  RMSE(VV-asym) <= 0.9 RMSE(BV-asym)   the volume step alone, at equal representation degree
Design choices fixed before any target: degree 2 (three binary compositions, an exact fit; extra points at x = 1/8 and
7/8, dlnV = 0, are computed as a reported diagnostic only); targets keep every pairwise |x_a - x_b| <= 0.5 (the fitted
t range) and need no volume outside the binary grids; each target has its own SQS seed 100 + i; noise for the power
check is drawn from the rule's hm residuals, Co rows from Co rows (composition-dependent, not iid Gaussian).
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

ctx = context()
SCRIPT = str(Path(__file__))
BIN5 = ROOT / "data" / "binary_kgrid.csv"
BIN = ROOT / "data" / "binary_kgrid_asym.csv"
DIAG = ROOT / "data" / "binary_k_asym_diag.csv"
TGT = ROOT / "data" / "w1_shear_clamped.csv"
COMPS = ROOT / "data" / "w1_compositions.csv"
XS = (0.25, 0.75)
ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]  # as binary_kgrid.csv
LNV_MAX = 0.35  # targets may not need binaries beyond this, so splines never extrapolate
N_TGT, N_PERM, N_SIM = 80, 4000, 500
CH = ("Kp", "K44")
HYP = {"H1": ("VV-sym", "BV-asym"), "H2": ("VV-asym", "VV-sym"), "H3": ("VV-asym", "BV-asym")}
ALPHA = 0.005 / len(HYP)
ARMS = ("BV-asym", "VV-sym", "VV-asym", "BV-sym")
key = lambda c: ";".join(f"{e}:{v:.6f}" for e, v in sorted(c.items()))  # noqa: E731

# Same strain protocol as k_shear_transfer.py (copied, because importing that script runs its pipeline)
AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
_calc = None


def e_strained(atoms, v_atom, F):
    global _calc
    _calc = _calc or compute.calculator()
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    a.calc = _calc
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
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
    out = {}
    for name in CH[::-1]:
        em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
                                                         for el, xi in x.items()) for s in AMPS]
        c2 = np.polyfit(AMPS, em, 2)[0]
        out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
    return out


def pair_need(c):
    """ln(V0 / V_binary) for every binary composition a target reads, keyed (a, b, x_a)."""
    v0 = ctx.vegard(c)
    return {(a, b, xa): np.log(v0 / ctx.vegard({a: xa, b: 1 - xa})) for a, b, _, _ in ctx.pairs(c)
            for xa in (0.25, 0.5, 0.75)}


def from_counts(s):
    """Compositions are stored as whole atom counts of the 108-atom cell, so a reload is exact (Astra review 3)."""
    n = {e: int(k) for e, k in (kv.split(":") for kv in s.split(";"))}
    assert sum(n.values()) == 108, s
    return {e: k / 108 for e, k in n.items()}


def check_comps(cnts, sd):
    """Re-verify a stored draw: seeds unique and >= 100, constraints still hold on the exact counts."""
    assert len(cnts) == N_TGT and len(set(sd)) == len(sd) and min(sd) >= 100, "bad composition file"
    for s in cnts:
        n = {e: int(k) for e, k in (kv.split(":") for kv in s.split(";"))}
        assert 3 <= len(n) <= 5 and min(n.values()) >= 9 and 16 < max(n.values()) - min(n.values()) <= 54, s
        assert max(abs(d) for d in pair_need(from_counts(s)).values()) <= LNV_MAX, s


def draw_targets():
    if not COMPS.exists():
        rng, out, seen = np.random.default_rng(2611), [], set()
        quota = {3: 27, 4: 27, 5: 26}  # equal shares; a free draw gave 58/17/5 because the 1/12 floor rejects n = 5
        while len(out) < N_TGT:
            n = int(rng.integers(3, 6))
            if sum(s.count(":") == n for s in out) >= quota[n]:
                continue
            els = sorted(rng.choice(ELS, n, replace=False))
            cnt = np.round(rng.dirichlet([0.7] * n) * 108).astype(int)
            cnt[np.argmax(cnt)] += 108 - cnt.sum()
            # at least 9 atoms (1/12) each; spread over 16/108 (off-equiatomic) and at most 54/108 (fitted t range)
            if cnt.min() < 9 or not 16 < cnt.max() - cnt.min() <= 54:
                continue
            s = ";".join(f"{e}:{k}" for e, k in zip(els, cnt))
            if s in seen or max(abs(d) for d in pair_need(from_counts(s)).values()) > LNV_MAX:
                continue
            seen.add(s)
            out.append(s)
        pd.DataFrame({"counts": out, "seed": [100 + i for i in range(len(out))]}).to_csv(COMPS, index=False)
    f = pd.read_csv(COMPS)
    check_comps(f.counts.tolist(), f.seed.tolist())
    return [from_counts(s) for s in f.counts]


CODE = [ROOT / "harness" / f for f in ("compute.py", "context.py", "features.py", "ledger.py")]
INPUTS = [str(p) for p in (COMPS, BIN, BIN5, DIAG, ROOT / "data" / "hm_shear_clamped.csv",
                           ROOT / "data" / "scan_fcc_omat_pure.csv", *CODE)]
PREREG = {h: [e for e in ledger.entries() if e["claim"].startswith(f"W1 {h}:") and "prereg" in e["notes"]]
          for h in HYP}
for h, found in PREREG.items():  # once registered, script, data and code are checked before anything is written
    for f in ([SCRIPT, *INPUTS] if found else []):
        assert Path(f).exists(), f"{h}: {f} missing after registration"
        assert found[-1]["evidence"].get(f) == ledger.file_hash(f), f"{h}: {f} changed since registration"
comps = draw_targets()
seeds = pd.read_csv(COMPS).seed.tolist()
need = {}
for c in comps:
    for k, d in pair_need(c).items():
        need.setdefault(k, []).append(d)

# 1. off-equiatomic binaries on the ln V grid around each binary's own Vegard volume, as wide as the targets need
done = set(map(tuple, pd.read_csv(BIN)[["pair", "xA", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
for (a, b, xa), ds in sorted(need.items()):
    if xa == 0.5:
        continue
    lo, hi = min(min(ds), 0.0) - 0.1, max(max(ds), 0.0) + 0.1
    grid = [d for d in GRID if lo <= d <= hi]
    for seed in (0, 1, 2):
        alloy = compute.solid_solution({a: xa, b: 1 - xa}, "fcc", reps=3, seed=seed)
        x = compute.actual_fractions(alloy)
        for d in grid:
            if (f"{a}-{b}", str(xa), str(seed), str(d)) in done:
                continue
            v = ctx.vegard({a: xa, b: 1 - xa}) * np.exp(d)
            r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "dlnV": d, "V": v,
                 **curvatures(alloy, x, v)}
            pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False, float_format="%.10g")
    print("binary", a, b, xa, flush=True)

# degree diagnostic (reported only): x = 1/8, 7/8 at the binary's own Vegard volume
done = set(map(tuple, pd.read_csv(DIAG)[["pair", "xA", "seed"]].astype(str).values)) if DIAG.exists() else set()
for a, b in sorted({(a, b) for a, b, _ in need}):
    for xa in (0.125, 0.875):
        for seed in (0, 1, 2):
            if (f"{a}-{b}", str(xa), str(seed)) in done:
                continue
            alloy = compute.solid_solution({a: xa, b: 1 - xa}, "fcc", reps=3, seed=seed)
            x = compute.actual_fractions(alloy)
            v = ctx.vegard(x)  # the cell's actual composition (14/108, 94/108), so the diagnostic sees no volume shift
            r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "V": v, **curvatures(alloy, x, v)}
            pd.DataFrame([r]).to_csv(DIAG, mode="a", header=not DIAG.exists(), index=False, float_format="%.10g")
print("diagnostic binaries done", flush=True)

# splines in absolute ln V, x = 0.25, 0.75 (this script) and 0.5 (binary_kgrid.csv); no extrapolation allowed
SPL, RANGE = {}, {}
g = pd.read_csv(BIN).groupby(["pair", "xA", "dlnV"])[["V", *CH]].mean().reset_index()
g5 = pd.read_csv(BIN5).groupby(["pair", "dlnV"])[["V", *CH]].mean().reset_index().assign(xA=0.5)
for (pair, xa), s in pd.concat([g, g5]).groupby(["pair", "xA"]):
    lv = np.log(s.V.values)
    RANGE[(tuple(pair.split("-")), xa)] = (lv.min(), lv.max())
    for ch in CH:
        SPL[(tuple(pair.split("-")), xa, ch)] = CubicSpline(lv, s[ch].values, extrapolate=False)


def k_at(a, b, x, ch, lnv):
    lo, hi = RANGE[((a, b), x)]
    assert lo - 1e-9 <= lnv <= hi + 1e-9, ("extrapolation", a, b, x, lnv, lo, hi)
    return float(SPL[((a, b), x, ch)](lnv))


def rk(k25, k50, k75):
    """Exact L0, L1, L2 from K(x) = x(1-x)[L0 + L1 t + L2 t^2], t = 2x - 1, at x = 0.25, 0.5, 0.75."""
    y = np.array([k25 / (3 / 16), k50 / 0.25, k75 / (3 / 16)])
    return np.linalg.solve(np.array([[1, -0.5, 0.25], [1, 0, 0], [1, 0.5, 0.25]]), y)


def predict(c, ch, arm):
    vol, rep = arm.split("-")
    v0, tot = ctx.vegard(c), 0.0
    for a, b, xa, xb in ctx.pairs(c):
        at = lambda x: np.log(v0) if vol == "VV" else np.log(ctx.vegard({a: x, b: 1 - x}))  # noqa: E731
        if rep == "sym":
            tot += 4 * xa * xb * k_at(a, b, 0.5, ch, at(0.5))
        else:
            L = rk(*(k_at(a, b, x, ch, at(x)) for x in (0.25, 0.5, 0.75)))
            t = xa - xb
            tot += xa * xb * (L[0] + L[1] * t + L[2] * t * t)
    return tot


P = {ch: {arm: np.array([predict(c, ch, arm) for c in comps]) for arm in ARMS} for ch in CH}
for ch in CH:  # the four arms must really differ (the first draft's endswith("sym") made asym equal sym)
    for i, a1 in enumerate(ARMS):
        for a2 in ARMS[i + 1:]:
            assert np.abs(P[ch][a1] - P[ch][a2]).max() > 1e-6, (ch, a1, a2)

# degree diagnostic, reported only: degree-2 RK at the binary's own volume against x = 1/8, 7/8 (actual fractions)
dg = pd.read_csv(DIAG).groupby(["pair", "xA"])[["xA_actual", "V", *CH]].mean().reset_index()
for ch in CH:
    err = []
    for _, r in dg.iterrows():
        a, b = r.pair.split("-")
        x = r.xA_actual
        L = rk(*(k_at(a, b, xx, ch, np.log(ctx.vegard({a: xx, b: 1 - xx}))) for xx in (0.25, 0.5, 0.75)))
        err.append(x * (1 - x) * (L[0] + L[1] * (2 * x - 1) + L[2] * (2 * x - 1) ** 2) - r[ch])
    print(f"degree diagnostic {ch}: n {len(err)}, rms {np.sqrt(np.mean(np.square(err))):.3f}, "
          f"max {np.max(np.abs(err)):.3f} GPa (RK2 at x ~ 1/8, 7/8, own volume)", flush=True)

# 2. power with composition-dependent noise, then registration.
# Noise = systematic part + scatter. Calibration: the rule's residual on the seen hm targets (SQS seed 0), predicted
# from binaries of seeds 1-2 only, so inputs and targets share no seed. The systematic part is an OLS fit of that
# residual on target features (Co and Cu fractions, component count, size mismatch); the scatter is a bootstrap of
# leave-one-out residuals without sign flips, drawn separately for Co and Co-free rows (their scatter differs, 2.2 vs
# 1.4 GPa, review 3), so neither the Co bias nor the Co heteroscedasticity is averaged away.
hm = pd.read_csv(ROOT / "data" / "hm_shear_clamped.csv")
hmc = [parse_comp(s) for s in hm.comp]
b12 = pd.read_csv(BIN5)
b12 = b12[b12.seed.isin([1, 2])].groupby(["pair", "dlnV"])[["V", "Kp"]].mean().reset_index()
S12 = {tuple(p.split("-")): CubicSpline(np.log(s.V.values), s.Kp.values) for p, s in b12.groupby("pair")}
res_hm = hm.Kp.values - np.array([sum(4 * xa * xb * float(S12[(a, b)](np.log(ctx.vegard(c))))
                                       for a, b, xa, xb in ctx.pairs(c)) for c in hmc])


def feats(c):
    lv = np.array([np.log(ctx.pure[e]["V"]) for e in c])
    x = np.array(list(c.values()))
    return [1.0, c.get("Co", 0.0), c.get("Cu", 0.0), len(c), float(np.sqrt(x @ (lv - x @ lv) ** 2))]


Xh = np.array([feats(c) for c in hmc])
beta = np.linalg.lstsq(Xh, res_hm, rcond=None)[0]
H = Xh @ np.linalg.pinv(Xh)
scatter = (res_hm - Xh @ beta) / (1 - np.diag(H))  # leave-one-out residuals
co_hm = np.array(["Co" in c for c in hmc])
bias = np.array([feats(c) for c in comps]) @ beta
co = np.array(["Co" in c for c in comps])
print(f"noise model: hm residual rms {np.sqrt(np.mean(res_hm**2)):.3f} (seeds 1-2 inputs), systematic rms "
      f"{np.sqrt(np.mean((Xh @ beta)**2)):.3f}, LOO scatter rms Co {np.sqrt(np.mean(scatter[co_hm]**2)):.3f} / Co-free "
      f"{np.sqrt(np.mean(scatter[~co_hm]**2)):.3f}, beta {np.round(beta, 3)}",
      flush=True)


def signflip(y, new, old, rng):
    d = (y - old) ** 2 - (y - new) ** 2
    gain = 1 - np.sqrt(np.mean((y - new) ** 2)) / np.sqrt(np.mean((y - old) ** 2))
    flips = rng.choice([-1.0, 1.0], (N_PERM, len(d)))
    p = (np.sum((flips * d).mean(1) >= d.mean()) + 1) / (N_PERM + 1)
    return gain >= 0.10 and p < ALPHA, float(gain), float(p)


def noise(rng):
    e = bias.copy()
    for flag in (True, False):
        e[co == flag] += rng.choice(scatter[co_hm == flag], (co == flag).sum())
    return e


def power(new, old):
    rng = np.random.default_rng(7)
    run = lambda truth: np.mean([signflip(truth + noise(rng), P["Kp"][new], P["Kp"][old], rng)[0]  # noqa: E731
                                 for _ in range(N_SIM)])
    pw, fp = run(P["Kp"][new]), run(P["Kp"][old])
    pool_mean = np.where(co, scatter[co_hm].mean(), scatter[~co_hm].mean())
    fp_mid = run(0.5 * (P["Kp"][new] + P["Kp"][old]) - bias - pool_mean)  # equal expected error, exactly centred
    return {"power": round(float(pw), 3), "false_pass": round(float(max(fp, fp_mid)), 3), "n_sims": N_SIM,
            "power_se": round(float(np.sqrt(pw * (1 - pw) / N_SIM)), 3)}


regs = {}
for h, (new, old) in HYP.items():
    tag = f"W1 {h}:"
    if PREREG[h]:
        regs[h] = PREREG[h][-1]
        continue
    if any(e["claim"].startswith(f"Design note, {tag}") for e in ledger.entries()):
        continue
    pw = power(new, old)
    d = P["Kp"][new] - P["Kp"][old]
    print(f"{h}: rms(new - old) {np.sqrt(np.mean(d**2)):.2f} GPa, hm residual rms {np.sqrt(np.mean(res_hm**2)):.2f}, "
          f"{pw}", flush=True)
    claim = (f"{tag} on {len(comps)} fresh off-equiatomic fcc alloys (3-5 of {''.join(ELS)}), clamped mixing K' "
             f"RMSE({new}) <= 0.9 RMSE({old}) and paired sign-flip p < {ALPHA:.4f}; MACE medium-omat-0, per-target "
             f"SQS seeds 100-{99 + len(comps)}, targets computed after registration")
    try:
        regs[h] = ledger.register(claim, SCRIPT, pw, notes="literature gap Wu 2021 / Marker 2017 (literature.jsonl "
                                  "line 65); design reviewed by Astra (.orchestra/audits/w1_design*_astra.md)",
                                  inputs=tuple(INPUTS))
        print("registered", h, regs[h]["id"], flush=True)
    except ValueError as err:
        ledger.record(f"Design note, {tag} not registered: {err}", "L0", [SCRIPT, str(BIN)],
                      notes=f"design; effect below detectability at n {len(comps)}")
        print(h, "not registered:", err, flush=True)

if "targets" not in sys.argv[1:]:
    sys.exit(0)
if not regs:
    sys.exit("no hypothesis registered; no target computed")

# 3. targets, each with its own seed
done = set()
if TGT.exists():
    old = pd.read_csv(TGT)
    want = {key(c): s for c, s in zip(comps, seeds)}
    assert old.comp.is_unique and all(want.get(k) == s for k, s in zip(old.comp, old.seed)), "target rows do not match"
    done = set(old.comp)
for c, seed in zip(comps, seeds):
    if key(c) in done:
        continue
    alloy = compute.solid_solution(c, "fcc", reps=3, seed=seed)
    x = compute.actual_fractions(alloy)
    assert max(abs(x[e] - c[e]) for e in c) < 1e-6, (key(c), x)
    r = {"comp": key(c), "seed": seed, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False, float_format="%.10g")
print("targets done", flush=True)

# 4. test, matched by composition key
t = pd.read_csv(TGT).set_index("comp").loc[[key(c) for c in comps]]
y = {ch: t[ch].values for ch in CH}
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
for ch in CH:
    for name, m in (("all", np.ones(len(comps), bool)), ("Co", co), ("Co-free", ~co)):
        print(ch, name, int(m.sum()), {arm: round(rm((y[ch] - P[ch][arm])[m]), 3) for arm in ARMS}, flush=True)
rng = np.random.default_rng(11)
for h, reg in regs.items():
    new, old = HYP[h]
    ok, gain, p = signflip(y["Kp"], P["Kp"][new], P["Kp"][old], rng)
    k44 = signflip(y["K44"], P["K44"][new], P["K44"][old], rng)
    print(f"{h}: gain {gain:.3f}, p {p:.1e} -> {'PASS' if ok else 'FAIL'}; K44 (secondary) gain {k44[1]:.3f}, "
          f"p {k44[2]:.1e}", flush=True)
    ledger.record(f"W1 {h} result: {'PASS' if ok else 'FAIL'}, K' RMSE {new} {rm(y['Kp'] - P['Kp'][new]):.3f} vs "
                  f"{old} {rm(y['Kp'] - P['Kp'][old]):.3f} GPa, gain {gain:.3f}, p {p:.1e}; K44 gain {k44[1]:.3f}",
                  "L0", [str(BIN), str(DIAG), str(TGT), str(COMPS), SCRIPT],
                  notes=f"prereg {reg['id']}; independent audit and ledger.verdict pending")
