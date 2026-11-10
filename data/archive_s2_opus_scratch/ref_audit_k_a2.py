"""Same reference-state audit for the shear-curvature L2 (697c2d6d75): targets h3_shear_clamped, hm_shear_clamped.
own-ref: G_ij = K_ij(V_ij) + mean_k [K_k(V_ij) - K_k(V_k)]; pred = sum 4 x_i x_j G_ij - sum x_i [K_i(V0) - K_i(V_i)]"""
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
pv = {el: ctx.pure[el]["V"] for el in ctx.pure}
dk = lambda el, v, ch: float(PS[(el, ch)](np.log(v/pv[el])) - PS[(el, ch)](0.0))
g = pd.read_csv(ROOT/"data"/"binary_kgrid.csv").groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
BS = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}
rm = lambda x: float(np.sqrt(np.mean(np.square(x))))
def signflip(y, a, b, n=20000):
    d = (y-b)**2-(y-a)**2; rng = np.random.default_rng(0)
    null = np.array([np.mean(d*rng.choice([-1, 1], len(d))) for _ in range(n)]); return (np.sum(null >= d.mean())+1)/(n+1)
for f in ("a2_shear_clamped.csv",):
    t = pd.read_csv(ROOT/"data"/f); t["n_el"] = t.comp.str.count(":"); t = t[(t.n_el == 3) & ~t.comp.str.contains("Al")]
    for ch in ("Kp", "K44"):
        rows = []
        for r in t.itertuples():
            c = parse_comp(r.comp)
            if not all(((a, b), ch) in BS for a, b, _, _ in ctx.pairs(c)): continue
            v0 = ctx.vegard(c)
            pair = sum(4*xa*xb*float(BS[((a, b), ch)](0.0)) for a, b, xa, xb in ctx.pairs(c))
            rule = sum(4*xa*xb*float(BS[((a, b), ch)](np.log(v0/ctx.pair[(a, b)]["V"]))) for a, b, xa, xb in ctx.pairs(c))
            Gij = lambda a, b: float(BS[((a, b), ch)](0.0)) + 0.5*(dk(a, ctx.pair[(a, b)]["V"], ch) + dk(b, ctx.pair[(a, b)]["V"], ch))
            own = sum(4*xa*xb*Gij(a, b) for a, b, xa, xb in ctx.pairs(c)) - sum(x*dk(el, v0, ch) for el, x in c.items())
            rows.append((getattr(r, ch), pair, rule, own))
        a = np.array(rows); y = a[:, 0]
        print(f"{f:22s} {ch:3s} n {len(a):3d}  RMSE GPa: pair-at-V_ij {rm(y-a[:,1]):5.2f}  rule {rm(y-a[:,2]):5.2f}  own-volume Muggianu {rm(y-a[:,3]):5.2f}"
              f"  | rule vs own: gain {1-rm(y-a[:,2])/rm(y-a[:,3]):+.2f} p {signflip(y, a[:,2], a[:,3]):.1e}  corr {np.corrcoef(a[:,2], a[:,3])[0,1]:.3f}")
