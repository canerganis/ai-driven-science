"""What a candidate formula may use: per-element and per-binary inputs, never the alloy's own target.

ctx.pure[el]      dict: V (A^3/atom, MACE fcc), B, G, C11, C12, C44 (GPa), r, chi, vec, tm
ctx.pair[(a, b)]  dict for sorted element pairs, 50:50 random clamped binary at its Vegard volume V_ij:
                  E (eV/atom), D = dE/dlnV, D2 = d2E/dlnV2 (eV/atom), V (A^3/atom); mean over SQS seeds 0-2
ctx.vegard(comp)  Vegard volume of a composition
ctx.pairs(comp)   iterator over (a, b, x_a, x_b) for unlike pairs
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from pathlib import Path

import pandas as pd

from harness.features import elem, parse_comp

ROOT = Path(__file__).resolve().parent.parent


class Context:
    def __init__(self):
        p = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
        self.pure = {}
        for el, r in p.iterrows():
            self.pure[el] = {"V": r.vol_per_atom, "B": r.B, "G": r.G, "C11": r.C11, "C12": r.C12, "C44": r.C44,
                             **elem(el)}
        h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
        h1["c"] = h1.comp.map(parse_comp)
        eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
        rows = [eq[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]]]
        seeds = ROOT / "data" / "binary_seeds.csv"
        if seeds.exists():
            rows.append(pd.read_csv(seeds)[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]])
        b = pd.concat(rows)
        b["pair"] = b.comp.map(lambda s: tuple(sorted(parse_comp(s))))
        m = b.groupby("pair")[["E_mix", "dE_dlnV", "d2E_dlnV2"]].mean()
        self.pair = {k: {"E": r.E_mix, "D": r.dE_dlnV, "D2": r.d2E_dlnV2,
                         "V": 0.5 * (self.pure[k[0]]["V"] + self.pure[k[1]]["V"])} for k, r in m.iterrows()}

    def vegard(self, comp: dict) -> float:
        return sum(x * self.pure[e]["V"] for e, x in comp.items())

    def pairs(self, comp: dict):
        for a, b in combinations(sorted(comp), 2):
            yield a, b, comp[a], comp[b]


@lru_cache(maxsize=1)
def context() -> Context:
    return Context()
