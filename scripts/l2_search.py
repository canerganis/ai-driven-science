"""L2 residual search on the fcc scan: python scripts/l2_search.py [n_perm]"""

import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from harness import discover, ledger  # noqa: E402
from harness.baselines import reuss  # noqa: E402
from harness.features import parse_comp  # noqa: E402

n_perm = int(sys.argv[1]) if len(sys.argv) > 1 else 60000
files = [ROOT / "data" / f for f in ("scan_fcc_omat.csv", "scan_fcc_omat_rev.csv")]
df = pd.concat([pd.read_csv(f) for f in files if f.exists()]).drop_duplicates("comp")
emix = pd.read_csv(ROOT / "data" / "scan_fcc_omat_emix.csv")
emix = emix[emix.vol_check.abs() < 2e-3]  # rebuilt cell must be the scanned structure
df = df.merge(emix[["comp", "E_mix"]], on="comp")
df = df[df.cubic_spread < 0.1].reset_index(drop=True)
pure = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
pure["Cp"] = (pure.C11 - pure.C12) / 2
df["Cp"] = (df.C11 - df.C12) / 2
# Moduli are compared with the Reuss bound, volume with Vegard. Against rule of mixtures any
# modulus residual tracks modulus mismatch trivially (the Voigt-Reuss gap), see AGENTS.md.
for t in ("B", "G", "C44", "Cp"):
    df[f"{t}_reuss"] = [reuss(parse_comp(c), pure[t].to_dict()) for c in df.comp]
bases = {"B": "B_reuss", "G": "G_reuss", "C44": "C44_reuss", "Cp": "Cp_reuss",
         "vol_per_atom": "vol_per_atom_rom"}
for t, b in bases.items():  # dimensionless form: X / X_base - 1
    df[f"r{t}"] = df[t] / df[b] - 1
    df[f"r{t}_base"] = 0.0
df["E_mix"] *= 1000  # meV/atom
base_cols = ["delta_r", "d_chi", "vec", "S_mix", "d_B", "d_G", "d_C44", "E_mix"]
tests = list(bases.items()) + [(f"r{t}", f"r{t}_base") for t in bases]
stamp = f"{dt.datetime.now():%Y%m%d_%H%M%S}"
snap = ROOT / "data" / f"l2_input_{stamp}.csv"
df.to_csv(snap, index=False)
print(f"{len(df)} rows after quality filter, {df.family.nunique()} families")
out = []
for target, base in tests:
    # vegard_dev and misfit_sum are built from the alloy volume, so they leak into volume targets.
    cols = base_cols + ([] if "vol" in target else ["vegard_dev", "misfit_sum"])
    res = discover.search(df, target, base, cols, group="family", n_perm=n_perm, n_top=1,
                          n_tests=len(tests))
    top = res.iloc[0].to_dict() | {"target": target}
    out.append(top)
    print(f"{target:>14}: {top['term']:<22} gain {top['gain']:+.3f} p {top['p_perm']:.2e} "
          f"(alpha {top['p_bonf_alpha']:.1e}) L2={top['passes_L2']}", flush=True)
summary = pd.DataFrame(out)
sp = ROOT / "data" / f"l2_results_{stamp}.csv"
summary.to_csv(sp, index=False)
parent = next(e["id"] for e in reversed(ledger.entries())
              if e["level"] == "L1" and "medium-omat-0" in e["claim"] and e.get("id"))
for r in summary[summary.passes_L2].itertuples():
    e = ledger.record(f"fcc solid solutions (medium-omat-0): residual {r.target} explained by {r.term}",
                      "L2", [str(snap), str(sp)], parent=parent,
                      notes=f"CV gain {r.gain:.3f}, p_perm {r.p_perm:.2e} < {r.p_bonf_alpha:.1e}")
    print("L2 recorded", e["id"])
