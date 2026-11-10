"""Discovery swarm: one Astra and one Opus per front, in parallel, each front with its own problem.

python scripts/swarm.py [front ...] [--deep] [--no-test] [--resume]
Fronts are .orchestra/fronts/*.md (all of them by default). A front's first line after the title, "dataset: <name>",
says whether its candidates go to the arena (harness/arena.py) or are proposals the harness owner turns into a test.
Within a front the other model critiques each answer and checks prior work. Everything lands in
.orchestra/swarm/S<n>/<front>/; candidates go to candidates/S<n>_<front>_<author>_<i>.py, proposals to proposals.jsonl.
At most WORKERS agents run at once (the agents' own python checks run on this machine).
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

FR = ROOT / ".orchestra" / "fronts"
SW = ROOT / ".orchestra" / "swarm"
SW.mkdir(parents=True, exist_ok=True)
DEEP, TEST, RESUME = "--deep" in sys.argv, "--no-test" not in sys.argv, "--resume" in sys.argv
EFFORT = {"astra": "xhigh" if DEEP else "high", "opus": "max" if DEEP else "xhigh"}
WORKERS = 4
names = [a for a in sys.argv[1:] if not a.startswith("--")] or sorted(p.stem for p in FR.glob("*.md"))
n = len([p for p in SW.iterdir() if p.is_dir()]) + (0 if RESUME else 1)
S = SW / f"S{n}"
S.mkdir(exist_ok=RESUME)

LIMITS = """Limits:
- Read anything in the project except data/sealed/ (the scrambled test set). Do not edit files.
- Read .orchestra/LESSONS.md first: past ways ideas died for the wrong reason.
- Known results renamed do not count. Finding an error in the data or the harness counts as much as a new result.
- Other agents work on other fronts in parallel (.orchestra/fronts/); stay on yours unless you find something bigger."""

ARENA = """Answer with up to 3 candidates, each one ```python block with META and predict (format: candidates/README.md).
A candidate predicts from ctx only, has at most one free coefficient, and must beat the champion on a sealed holdout by
>= 10% RMSE with p < 0.01/m; one the holdout cannot tell apart from the champion is rejected before testing.
Say what mechanism each formula encodes. The rest is up to you."""

PROPOSE = """Answer with up to 3 proposals, each one ```json block:
{"claim": ..., "mechanism": ..., "prediction": <numbers for cases not yet computed>, "test": <what to compute, with
which script or data>, "falsifier": <result that would kill it>, "cost": <rough CPU hours>}
For an error found, use {"claim": "error: ...", "evidence": <file:line and numbers>, "size": ..., "fix": ...}.
The rest is up to you."""

CRITIQUE = """Below are answers from another agent for the problem in {front}. For each: (1) is it physically sound and
supported by the files it cites (check them); (2) prior work: search the literature (valency tools if you have them),
NOVEL, KNOWN (cite) or UNCLEAR; (3) KEEP or DROP. Answer as JSON lines:
{{"item": ..., "verdict": "KEEP|DROP", "prior": "NOVEL|KNOWN|UNCLEAR", "refs": [...], "why": ...}}

