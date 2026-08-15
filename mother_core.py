"""
mother_core.py
Central simulation routines for Ras7rba - V11.0
Contains multiple numerical solvers and a simple runner that records results.
"""

import numpy as np
import hashlib
import json
from datetime import datetime

try:
    from create_ledger import log_result, init_db
except Exception:
    # When running tests, import may be relative
    from .create_ledger import log_result, init_db


class MotherCore:
    def __init__(self, ledger_path="noor_wall_ledger.db"):
        init_db(ledger_path)
        self.ledger_path = ledger_path
        self.results = {}

    def _checksum(self, arrs):
        h = hashlib.sha256()
        for a in arrs:
            if a is None:
                continue
            h.update(np.ascontiguousarray(a).tobytes())
        return h.hexdigest()

    def solve_klein_gordon(self, nx=100, nt=500, m=1.0, dt=0.01):
        dx = 20.0 / (nx - 1)
        phi = np.zeros((nt, nx))
        x = np.linspace(-10, 10, nx)
        phi[0] = np.exp(-x**2 / 4)
        phi[1] = phi[0].copy()
        for n in range(1, nt - 1):
            phi[n+1, 1:-1] = (
                2 * phi[n, 1:-1]
                - phi[n-1, 1:-1]
                + (dt / dx) ** 2 * (phi[n, 2:] - 2 * phi[n, 1:-1] + phi[n, :-2])
                - m ** 2 * dt ** 2 * phi[n, 1:-1]
            )
        cs = self._checksum([phi, x])
        result = {"name": "Klein-Gordon", "status": "SOLVED NUMERICALLY", "phi": phi, "x": x, "checksum": cs}
        self.results[result['name']] = result
        log_result(result['name'], cs, pulse_applied=None, metadata={"nx": nx, "nt": nt})
        return result

    def solve_schrodinger_well(self, nx=200, nt=500, L=1.0, dt=1e-4, hbar=1.0, m=1.0):
        # Crank-Nicolson for 1D infinite well with V=0
        dx = L / (nx - 1)
        x = np.linspace(0, L, nx)
        psi = np.zeros((nt, nx), dtype=complex)
        # initial condition: first eigenstate with a phase
        psi0 = np.sin(np.pi * x / L) * np.exp(1j * 10 * x)
        # normalize
        psi0 = psi0 / np.sqrt(np.trapz(np.abs(psi0) ** 2, x))
        psi[0] = psi0

        # Set up tridiagonal matrix for Crank-Nicolson
        r = 1j * hbar * dt / (2 * m * dx * dx)
        main = np.ones(nx) * (1 + 2 * r)
        off = np.ones(nx - 1) * (-r)
        # Impose Dirichlet BCs (psi=0 at boundaries)
        main[0] = main[-1] = 1.0
        A = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)

        main_b = np.ones(nx) * (1 - 2 * r)
        off_b = np.ones(nx - 1) * (r)
        B = np.diag(main_b) + np.diag(off_b, 1) + np.diag(off_b, -1)
        # enforce BCs in B
        B[0, :] = 0.0
        B[-1, :] = 0.0
        B[0, 0] = 1.0
        B[-1, -1] = 1.0

        # pre-factorize A using numpy.linalg (sufficient for small nx)
        for n in range(0, nt - 1):
            b = B.dot(psi[n])
            # enforce BCs in b
            b[0] = 0.0
            b[-1] = 0.0
            psi[n + 1] = np.linalg.solve(A, b)
            # renormalize to reduce drift (optional)
            norm = np.sqrt(np.trapz(np.abs(psi[n + 1]) ** 2, x))
            if norm != 0:
                psi[n + 1] /= norm

        cs = self._checksum([psi, x])
        result = {"name": "Schrodinger Well", "status": "SOLVED NUMERICALLY", "psi": psi, "x": x, "checksum": cs}
        self.results[result['name']] = result
        log_result(result['name'], cs, pulse_applied=None, metadata={"nx": nx, "nt": nt, "L": L})
        return result

    def solve_lotka_volterra(self, alpha=1.5, beta=1.0, delta=1.0, gamma=3.0, dt=0.01, steps=1000):
        prey = np.zeros(steps)
        pred = np.zeros(steps)
        prey[0], pred[0] = 10.0, 5.0
        for i in range(steps - 1):
            prey[i + 1] = prey[i] + dt * (alpha * prey[i] - beta * prey[i] * pred[i])
            pred[i + 1] = pred[i] + dt * (delta * prey[i] * pred[i] - gamma * pred[i])
        cs = self._checksum([prey, pred])
        result = {"name": "Lotka-Volterra", "status": "SOLVED NUMERICALLY", "prey": prey, "pred": pred, "checksum": cs}
        self.results[result['name']] = result
        log_result(result['name'], cs, pulse_applied=None, metadata={"alpha": alpha})
        return result

    def solve_forced_damped_oscillator(self, omega0=1.0, gamma=0.1, F0=1.0, omega_drive=1.44, dt=0.01, steps=5000):
        t = np.linspace(0, dt * (steps - 1), steps)
        x = np.zeros(steps)
        v = np.zeros(steps)
        for i in range(steps - 1):
            a = -2 * gamma * v[i] - omega0 ** 2 * x[i] + F0 * np.cos(omega_drive * t[i])
            v[i + 1] = v[i] + a * dt
            x[i + 1] = x[i] + v[i + 1] * dt
        cs = self._checksum([x, t])
        result = {"name": "Forced Damped Oscillator", "status": "SOLVED NUMERICALLY", "x": x, "t": t, "checksum": cs}
        self.results[result['name']] = result
        log_result(result['name'], cs, pulse_applied=1444.44, metadata={"omega0": omega0})
        return result

    def solve_burgers_shock(self, nx=200, nt=300, nu=0.01, dt=0.001):
        x = np.linspace(0, 2 * np.pi, nx)
        u = np.sin(x)
        us = np.zeros((nt, nx))
        us[0] = u
        dx = x[1] - x[0]
        for n in range(0, nt - 1):
            un = us[n].copy()
            # viscous Burgers using simple finite difference (periodic)
            us[n + 1, 1:-1] = (
                un[1:-1]
                - un[1:-1] * dt / (2 * dx) * (un[2:] - un[:-2])
                + nu * dt / (dx ** 2) * (un[2:] - 2 * un[1:-1] + un[:-2])
            )
            # periodic BCs
            us[n + 1, 0] = us[n + 1, -2]
            us[n + 1, -1] = us[n + 1, 1]
        cs = self._checksum([us, x])
        result = {"name": "Burgers Shock", "status": "SOLVED NUMERICALLY", "u": us, "x": x, "checksum": cs}
        self.results[result['name']] = result
        log_result(result['name'], cs, pulse_applied=None, metadata={"nu": nu})
        return result

    def run_all(self):
        # run a selection of lightweight simulations for demonstration
        out = {}
        out['KG'] = self.solve_klein_gordon(nx=100, nt=200)
        out['Sch'] = self.solve_schrodinger_well(nx=120, nt=200)
        out['LV'] = self.solve_lotka_volterra(steps=1000)
        out['Osc'] = self.solve_forced_damped_oscillator(steps=2000)
        out['Burg'] = self.solve_burgers_shock(nx=128, nt=150)
        return out
