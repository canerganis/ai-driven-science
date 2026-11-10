import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from harness import compute
from harness.features import parse_comp
SP = Path(__file__).resolve().parent
G = 160.21766208
d = pd.concat([pd.read_csv(SP/"ion_volume.csv"), pd.read_csv(SP/"ion_volume_rest.csv")]).drop_duplicates("comp")
pv = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el").vol_per_atom
def v0act(c):
    x = compute.actual_fractions(compute.solid_solution(parse_comp(c), "fcc", 3, 0)); return sum(x[e]*pv[e] for e in x)
d["V0"] = d.comp.map(v0act)
d["tot"] = np.log(d.V/d.V0); d["ideal"] = d.tot - d.dlnV_ion
d["Al"] = d.comp.str.contains("Al")
h = pd.read_csv(ROOT/"data"/"h1_ev_rows_fixed.csv").set_index("comp")
d["p"] = [h.dE_dlnV.get(c, np.nan) for c in d.comp]/(d.B/G*d.V)
def fit(s, lab):
    k = np.sum(s.ideal*s.dlnV_ion)/np.sum(s.ideal**2); r = np.corrcoef(s.ideal, s.dlnV_ion)[0, 1]
    rm = lambda e: np.sqrt(np.mean(e**2))
    print(f"{lab:28s} n {len(s):3d}  lambda {-k:.3f}  r {r:+.2f}  rms ion {rm(s.dlnV_ion)*100:.2f}%  resid {rm(s.dlnV_ion-k*s.ideal)*100:.2f}%  "
          f"rms tot {rm(s.tot)*100:.2f}  rms ideal {rm(s.ideal)*100:.2f}")
    return k
for lab, s in [("all", d), ("no Al", d[~d.Al]), ("binary no Al", d[(d.n_el == 2) & ~d.Al]),
               ("multi no Al", d[(d.n_el > 2) & ~d.Al]), ("n3", d[(d.n_el == 3) & ~d.Al]), ("n4+", d[(d.n_el >= 4) & ~d.Al]),
               ("Al", d[d.Al]), ("spread<0.1 no Al", d[(d.spread < 0.1) & ~d.Al])]:
    if len(s) > 2: fit(s, lab)
kb = fit(d[(d.n_el == 2) & ~d.Al], "binary (train)")
m = d[(d.n_el > 2) & ~d.Al]
pred = kb*m.ideal
print("multi with binary lambda: rmse", np.sqrt(np.mean((m.dlnV_ion-pred)**2))*100, "vs zero", np.sqrt(np.mean(m.dlnV_ion**2))*100)
d.to_csv(SP/"ion_all.csv", index=False)
print(d[d.n_el > 2].sort_values("ideal")[["comp", "tot", "ideal", "dlnV_ion", "spread"]].assign(**{c: lambda x, c=c: x[c]*100 for c in ["tot", "ideal", "dlnV_ion"]}).round(2).to_string())
