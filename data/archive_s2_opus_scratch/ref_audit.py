"""Is the volume-transfer gain a reference-state effect? Compare, on clamped E_mix(V0) of multicomponent alloys:
 pair    : sum 4 x_i x_j E_ij(V_ij)                     (L2 baseline, references at the common volume)
 transfer: sum 4 x_i x_j E_ij(V0) exact, from binary_vgrid splines (k_direct, no parameter)
 own-ref : Muggianu of binary formation energies (pures at their own volumes), converted back:
           sum 4 x_i x_j F_ij - sum x_i [e_i(V0) - e_i(V_i)],  F_ij = E_ij(V_ij) + mean_k [e_k(V_ij) - e_k(V_k)]
"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from scipy.interpolate import CubicSpline
from harness.context import context
from harness.features import parse_comp
SP = Path(__file__).resolve().parent
ctx = context()
pe = pd.read_csv(SP/"pure_ev.csv")
ES = {el: CubicSpline(np.log(g.V), g.E) for el, g in pe.groupby("el")}
pv = {el: ctx.pure[el]["V"] for el in ctx.pure}
e = lambda el, v: float(ES[el](np.log(v)))
de = lambda el, v: e(el, v) - e(el, pv[el])      # cost of putting pure el at volume v
gv = pd.read_csv(ROOT/"data"/"binary_vgrid.csv").groupby(["pair", "dlnV"]).E_mix.mean().reset_index()
VS = {tuple(k.split("-")): CubicSpline(s.dlnV, s.E_mix) for k, s in gv.groupby("pair")}
F = {k: p["E"] + 0.5*(de(k[0], p["V"]) + de(k[1], p["V"])) for k, p in ctx.pair.items()}
rm = lambda x: float(np.sqrt(np.mean(np.square(x))))*1000
for f in ("h1_ev_rows_fixed.csv", "h3_fresh_rows_fixed.csv", "hm_fresh_rows_fixed.csv"):
    df = pd.read_csv(ROOT/"data"/f); df = df[df.n_el >= 3]
    rows = []
    for r in df.itertuples():
        c = parse_comp(r.comp_actual)
        if not all((a, b) in VS for a, b, _, _ in ctx.pairs(c)): continue
        v0 = ctx.vegard(c)
        pair = sum(4*xa*xb*ctx.pair[(a, b)]["E"] for a, b, xa, xb in ctx.pairs(c))
        tr = sum(4*xa*xb*float(VS[(a, b)](np.log(v0/ctx.pair[(a, b)]["V"]))) for a, b, xa, xb in ctx.pairs(c))
        own = sum(4*xa*xb*F[(a, b)] for a, b, xa, xb in ctx.pairs(c)) - sum(x*de(el, v0) for el, x in c.items())
        rows.append((r.E_mix, pair, tr, own))
    a = np.array(rows); y = a[:, 0]
    print(f"{f:26s} n {len(a):3d}  RMSE meV: pair-at-V_ij {rm(y-a[:,1]):5.1f}  exact transfer {rm(y-a[:,2]):5.1f}  "
          f"own-volume Muggianu {rm(y-a[:,3]):5.1f}   corr(transfer, own) {np.corrcoef(a[:,2], a[:,3])[0,1]:.3f}")
