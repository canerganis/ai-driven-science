"""One discovery round: problems -> free derivation by Astra and Opus in parallel -> cross-critique with a prior-work
check -> arena (power, pre-registration, sealed test).

python scripts/discovery_round.py [dataset] [--no-test] [--deep]
Effort is one notch below the top (Astra high, Opus xhigh). --deep uses the top (xhigh, max); the round escalates to it
by itself when no candidate passes the power gate.
The agents get the problem, the limits and the candidate format, nothing else; how they think is theirs.
Everything lands in .orchestra/rounds/R<n>/. Candidates are copied to candidates/R<n>_<author>_<i>.py.
"""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness import arena  # noqa: E402
from harness.anomaly import brief  # noqa: E402

DS = next((a for a in sys.argv[1:] if not a.startswith("--")), "emix_random")
TEST = "--no-test" not in sys.argv
DEEP = "--deep" in sys.argv
EFFORT = {"astra": "xhigh" if DEEP else "high", "opus": "max" if DEEP else "xhigh"}
RD = ROOT / ".orchestra" / "rounds"
RD.mkdir(parents=True, exist_ok=True)
RESUME = "--resume" in sys.argv  # continue the last round after a crash or reboot; finished agent outputs are kept
n = len([p for p in RD.iterdir() if p.is_dir()]) + (0 if RESUME else 1)
R = RD / f"R{n}"
R.mkdir(exist_ok=RESUME)

LIMITS = """Limits (enforced by the harness, not negotiable):
- You may read anything in the project except data/sealed/ (the test set; it is scrambled, do not try to decode it).
- Do not edit files. Put your candidates in your answer.
- A candidate predicts the target from ctx only (harness/context.py: pure-element properties and 50:50 binary
  mixing data), never from the alloy's own computed values. At most one free coefficient; it is fitted on the
  training rows by the arena.
- It must beat the champion on a sealed holdout by >= 10% RMSE with p < 0.01/m. A candidate the holdout cannot tell
  apart from the champion is rejected before testing, so a cosmetic variant is wasted.
- Read .orchestra/LESSONS.md: past ways candidates died for the wrong reason.
- Known results renamed do not count."""

ASK = """{problems}

{limits}

Format: candidates/README.md. Give up to 3 candidates, each as one ```python block with META and predict. Physics
first: say what mechanism the formula encodes. Finding an error in the data or the harness counts as much as a
formula: report it with evidence. The rest is up to you."""

CRITIQUE = """Below are candidates from another agent for the problem in {brief_path}. For each: (1) is it physically
sound and not a trivial refit of the champion; (2) prior work: search the literature (use the valency tools if you have
them) and say NOVEL, KNOWN (cite) or UNCLEAR; (3) one line verdict KEEP or DROP. Answer as JSON lines:
{{"file": ..., "verdict": "KEEP|DROP", "prior": "NOVEL|KNOWN|UNCLEAR", "refs": [...], "why": ...}}

{cands}"""


def astra(prompt: str, out: Path) -> str:
    if RESUME and out.exists() and out.stat().st_size > 0:
        return out.read_text(encoding="utf-8")
    r = subprocess.run(["codex", "exec", "-m", "gpt-6-astra", "-c", f'model_reasoning_effort="{EFFORT["astra"]}"', "-s", "read-only",
                        "--skip-git-repo-check", "-C", str(ROOT), "-"], input=prompt, capture_output=True, text=True,
                       encoding="utf-8")
    out.write_text(r.stdout, encoding="utf-8")
    return r.stdout


def opus(prompt: str, out: Path) -> str:
    if RESUME and out.exists() and out.stat().st_size > 0:
        return out.read_text(encoding="utf-8")
    r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", EFFORT["opus"], "--allowedTools", "Read", "Glob", "Grep",
                        "Bash(./.venv/Scripts/python:*)", "mcp__valency", "--disallowedTools", "Edit", "Write"],
                       input=prompt, capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    out.write_text(r.stdout, encoding="utf-8")
    return r.stdout


AGENTS = {"astra": astra, "opus": opus}


def extract(text: str, author: str) -> list[Path]:
    paths = []
    for i, block in enumerate(b for b in re.findall(r"```python\n(.*?)```", text, re.S) if "META" in b and "def predict" in b):
        p = ROOT / "candidates" / f"R{n}_{author}_{i + 1}.py"
        p.write_text(f'"""Round R{n}, {author}. Verbatim from .orchestra/rounds/R{n}/{author}.md"""\n\n' + block,
                     encoding="utf-8")
        paths.append(p)
    return paths


problems = brief(DS)
extra = ROOT / ".orchestra" / "problems_extra.md"
if extra.exists():
    problems += "\n\n" + extra.read_text(encoding="utf-8")
(R / "problems.md").write_text(problems, encoding="utf-8")
prompt = ASK.format(problems=problems, limits=LIMITS)
(R / "prompt.md").write_text(prompt, encoding="utf-8")

with ThreadPoolExecutor(2) as ex:
    outs = dict(zip(AGENTS, ex.map(lambda a: AGENTS[a](prompt, R / f"{a}.md"), AGENTS)))
cands = {a: extract(t, a) for a, t in outs.items()}
print({a: [p.name for p in ps] for a, ps in cands.items()}, flush=True)

# cross-critique: each agent reviews the other's candidates
other = {"astra": "opus", "opus": "astra"}
with ThreadPoolExecutor(2) as ex:
    jobs = {}
    for critic, author in other.items():
        if cands[author]:
            body = "\n\n".join(f"# {p.name}\n{p.read_text(encoding='utf-8')}" for p in cands[author])
            q = CRITIQUE.format(brief_path=f".orchestra/rounds/R{n}/problems.md", cands=body)
            jobs[author] = ex.submit(AGENTS[critic], q, R / f"critique_of_{author}_by_{critic}.md")
    verdicts = {}
    for author, j in jobs.items():
        for line in j.result().splitlines():
            line = line.strip().strip("`")
            if line.startswith("{") and '"verdict"' in line:
                try:
                    v = json.loads(line)
                    verdicts[Path(v["file"]).name] = v
                except json.JSONDecodeError:
                    pass
with (ROOT / "claims" / "literature.jsonl").open("a", encoding="utf-8") as f:
    for name, v in verdicts.items():
        f.write(json.dumps({"round": f"R{n}", "candidate": name, "prior": v.get("prior"), "refs": v.get("refs"),
                            "verdict": v.get("verdict"), "why": v.get("why")}, ensure_ascii=False) + "\n")

results = []
for p in [p for ps in cands.values() for p in ps]:
    v = verdicts.get(p.name, {})
    if v.get("verdict") == "DROP" or v.get("prior") == "KNOWN":
        results.append({"file": p.name, "status": f"dropped in critique: {v.get('why')}"})
        continue
    try:
        rep = arena.run(p, dry=not TEST)
    except Exception as e:  # a broken candidate is the author's problem, not the round's
        rep = {"status": f"error: {type(e).__name__}: {e}"}
    results.append({"file": p.name, **{k: v for k, v in rep.items() if k != "author"}})
    print(results[-1], flush=True)
(R / "results.json").write_text(json.dumps(results, indent=1, default=str), encoding="utf-8")
if not DEEP and not any(r.get("power", 0) >= 0.8 for r in results):
    print("no candidate passed the power gate; escalating to a deep round", flush=True)
    subprocess.run([sys.executable, __file__, DS, "--deep"] + (["--no-test"] if not TEST else []), check=False)
