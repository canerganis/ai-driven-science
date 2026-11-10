"""Exploration (seen scan rows): ideal-site equilibrium volume V_c vs relaxed volume V*, and E_relax at V*."""
import sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd
from mace.calculators import mace_mp
from harness import compute
from harness.features import parse_comp
calc = mace_mp(model="medium-omat-0", device="cpu", default_dtype="float64")
scan = pd.concat([pd.read_csv(ROOT/"data"/f) for f in ("scan_fcc_omat.csv","scan_fcc_omat_rev.csv")]).drop_duplicates("comp")
em = pd.read_csv(ROOT/"data"/"scan_fcc_omat_emix.csv").set_index("comp")
out = Path(sys.argv[1])
S = np.array([-0.06,-0.04,-0.02,0.0,0.02])  # dlnV around V*
rows=[]
t0=time.time()
for r in scan.itertuples():
    if r.comp not in em.index: continue
    a0 = compute.solid_solution(parse_comp(r.comp), "fcc", 3, 0)
    E=[]
    for d in S:
        a=a0.copy(); v=r.vol_per_atom*np.exp(d)
        a.set_cell(a.cell*(v*len(a)/a.get_volume())**(1/3), scale_atoms=True); a.calc=calc
        E.append(a.get_potential_energy()/len(a))
    c3,c2,c1,c0=np.polyfit(S,E,3)
    # minimum of cubic near 0
    roots=np.roots([3*c3,2*c2,c1]); roots=roots[np.isreal(roots)].real
    u=roots[np.argmin(abs(roots))]
    rows.append(dict(comp=r.comp,n_el=r.n_el,V=r.vol_per_atom,B=r.B,C44=r.C44,G=r.G,
                     E_ideal=E[3],E_rel=em.loc[r.comp,"e_per_atom"],dlnV_ion=-u,curv=2*c2,dEdlnV_ideal=c1,
                     spread=r.cubic_spread,vegard_dev=r.vegard_dev,delta_r=r.delta_r))
    print(len(rows), r.comp, f"Erelax {1000*(E[3]-em.loc[r.comp,'e_per_atom']):.1f} meV dlnV_ion {-u*100:.3f}%  {time.time()-t0:.0f}s", flush=True)
pd.DataFrame(rows).to_csv(out,index=False)
