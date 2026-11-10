"""Compare completed benchmark runs; thresholds concern solver agreement only."""
import argparse
import json
from pathlib import Path
from qe_gpu_benchmark import parse_output

RY_EV = 13.605693122994
BOHR_ANGSTROM = 0.529177210903
RY_BOHR3_GPA = RY_EV / BOHR_ANGSTROM**3 * 160.2176634
LIMITS = dict(energy_ev_atom=1e-6, stress_gpa=5e-4, force_ev_angstrom=1e-5)


def load(path):
    meta = json.loads((path/'result.json').read_text())
    meta.update(parse_output((path/'pw.out').read_text()))
    return meta


def max_delta(a, b):
    assert len(a) == len(b) and a
    assert all(len(x) == len(y) for x, y in zip(a, b))
    return max(abs(x-y) for ar, br in zip(a, b) for x, y in zip(ar, br))


def compare(ref, test):
    assert ref['source_sha256'] == test['source_sha256']
    assert ref['pseudopotentials'] == test['pseudopotentials']
    assert ref['nat'] == test['nat']
    differences = dict(
        energy_ev_atom=abs(ref['energy_ry']-test['energy_ry'])*RY_EV/ref['nat'],
        stress_gpa=max_delta(ref['stress_ry_bohr3'], test['stress_ry_bohr3'])*RY_BOHR3_GPA,
        force_ev_angstrom=max_delta(ref['forces_ry_bohr'], test['forces_ry_bohr'])*RY_EV/BOHR_ANGSTROM)
    return dict(reference=ref['mode'], candidate=test['mode'], differences=differences,
                limits=LIMITS, within_limits=all(differences[k]<=LIMITS[k] for k in LIMITS),
                elapsed_speedup=ref['elapsed_seconds']/test['elapsed_seconds'],
                scf_iterations=[ref['scf_iterations'], test['scf_iterations']],
                limitation='One structure; does not validate physical accuracy or Kp/K44. Stress uses rounded printed Ry/bohr^3 values.')


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('reference', type=Path)
    p.add_argument('candidate', type=Path)
    a=p.parse_args()
    print(json.dumps(compare(load(a.reference), load(a.candidate)), indent=2))
