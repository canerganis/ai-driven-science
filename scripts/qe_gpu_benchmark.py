"""Run isolated, cold-start CPU/GPU QE comparisons from an existing PBE input.

Run inside WSL with Python 3; no third-party Python dependencies.
Never changes the source input, existing QE installation, or production outputs.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_output(text):
    energy = re.findall(r"!\s+total energy\s+=\s+([-\d.]+)\s+Ry", text)
    scf = re.findall(r"convergence has been achieved in\s+(\d+) iterations", text)
    stress = re.findall(r"total\s+stress[^\n]*\n((?:[^\n]*\n){3})", text)
    forces = re.findall(r"atom\s+\d+\s+type\s+\d+\s+force =\s+([-\d.Ee+]+)\s+([-\d.Ee+]+)\s+([-\d.Ee+]+)", text)
    if not energy or not scf or not stress or 'JOB DONE.' not in text or 'convergence NOT achieved' in text:
        raise ValueError('Missing converged energy/stress or JOB DONE')
    return dict(energy_ry=float(energy[-1]), scf_iterations=int(scf[-1]),
                stress_ry_bohr3=[[float(v) for v in line.split()[:3]] for line in stress[-1].splitlines()],
                stress_kbar=[[float(v) for v in line.split()[3:6]] for line in stress[-1].splitlines()],
                forces_ry_bohr=[[float(v) for v in row] for row in forces],
                gpu_active=bool(re.search(r'GPU acceleration\s+is\s+ACTIVE', text)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--mode', choices=['cpu2', 'cpu4', 'cpu8', 'gpu'], required=True)
    p.add_argument('--gpu-exe', type=Path)
    p.add_argument('--threads', type=int, default=4)
    a = p.parse_args()
    dest = a.output.resolve()
    dest.mkdir(parents=True, exist_ok=False)
    source = a.input.resolve()
    raw = source.read_text()
    scratch = dest / 'scratch'
    modified, count = re.subn(r"outdir\s*=\s*'[^']*'", f"outdir = '{scratch}'", raw)
    assert count == 1, 'Expected exactly one outdir'
    (dest / 'pw.in').write_text(modified)
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1', OMP_PROC_BIND='false')
    if a.mode.startswith('cpu'):
        ranks = int(a.mode[3:])
        base = Path.home() / 'mamba/envs/qe/bin'
        env['OMP_NUM_THREADS'] = '1'
        cmd = [str(base/'mpirun'), '-np', str(ranks), str(base/'pw.x'), '-nk', str(min(ranks, 4)), '-in', 'pw.in']
        exe = base / 'pw.x'
    else:
        assert a.gpu_exe and a.gpu_exe.is_file()
        exe = a.gpu_exe.resolve()
        env['OMP_NUM_THREADS'] = str(a.threads)
        cmd = [str(exe), '-in', 'pw.in']
    pseudo_dir = Path(re.search(r"pseudo_dir\s*=\s*'([^']+)'", raw)[1])
    upfs = re.findall(r'^\s*\w+\s+[\d.]+\s+(\S+\.[Uu][Pp][Ff])\s*$', raw, re.M)
    meta = dict(mode=a.mode, command=cmd, source=str(source), source_sha256=sha256(source),
                executable=str(exe), executable_sha256=sha256(exe),
                pseudopotentials={n:sha256(pseudo_dir/n) for n in upfs},
                changed_input_fields=['outdir'], omp_threads=env['OMP_NUM_THREADS'],
                nat=int(re.search(r'\bnat\s*=\s*(\d+)', raw)[1]), started=time.time())
    (dest/'metadata.json').write_text(json.dumps(meta, indent=2))
    start = time.perf_counter()
    with (dest/'pw.out').open('w') as out, (dest/'pw.err').open('w') as err:
        run = subprocess.run(cmd, cwd=dest, env=env, stdout=out, stderr=err)
    meta.update(elapsed_seconds=time.perf_counter()-start, returncode=run.returncode)
    (dest/'metadata.json').write_text(json.dumps(meta, indent=2))
    if run.returncode:
        raise RuntimeError(f'QE failed; inspect {dest}')
    result = parse_output((dest/'pw.out').read_text())
    if a.mode == 'gpu' and not result['gpu_active']:
        raise RuntimeError('GPU activation banner missing')
    meta.update(result)
    (dest/'result.json').write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2), flush=True)


if __name__ == '__main__':
    main()
