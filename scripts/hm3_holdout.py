"""Third holdout (for the transfer coefficient k): clamped E_mix at Vegard volume only, 3 random seeds per composition.

python scripts/hm3_holdout.py
Al-free, 3 to 5 elements, Dirichlet fractions (each >= 0.1), seed 2028, no overlap with h1, h3 or hm_fresh.
Written to data/hm3_holdout_rows.csv. No agent may read it before its formula is registered.
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
from harness.fcc_set import compositions, fresh_compositions, key  # noqa: E402

POOL = ["Ni", "Cu", "Pd", "Pt", "Ag", "Au", "Rh", "Ir", "Co"]
pure_v = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
calc = compute.calculator()
seen = ({key(c) for c in compositions()} | {key(c) for c in fresh_compositions()}
        | set(pd.read_csv(ROOT / "data" / "hm_fresh_rows.csv")["comp"]))


def e_at(atoms, v):
    a = atoms.copy()
    a.set_cell(a.cell * (v * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.calc = calc
    return a.get_potential_energy() / len(a)


rng = np.random.default_rng(2028)
comps = []
while len(comps) < 150:
    n = int(rng.choice([3, 4, 5], p=[0.3, 0.35, 0.35]))
    els = sorted(rng.choice(POOL, n, replace=False))
    x = rng.dirichlet(np.ones(n))
    if x.min() < 0.1:
        continue
    c = {e: round(float(v), 4) for e, v in zip(els, x)}
    c[els[-1]] = round(1 - sum(c[e] for e in els[:-1]), 4)
    if key(c) not in seen | {key(k) for k in comps}:
        comps.append(c)

OUT = ROOT / "data" / "hm3_holdout_rows.csv"
done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
for comp in comps:
    if key(comp) in done:
        continue
    v0 = sum(x * pure_v[el] for el, x in comp.items())
    xa = {el: c / 108 for el, c in compute.site_counts(comp, 108).items()}  # whole-atom counts in the 108-site cell
    ref = sum(x * e_at(bulk(el, "fcc", a=4.0, cubic=True), v0) for el, x in xa.items())
    e = [e_at(compute.solid_solution(comp, "fcc", reps=3, seed=s), v0) - ref for s in (0, 1, 2)]
    r = {"comp": key(comp), "family": "-".join(sorted(comp)), "n_el": len(comp), "V0": v0,
         "E_mix": float(np.mean(e)), "E_sd": float(np.std(e)), "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
