"""Ideal-lattice equilibrium volume V_c (seed-0 cell, affine, no ionic relaxation) for hm_fresh n_el>=3 alloys.
No relaxation is done: the relaxed volumes stay unseen."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd, torch
torch.set_num_threads(4)
from mace.calculators import mace_mp
from harness import compute
from harness.features import parse_comp
calc = mace_mp(model="medium-omat-0", device="cpu", default_dtype="float64")
pv = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el").vol_per_atom
h = pd.read_csv(ROOT/"data"/"hm_fresh_rows_fixed.csv"); h = h[h.n_el >= 3]
out = Path(sys.argv[1]); done = set(pd.read_csv(out).comp) if out.exists() else set()
S = np.array([-0.04, -0.02, 0.0, 0.02, 0.04])
for s in h.comp_actual:
    if s in done: continue
    a0 = compute.solid_solution(parse_comp(s), "fcc", 3, 0); x = compute.actual_fractions(a0)
    v0 = sum(x[e]*pv[e] for e in x)
    E = []
    for d in S:
        a = a0.copy(); v = v0*np.exp(d)
        a.set_cell(a.cell*(v*len(a)/a.get_volume())**(1/3), scale_atoms=True); a.calc = calc
        E.append(a.get_potential_energy()/len(a))
    c3, c2, c1, c0 = np.polyfit(S, E, 3)
    r = np.roots([3*c3, 2*c2, c1]); r = r[np.isreal(r)].real; u = r[np.argmin(abs(r))]
    pd.DataFrame([dict(comp=s, n_el=len(x), V0=v0, ln_Vc_V0=u, curv=2*c2+6*c3*u)]).to_csv(out, mode="a", header=not out.exists(), index=False)
print("done")
