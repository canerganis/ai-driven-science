"""H1 test data: clamped-ion mixing energy as a function of volume, E_mix(V).

python scripts/h1_ev.py
Atoms stay on ideal fcc sites (affine, no relaxation), so E_mix(V) is the pure chemical term.
Pure elements are evaluated at the same per-atom volume as the alloy, never at their own.
With x = ln(V/V_vegard) and E_mix = a + b x + c x^2:
  n_eff = -3 b / a        effective exponent if E_mix ~ V^(-n/3)
  R     = 2 c a / b^2     equals 1 for any pure power law; the parameter-free H1 check
  B_chem = (2c - b) / V   chemical bulk modulus term (GPa), H1 says (n/3)(n/3+1) E_mix / V
"""

import datetime as dt
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness import compute  # noqa: E402
from harness.compute import GPA  # noqa: E402
from harness.fcc_set import compositions, fresh_compositions, key  # noqa: E402

SCALES = np.linspace(0.97, 1.03, 7)  # on the lattice parameter, so +-9% in volume
pure_v = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
calc = compute.calculator()


def e_at(atoms, v_atom: float) -> float:
    a = atoms.copy()
    a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / len(a)


# "fresh" runs the held-out H3 set into its own file.
FRESH = len(sys.argv) > 1 and sys.argv[1] == "fresh"
OUT = ROOT / "data" / ("h3_fresh_rows.csv" if FRESH else "h1_ev_rows.csv")  # appended, restartable
done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for comp in (fresh_compositions() if FRESH else compositions()):
    if key(comp) in done:
        continue
    v0 = sum(x * pure_v[el] for el, x in comp.items())  # Vegard volume
    alloy = compute.solid_solution(comp, "fcc", reps=3, seed=0)
    pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in comp}
    vols = v0 * SCALES**3
    xa = compute.actual_fractions(alloy)  # whole-atom counts, not the nominal fractions
    emix = np.array([e_at(alloy, v) - sum(x * e_at(pures[el], v) for el, x in xa.items())
                     for v in vols])
    x = np.log(vols / v0)
    c, b, a = np.polyfit(x, emix, 2)
    resid = emix - np.polyval([c, b, a], x)
    r = {"comp": key(comp), "family": "-".join(sorted(comp)), "n_el": len(comp),
                 "V0": v0, "E_mix": a, "dE_dlnV": b, "d2E_dlnV2": 2 * c,
                 "n_eff": -3 * b / a, "R": 2 * c * a / b**2, "B_chem": (2 * c - b) / v0 * GPA,
                 "fit_rms_meV": float(np.sqrt(np.mean(resid**2)) * 1000),
                 "time": dt.datetime.now().isoformat(timespec="seconds"),
                 **{f"emix_{i}": e for i, e in enumerate(emix)}}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(r["family"], f"E_mix {a * 1000:+7.1f} meV  n_eff {r['n_eff']:+7.2f}  R {r['R']:+6.2f}  "
          f"B_chem {r['B_chem']:+6.1f} GPa", flush=True)
