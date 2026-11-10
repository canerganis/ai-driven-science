# Candidates

One python file per candidate. The arena (`harness/arena.py`) loads it, fits at most one free coefficient on the
training rows, checks on the sealed holdout's compositions that the test can tell it from the champion, pre-registers
it, then tests it on the sealed targets.

```python
META = {
    "name": "short_snake_name",
    "author": "astra | opus | ...",
    "dataset": "emix_random",
    "statement": "one line: the physical claim",
    "mechanism": "a few lines: why",
    "free": [],                      # or [("k", lo, hi)]
}

def predict(comp, ctx, *coef):       # comp: {"Cu": 0.25, ...}; ctx: harness/context.py
    return ...                       # eV/atom
```

The champion is `champion_volume_transfer.py`. A candidate must beat it by 10% RMSE with p < 0.01/m.
