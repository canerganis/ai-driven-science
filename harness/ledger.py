"""Append-only claim ledger. Nothing is called a discovery unless it is here at L2 or above.

Every entry above L1 names a parent entry one level below, so a claim's chain of evidence
can be walked back to the calibration of the method that produced its data.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "claims" / "claims.jsonl"
LEVELS = ("L0", "L1", "L2", "L3", "L4")


def file_hash(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def entries() -> list[dict]:
    if not LEDGER.exists():
        return []
    return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line]


def record(claim: str, level: str, evidence: list[str], notes: str = "",
           parent: str | None = None) -> dict:
    assert level in LEVELS, level
    if level in ("L2", "L3", "L4"):
        below = LEVELS[LEVELS.index(level) - 1]
        known = {e.get("id"): e["level"] for e in entries()}
        if known.get(parent) != below:
            raise ValueError(f"{level} claim needs a parent entry at {below}, got {parent!r}")
    now = dt.datetime.now().isoformat(timespec="seconds")
    entry = {"id": hashlib.sha256(f"{now}{claim}".encode()).hexdigest()[:10], "time": now,
             "level": level, "claim": claim, "parent": parent,
             "evidence": {str(p): file_hash(p) for p in evidence}, "notes": notes}
    LEDGER.parent.mkdir(exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


# Pre-registration and verdicts. A test is registered with its measured power (harness/power.py): a design in which
# a correct formula usually fails is not a test. A failed test is closed with a cause; only cause "hypothesis" retires
# the candidate, "design" and "numerics" send it back to the queue.
CAUSES = ("pass", "hypothesis", "design", "numerics")


def register(claim: str, script: str, power: dict, notes: str = "", inputs: tuple = ()) -> dict:
    """inputs: data files the predictions depend on; their hashes are frozen with the script (W1 design review)."""
    if power.get("power", 0) < 0.8 or power.get("false_pass", 1) > 0.05:
        raise ValueError(f"underpowered or leaky test design, not registered: {power}")
    return record(claim, "L0", [script, *inputs], notes=f"prereg; power {power}; {notes}".strip("; "))


def verdict(prereg: str, outcome: str, cause: str, audit: str, evidence: list[str]) -> dict:
    assert cause in CAUSES, cause
    if cause == "hypothesis" and not audit.strip():
        raise ValueError("retiring a candidate needs a post-fail audit (what was checked, by whom)")
    return record(f"verdict on {prereg}: {outcome}", "L0", evidence, notes=f"cause={cause}; audit: {audit}")


def open_candidates() -> list[dict]:
    """Registered candidates without a verdict, or whose last verdict was a design or numerics failure."""
    es = entries()
    last = {}
    for e in es:
        if e["claim"].startswith("verdict on "):
            last[e["claim"].split()[2].rstrip(":")] = e["notes"]
    return [e for e in es if e["notes"].startswith("prereg")
            and ("cause=pass" not in last.get(e["id"], "") and "cause=hypothesis" not in last.get(e["id"], ""))]
