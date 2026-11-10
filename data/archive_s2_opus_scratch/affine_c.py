"""Exploration (seen scan rows): clamped-ion (affine) elastic constants at the relaxed state vs scan's relaxed-ion ones."""
import os, sys, time

os.environ["HARNESS_MODEL"] = "medium-omat-0"
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import torch; torch.set_num_threads(6)
import numpy as np, pandas as pd
from harness import compute
from harness.features import parse_comp
out = Path(sys.argv[1])
scan = pd.concat([pd.read_csv(ROOT/"data"/f) for f in ("scan_fcc_omat.csv","scan_fcc_omat_rev.csv")]).drop_duplicates("comp")
scan = scan.sample(frac=1, random_state=3)  # mixed order
done = set(pd.read_csv(out).comp) if out.exists() else set()
from mace.calculators import mace_mp
calc = mace_mp(model="medium-omat-0", device="cpu", default_dtype="float64")
compute.calculator = lambda: calc
t0 = time.time()
for r in scan.itertuples():
    if r.comp in done: continue
    a = compute.solid_solution(parse_comp(r.comp), "fcc", 3, 0)
    compute.relax(a, cell=True)
    v = a.get_volume()/len(a)
    e_rel = a.get_potential_energy()/len(a)
    ideal = compute.solid_solution(parse_comp(r.comp), "fcc", 3, 0)
    ideal.set_cell(a.cell, scale_atoms=True); ideal.calc = calc
    e_id = ideal.get_potential_energy()/len(a)
    C = compute.elastic_tensor(a, relax_ions=False)
    c11, c12, c44 = compute.cubic_average(C)
    rec = dict(comp=r.comp, n_el=r.n_el, V=v, vol_check=v/r.vol_per_atom-1, E_relax=e_id-e_rel,
               C11a=c11, C12a=c12, C44a=c44, C11=r.C11, C12=r.C12, C44=r.C44, B=r.B, spread=r.cubic_spread,
               delta_r=r.delta_r)
    pd.DataFrame([rec]).to_csv(out, mode="a", header=not out.exists(), index=False)
    print(r.comp, f"Erel {1000*rec['E_relax']:.1f} N44 {c44-r.C44:.1f} N' {(c11-c12-r.C11+r.C12)/2:.1f} vchk {rec['vol_check']:+.4f} {time.time()-t0:.0f}s", flush=True)
