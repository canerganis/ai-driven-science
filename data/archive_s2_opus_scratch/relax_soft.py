import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from scipy.interpolate import CubicSpline
from harness.context import context
from harness.features import parse_comp
SP = Path(__file__).resolve().parent
ctx = context()
pk = pd.read_csv(SP/"pure_k.csv")
PS = {(el, ch): CubicSpline(g.dlnV, g[ch]) for el, g in pk.groupby("el") for ch in ("K44", "Kp")}
pv = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el").vol_per_atom
g = pd.read_csv(ROOT/"data"/"binary_kgrid.csv").groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
BS = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}
s = pd.concat([pd.read_csv(ROOT/"data"/f) for f in ("scan_fcc_omat.csv", "scan_fcc_omat_rev.csv")]).drop_duplicates("comp")
ion = pd.read_csv(SP/"ion_volume.csv").set_index("comp")
rows = []
for r in s.itertuples():
    c = parse_comp(r.comp)
    if "Al" in c: continue
    if not all(((a, b), "Kp") in BS for a, b, _, _ in ctx.pairs(c)): continue
    V = r.vol_per_atom
    rec = dict(comp=r.comp, n_el=len(c), spread=r.cubic_spread)
    for ch, obs in (("K44", r.C44), ("Kp", (r.C11-r.C12)/2)):
        pure = sum(x*float(PS[(e, ch)](np.log(V/pv[e]))) for e, x in c.items())
        mix = sum(4*xa*xb*float(BS[((a, b), ch)](np.log(V/ctx.pair[(a, b)]["V"]))) for a, b, xa, xb in ctx.pairs(c))
        rec[ch+"_obs"] = obs; rec[ch+"_pure"] = pure; rec[ch+"_mix"] = mix; rec["N_"+ch] = pure+mix-obs
    rec["Erel_meV"] = 1000*(ion.E_ideal.get(r.comp, np.nan)-ion.E_rel.get(r.comp, np.nan))
    rows.append(rec)
t = pd.DataFrame(rows); t.to_csv(SP/"relax_soft.csv", index=False)
eq = t[(t.n_el == 2) & t.comp.str.contains("0.5000")]
print("50:50 binaries (transfer exact, N = relaxation softening + seed noise):", len(eq))
print(eq[["N_K44", "N_Kp"]].describe().round(2))
print("corr", eq[["N_K44", "N_Kp", "Erel_meV", "spread"]].corr().round(2))
print(eq.sort_values("N_K44")[["comp", "K44_obs", "K44_pure", "K44_mix", "N_K44", "Kp_obs", "Kp_pure", "Kp_mix", "N_Kp", "Erel_meV", "spread"]].round(1).to_string())
for lab, q in [("25:75 binaries", t[(t.n_el == 2) & ~t.comp.str.contains("0.5000")]), ("ternaries", t[t.n_el == 3]), ("quinaries", t[t.n_el == 5])]:
    print(lab, len(q), q[["N_K44", "N_Kp"]].mean().round(2).to_dict(), "rms", np.sqrt((q[["N_K44", "N_Kp"]]**2).mean()).round(2).to_dict())
