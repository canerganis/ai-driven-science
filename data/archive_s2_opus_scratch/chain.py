"""Relaxed C44, C' of seen scan alloys from pures + binaries only:
C_pred = sum x_i K_i(V*) + sum 4 x_i x_j [K_ij(V*) - N_ij], N_ij = relaxation softening of the 50:50 binary
(clamped prediction at its relaxed volume minus its relaxed scan value). V* = observed relaxed volume (isolates the
elastic step). Baselines: Voigt rule of mixtures of pure relaxed constants, clamped-only (N = 0)."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from scipy.interpolate import CubicSpline
from harness.context import context
from harness.features import parse_comp
SP = Path(__file__).resolve().parent
ctx = context()
pk = pd.concat([pd.read_csv(SP/"pure_k.csv"), pd.read_csv(SP/"pure_k_ext.csv")]).sort_values(["el", "dlnV"])
PS = {(el, ch): CubicSpline(g.dlnV, g[ch]) for el, g in pk.groupby("el") for ch in ("K44", "Kp")}
pp = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el"); pv = pp.vol_per_atom
g = pd.read_csv(ROOT/"data"/"binary_kgrid.csv").groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
BS = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}
s = pd.concat([pd.read_csv(ROOT/"data"/f) for f in ("scan_fcc_omat.csv", "scan_fcc_omat_rev.csv")]).drop_duplicates("comp")
s = s[~s.comp.str.contains("Al")]
OBS = {"K44": lambda r: r.C44, "Kp": lambda r: (r.C11-r.C12)/2}
def clamped(c, V, ch):
    return (sum(x*float(PS[(e, ch)](np.log(V/pv[e]))) for e, x in c.items()),
            sum(4*xa*xb*float(BS[((a, b), ch)](np.log(V/ctx.pair[(a, b)]["V"]))) for a, b, xa, xb in ctx.pairs(c)))
N = {}
for r in s.itertuples():
    c = parse_comp(r.comp)
    if len(c) == 2 and all(abs(x-0.5) < 1e-3 for x in c.values()):
        for ch in OBS:
            p, m = clamped(c, r.vol_per_atom, ch); N[(tuple(sorted(c)), ch)] = p+m-OBS[ch](r)
rows = []
for r in s.itertuples():
    c = parse_comp(r.comp)
    if len(c) == 2 and all(abs(x-0.5) < 1e-3 for x in c.values()): continue
    if not all(((a, b), "Kp") in BS for a, b, _, _ in ctx.pairs(c)): continue
    rec = dict(comp=r.comp, n_el=len(c))
    for ch in OBS:
        p, m = clamped(c, r.vol_per_atom, ch)
        nrel = sum(4*xa*xb*N[((a, b), ch)] for a, b, xa, xb in ctx.pairs(c))
        rom = sum(x*(pp.loc[e, "C44"] if ch == "K44" else (pp.loc[e, "C11"]-pp.loc[e, "C12"])/2) for e, x in c.items())
        rec.update({ch+"_obs": OBS[ch](r), ch+"_rom": rom, ch+"_clamped": p+m, ch+"_chain": p+m-nrel, ch+"_N": nrel})
    rows.append(rec)
t = pd.DataFrame(rows); t.to_csv(SP/"chain.csv", index=False)
rm = lambda e: float(np.sqrt(np.mean(np.square(e))))
for lab, q in [("25:75 binaries", t[t.n_el == 2]), ("ternaries", t[t.n_el == 3]), ("quinaries", t[t.n_el == 5])]:
    for ch in OBS:
        y = q[ch+"_obs"]
        print(f"{lab:15s} {ch:3s} n {len(q):2d}  RMSE rom {rm(y-q[ch+'_rom']):6.2f}  clamped {rm(y-q[ch+'_clamped']):6.2f}  "
              f"chain {rm(y-q[ch+'_chain']):6.2f}  mean(obs-chain) {np.mean(y-q[ch+'_chain']):+6.2f}  sd obs {y.std():6.2f}")
