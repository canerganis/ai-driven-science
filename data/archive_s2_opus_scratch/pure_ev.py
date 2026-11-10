import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd, torch
torch.set_num_threads(2)
from mace.calculators import mace_mp
from ase.build import bulk
calc = mace_mp(model="medium-omat-0", device="cpu", default_dtype="float64")
pv = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el")
rows = []
for el in pv.index:
    for d in np.round(np.arange(-0.45, 0.4501, 0.025), 4):
        a = bulk(el, "fcc", a=4.0, cubic=True); v = pv.loc[el, "vol_per_atom"]*np.exp(d)
        a.set_cell(a.cell*(v*4/a.get_volume())**(1/3), scale_atoms=True); a.calc = calc
        rows.append(dict(el=el, dlnV=d, V=v, E=a.get_potential_energy()/4))
pd.DataFrame(rows).to_csv(sys.argv[1], index=False); print("done", len(rows))
