"""Build the reproducibility archive for the latest paper/draft_v*.md.

python scripts/build_repro.py
Writes paper/repro_<date>[_<n>].zip with the ledger, literature log, harness, scripts, data tables (no sealed holdout, no
raw pw.x runs), audits, lessons and swarm records, plus a SHA256 manifest. Never overwrites an existing archive.
"""

import datetime as dt
import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INCLUDE = ["claims", "harness", "scripts", "data", ".orchestra/audits", ".orchestra/swarm", ".orchestra/fronts",
           ".orchestra/LESSONS.md", "candidates/README.md", "AGENTS.md", "STATUS.md"]
INCLUDE.append(max(ROOT.glob("paper/draft_v*.md"), key=lambda f: int(f.stem.split("_v")[1])).relative_to(ROOT).as_posix())
SKIP = ("data/sealed", "data/dft_runs", "__pycache__")

import subprocess  # noqa: E402
import sys  # noqa: E402

out = ROOT / "paper" / f"repro_{dt.date.today():%Y%m%d}.zip"
n = 1
while out.exists():  # never overwrite: a second build on the same day gets a suffix
    n += 1
    out = ROOT / "paper" / f"repro_{dt.date.today():%Y%m%d}_{n}.zip"
freeze = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True).stdout
files = []
for item in INCLUDE:
    p = ROOT / item
    for f in ([p] if p.is_file() else sorted(p.rglob("*"))):
        rel = f.relative_to(ROOT).as_posix()
        if f.is_file() and not any(rel.startswith(s) or s in rel for s in SKIP):
            files.append((rel, f))
manifest = "".join(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {rel}\n" for rel, f in files)
readme = """Reproducibility archive for "Binary shear curvatures read at the alloy's volume".
claims/claims.jsonl is the append-only ledger; every number in the paper cites an id there. Evidence paths in it are
absolute paths of the author's machine; strip the prefix up to the project folder. Scripts run with MACE-MP
(mace-torch) and ASE; each script's docstring gives its command. The sealed arena holdout and raw pw.x runs are not
included. MANIFEST.sha256 lists every file; requirements.txt pins the Python environment used. PBE runs (harness/dft.py)
need Quantum ESPRESSO and the SSSP 1.3.0 PBE efficiency pseudopotentials; set PSEUDO_DIR and DISTRO there.
"""
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for rel, f in files:
        z.write(f, rel)
    z.writestr("MANIFEST.sha256", manifest)
    z.writestr("README.txt", readme)
    z.writestr("requirements.txt", freeze)
print(out, len(files), "files", f"{out.stat().st_size / 1e6:.1f} MB")
