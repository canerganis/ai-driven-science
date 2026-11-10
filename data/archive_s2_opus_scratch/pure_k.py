"""Clamped K44, Kp of pure fcc elements on a dlnV grid, same strain protocol as scripts/k_shear_transfer.py."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import numpy as np, pandas as pd, torch
torch.set_num_threads(2)
from mace.calculators import mace_mp
from ase.build import bulk
calc = mace_mp(model="medium-omat-0", device="cpu", default_dtype="float64")
G = 160.21766208
AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
def F_of(name, s):
    if name == "K44":
        F = np.eye(3); F[0, 1] = s; return F
    return np.diag([np.exp(s), np.exp(-s), 1.0])
pv = pd.read_csv(ROOT/"data"/"scan_fcc_omat_pure.csv").set_index("el")
rows = []
for el in pv.index:
    for d in np.round(np.arange(-0.15, 0.1501, 0.025), 4):
        v = pv.loc[el, "vol_per_atom"]*np.exp(d); r = dict(el=el, dlnV=d, V=v)
        for name in ("K44", "Kp"):
            em = []
            for s in AMPS:
                a = bulk(el, "fcc", a=4.0, cubic=True)
                a.set_cell(a.cell*(v*4/a.get_volume())**(1/3), scale_atoms=True)
                a.set_cell(a.cell @ F_of(name, s).T, scale_atoms=True); a.calc = calc
                em.append(a.get_potential_energy()/4)
            c2 = np.polyfit(AMPS, em, 2)[0]
            r[name] = (2*c2 if name == "K44" else c2/2)/v*G
        rows.append(r)
pd.DataFrame(rows).to_csv(sys.argv[1], index=False); print("done", len(rows))
