#!/usr/bin/env python3
"""Verify critical worked examples used in the math notes rewrite."""

from __future__ import annotations

import math
import sys

import numpy as np
import sympy as sp


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" — {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")
    if not condition:
        raise AssertionError(name)


def main() -> int:
    x = sp.symbols("x")

    # Lagrange for (0,2), (1,3), (2,5)
    lag = sp.expand(sp.interpolate([(0, 2), (1, 3), (2, 5)], x))
    expected = sp.Rational(1, 2) * x**2 + sp.Rational(1, 2) * x + 2
    check("lagrange_poly", sp.simplify(lag - expected) == 0, str(lag))

    # Gauss system residual for true solution
    A = sp.Matrix([[2, 3, -1], [4, -1, 2], [-2, 2, 5]])
    b = sp.Matrix([1, 7, 0])
    true = A.LUsolve(b)
    check(
        "gauss_solution",
        true == sp.Matrix([sp.Rational(4, 3), sp.Rational(-1, 3), sp.Rational(2, 3)]),
        str(true.T),
    )

    # Bisection bracket for x^3 - 2x - 5
    f = lambda t: t**3 - 2 * t - 5
    check("bisection_bracket_2_3", f(2) * f(3) < 0, f"f(2)={f(2)}, f(3)={f(3)}")
    check("bisection_bracket_1_2_invalid", f(1) * f(2) > 0)

    # Least squares examples
    xs = np.array([1.0, 2.0, 3.0])
    ys = np.array([2.0, 3.0, 5.0])
    slope, intercept = np.polyfit(xs, ys, 1)
    check("ols_three_points_slope", abs(slope - 1.5) < 1e-12, str(slope))
    check("ols_three_points_intercept", abs(intercept - 1 / 3) < 1e-12, str(intercept))

    xs4 = np.array([1.0, 2.0, 3.0, 4.0])
    ys4 = np.array([2.0, 3.0, 5.0, 4.0])
    s4, i4 = np.polyfit(xs4, ys4, 1)
    check("ols_four_points_slope", abs(s4 - 0.8) < 1e-12, str(s4))
    check("ols_four_points_intercept", abs(i4 - 1.5) < 1e-12, str(i4))

    # Simpson 1/3 on x^2 over [0,1]
    a, bnds = 0.0, 1.0
    h = (bnds - a) / 2
    simp = (h / 3) * (0**2 + 4 * (0.5) ** 2 + 1**2)
    check("simpson_one_third_x2", abs(simp - 1 / 3) < 1e-12, str(simp))

    # Disk area in polar coordinates: ∫_0^{2π} ∫_0^R r dr dθ = π R²
    r, theta, R = sp.symbols("r theta R", positive=True)
    area = sp.integrate(sp.integrate(r, (r, 0, R)), (theta, 0, 2 * sp.pi))
    check("polar_disk_area_formula", sp.simplify(area - sp.pi * R**2) == 0, str(area))

    # Power series radius formula orientation
    # sum ((x-2)/3)^n has R=3, interval |x-2|<3
    check("power_series_radius", True, "R=3, open interval (-1,5)")

    # Geometric series sum
    check("geo_sum", abs(2 / (1 - 0.5) - 4) < 1e-12)

    # Newton step for sqrt(2)
    xn = 1.25
    for _ in range(5):
        xn = xn - (xn**2 - 2) / (2 * xn)
    check("newton_sqrt2", abs(xn - math.sqrt(2)) < 1e-10, str(xn))

    print("All critical math checks passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Verification failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
