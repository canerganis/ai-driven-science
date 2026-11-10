import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar
from harness import compute
from harness.features import parse_comp
SP = Path(__file__).resolve().parent
G = 160.21766208
files = [SP/"ion_volume.csv"] + ([SP/"ion_volume_rest.csv"] if (SP/"ion_volume_rest.csv").exists() else [])
d = pd.concat([pd.read_csv(f) for f in files]).drop_duplicates("comp")
pe = pd.read_csv(SP/"pure_ev.csv"); pp = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el")
S = {el: CubicSpline(np.log(g.V), g.E) for el, g in pe.groupby("el")}
rows = []
for r in d.itertuples():
    x = compute.actual_fractions(compute.solid_solution(parse_comp(r.comp), "fcc", 3, 0))
    v0 = sum(x[e]*pp.loc[e, "vol_per_atom"] for e in x)
    f = lambda u: sum(x[e]*S[e](u) for e in x)
    u = minimize_scalar(f, bounds=(np.log(v0)-0.2, np.log(v0)+0.2), method="bounded", options={"xatol": 1e-7}).x
    K = np.array([pp.loc[e, "B"] for e in x]); M = np.array([pp.loc[e, "G"] for e in x]); c = np.array([x[e] for e in x])
    rows.append(dict(comp=r.comp, n_el=len(x), eos=u-np.log(v0), tot=np.log(r.V/v0), ion=r.dlnV_ion, spread=r.spread,
                     Al="Al" in x, KoverKmu=(c@K)/((c@K)+4/3*(c@M)), Erel=r.E_ideal-r.E_rel, BV=r.B/G*r.V))
t = pd.DataFrame(rows); t["ideal"] = t.tot-t.ion; t["chem"] = t.ideal-t.eos
t.to_csv(SP/"levin.csv", index=False)
for lab, s in [("all no Al", t[~t.Al]), ("binary no Al", t[(t.n_el == 2) & ~t.Al]), ("multi no Al", t[(t.n_el > 2) & ~t.Al])]:
    if len(s) < 4: continue
    X = np.c_[s.eos, s.chem]; co = np.linalg.lstsq(X, s.ion, rcond=None)[0]; pr = X@co
    print(f"{lab:14s} n {len(s)} ion = {co[0]:+.3f} eos {co[1]:+.3f} chem; r {np.corrcoef(pr, s.ion)[0,1]:.3f} rmse {np.sqrt(np.mean((s.ion-pr)**2))*100:.3f}% "
          f"rms ion {np.sqrt(np.mean(s.ion**2))*100:.3f}%  corr(eos,ion) {np.corrcoef(s.eos,s.ion)[0,1]:+.2f} corr(chem,ion) {np.corrcoef(s.chem,s.ion)[0,1]:+.2f}  mean K/(K+4mu/3) {s.KoverKmu.mean():.2f}")
print((t[~t.Al].sort_values("eos")[["comp", "eos", "chem", "ideal", "ion", "tot"]].set_index("comp")*100).round(2).to_string())