{items}"""


def call(agent: str, prompt: str, out: Path) -> str:
    if RESUME and out.exists() and out.stat().st_size > 0:
        return out.read_text(encoding="utf-8")
    if agent == "astra":
        cmd = ["codex", "exec", "-m", "gpt-6-astra", "-c", f'model_reasoning_effort="{EFFORT["astra"]}"', "-s",
               "read-only", "--skip-git-repo-check", "-C", str(ROOT), "-"]
    else:
        cmd = ["claude", "-p", "--model", "opus", "--effort", EFFORT["opus"], "--allowedTools", "Read", "Glob", "Grep",
               "Bash(./.venv/Scripts/python:*)", "mcp__valency", "--disallowedTools", "Edit", "Write"]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    out.write_text(r.stdout, encoding="utf-8")
    return r.stdout


def front(name: str):
    text = (FR / f"{name}.md").read_text(encoding="utf-8")
    m = re.search(r"^dataset:\s*(\S+)", text, re.M)
    ds = m.group(1) if m and m.group(1) in arena.DATASETS else None
    d = S / name
    d.mkdir(exist_ok=True)
    return name, ds, d, f"{text}\n\n{LIMITS}\n\n{ARENA if ds else PROPOSE}"


fronts = [front(x) for x in names]
jobs = [(f, a) for f in fronts for a in ("astra", "opus")]
with ThreadPoolExecutor(WORKERS) as ex:
    outs = dict(zip([(f[0], a) for f, a in jobs], ex.map(lambda j: call(j[1], j[0][3], j[0][2] / f"{j[1]}.md"), jobs)))


def items(name, ds, author, text):
    if ds:
        res = []
        for i, b in enumerate(b for b in re.findall(r"```python\n(.*?)```", text, re.S) if "META" in b and "def predict" in b):
            p = ROOT / "candidates" / f"S{n}_{name}_{author}_{i + 1}.py"
            p.write_text(f'"""Swarm S{n}, front {name}, {author}. Verbatim from .orchestra/swarm/S{n}/{name}/{author}.md"""'
                         f"\n\n{b}", encoding="utf-8")
            res.append((p.name, b, p))
        return res
    return [(f"{author}_{i + 1}", b, None) for i, b in enumerate(re.findall(r"```json\n(.*?)```", text, re.S))]


other = {"astra": "opus", "opus": "astra"}
crit_jobs = []
found = {}
for name, ds, d, _ in fronts:
    for author in ("astra", "opus"):
        its = items(name, ds, author, outs[(name, author)])
        found[(name, author)] = its
        if its:
            body = "\n\n".join(f"# {k}\n{b}" for k, b, _ in its)
            crit_jobs.append((other[author], CRITIQUE.format(front=f".orchestra/fronts/{name}.md", items=body),
                              d / f"critique_of_{author}_by_{other[author]}.md"))
with ThreadPoolExecutor(WORKERS) as ex:
    crit = list(ex.map(lambda j: call(*j), crit_jobs))
verdicts = {}
for (_, _, out), text in zip(crit_jobs, crit):
    front_name = out.parent.name
    for line in text.splitlines():
        line = line.strip().strip("`")
        if line.startswith("{") and '"verdict"' in line:
            try:
                v = json.loads(line)
                verdicts[(front_name, Path(str(v["item"])).name)] = v
            except json.JSONDecodeError:
                pass

summary = []
with (ROOT / "claims" / "literature.jsonl").open("a", encoding="utf-8") as lit:
    for name, ds, d, _ in fronts:
        for author in ("astra", "opus"):
            for key, body, path in found[(name, author)]:
                v = verdicts.get((name, key), {})
                lit.write(json.dumps({"round": f"S{n}/{name}", "candidate": key, "prior": v.get("prior"),
                                      "refs": v.get("refs"), "verdict": v.get("verdict"), "why": v.get("why")},
                                     ensure_ascii=False) + "\n")
                rec = {"front": name, "item": key, "author": author, "verdict": v.get("verdict"), "prior": v.get("prior"),
                       "why": v.get("why")}
                if path is not None and v.get("verdict") != "DROP" and v.get("prior") != "KNOWN":
                    try:
                        rep = arena.run(path, dry=not TEST)
                    except Exception as e:  # a broken candidate is the author's problem, not the swarm's
                        rep = {"status": f"error: {type(e).__name__}: {e}"}
                    rec["arena"] = {k: x for k, x in rep.items() if k != "author"}
                elif path is None:
                    try:
                        rec["proposal"] = json.loads(body)
                    except json.JSONDecodeError:
                        rec["proposal"] = body
                summary.append(rec)
                print(json.dumps(rec, ensure_ascii=False, default=str)[:400], flush=True)
(S / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
with (S / "proposals.jsonl").open("w", encoding="utf-8") as f:
    for r in summary:
        if "proposal" in r and r["verdict"] == "KEEP":
            f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
print(f"swarm S{n}: {len(summary)} items, {sum(r['verdict'] == 'KEEP' for r in summary)} kept", flush=True)
