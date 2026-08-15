"""
Simple pytest to check Crank-Nicolson preserves (approx.) normalization for a few steps.
"""
import numpy as np
from mother_core import MotherCore


def test_schrodinger_normalization():
    mc = MotherCore(ledger_path=':memory:')
    res = mc.solve_schrodinger_well(nx=80, nt=20, L=1.0, dt=1e-4)
    psi = res['psi']
    x = res['x']
    norm0 = np.trapz(np.abs(psi[0])**2, x)
    normf = np.trapz(np.abs(psi[-1])**2, x)
    assert abs(norm0 - 1.0) < 1e-8
    assert abs(normf - 1.0) < 1e-3
