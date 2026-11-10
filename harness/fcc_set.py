"""The fcc solid solution composition set shared by every fcc script."""

import itertools

import numpy as np

POOL = ["Ni", "Cu", "Pd", "Pt", "Ag", "Au", "Al", "Rh", "Ir", "Co"]


def compositions(seed: int = 7) -> list[dict[str, float]]:
    rng = np.random.default_rng(seed)
    out = [dict.fromkeys(p, 0.5) for p in itertools.combinations(POOL, 2)]
    pairs = list(itertools.combinations(POOL, 2))
    for i in rng.permutation(len(pairs))[:45]:
        a, b = pairs[i]
        out.append({a: 0.75, b: 0.25} if rng.random() < 0.5 else {a: 0.25, b: 0.75})
    for n, k in ((3, 60), (4, 25), (5, 15)):
        sets = list(itertools.combinations(POOL, n))
        for i in rng.permutation(len(sets))[:k]:
            out.append(dict.fromkeys(sets[i], 1 / n))
    # Al above 25 at.% tends to order or leave fcc; cap it so the solid solution premise holds.
    return [c for c in out if c.get("Al", 0) <= 0.25 + 1e-9]


def key(comp: dict[str, float]) -> str:
    return ";".join(f"{el}:{x:.4f}" for el, x in sorted(comp.items()))


def fresh_compositions(seed: int = 2026, n: int = 150) -> list[dict[str, float]]:
    """Held-out set for H3: Al-free, non-equiatomic, 2 to 5 elements, each at least 10 at.%."""
    rng = np.random.default_rng(seed)
    pool = [el for el in POOL if el != "Al"]
    out = []
    while len(out) < n:
        k = int(rng.integers(2, 6))
        els = rng.choice(pool, size=k, replace=False)
        x = 0.1 + (1 - 0.1 * k) * rng.dirichlet(np.ones(k))
        out.append({str(e): float(round(v, 4)) for e, v in zip(els, x)})
    return out
