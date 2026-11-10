"""Size of the cutoff mismatch found in the 2026-10-31 audit: pure references ran at their own SSSP cutoff,
alloy cells at the max over their elements (harness/dft.py), so cutoff errors do not cancel in E_mix.

python scripts/ecut_bias.py
1-atom fcc cells at the element's MACE volume. For each element: energy at its own cutoff vs at the Cu-cell cutoff
(112.5/900 Ry, the largest used), at V and V e^+-0.03, and clamped shear curvatures K44, Kp at both cutoffs.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import dft  # noqa: E402
from harness.compute import GPA  # noqa: E402

S = 0.02
HIGH = {"system.ecutwfc": 112.5, "system.ecutrho": 900.0}
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
       "t+": np.diag([np.exp(S), np.exp(-S), 1.0])}


def energy(el, v, k, which, ks):
    F = DEF[k]
    a = bulk(el, "fcc", a=4.0)
    a.set_cell(a.cell * (v / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    st = dft.Settings(kspacing=ks, np=4, extra=HIGH if which == "high" else {})
    return dft.run_pw(a, f"ecut/{el}_{which}_{k}_v{v:.3f}_k{ks}", st).get_potential_energy()


rows = []
for el in ["Ir", "Rh", "Pt", "Pd", "Au", "Ag"]:
    v = pv[el]
    r = {"el": el, "V": v}
    for which in ("own", "high"):
        es = {k: energy(el, v, k, which, 0.15) for k in DEF}
        r[f"K44_{which}"] = (2 * es["g+"] - 2 * es["0"]) / (2 * S**2) * 2 / v * GPA
        r[f"Kp_{which}"] = (2 * es["t+"] - 2 * es["0"]) / (2 * S**2) / (2 * v) * GPA
        for d in (-0.03, 0.0, 0.03):
            r[f"E_{which}_{d:+.2f}"] = energy(el, v * np.exp(d), "0", which, 0.15)
    r["dE_meV"] = (r["E_high_+0.00"] - r["E_own_+0.00"]) * 1000
    r["d_dE_dlnV_meV"] = ((r["E_high_+0.03"] - r["E_own_+0.03"]) - (r["E_high_-0.03"] - r["E_own_-0.03"])) / 0.06 * 1000
    r["dK44"] = r["K44_high"] - r["K44_own"]
    r["dKp"] = r["Kp_high"] - r["Kp_own"]
    rows.append(r)
    print(el, f"dE {r['dE_meV']:+.2f} meV  d(dE/dlnV) {r['d_dE_dlnV_meV']:+.2f} meV  dK44 {r['dK44']:+.2f}  "
          f"dKp {r['dKp']:+.2f} GPa  (K44 own {r['K44_own']:.1f}, Kp own {r['Kp_own']:.1f})", flush=True)
pd.DataFrame(rows).to_csv(ROOT / "data" / "ecut_bias.csv", index=False)
