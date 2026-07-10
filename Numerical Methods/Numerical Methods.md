---
dg-publish: true
dg-show-local-graph: true
tags:
  - numerical-methods
  - hub
aliases:
  - Numerical Methods
---

# Numerical Methods

## Summary

Numerical methods approximate mathematical problems that are hard or impossible to solve in closed form: roots, linear systems, interpolation, integrals, and data fitting.

## Prerequisites

[[Calculus]], [[Linear Algebra]], basic programming literacy for algorithms.

## Learning Order

1. [[Root Finding]] — bracket and open root finders
2. [[Numerical Methods/Linear Systems/Solving Linear Systems]] — direct and iterative solvers
3. [[Polynomial Interpolation]] — Lagrange / Newton
4. Integration: [[Midpoint Rule]], [[Trapezoidal Rule]], [[Simpson 1-3 Rule]], [[Simpson 3-8 Rule]]
5. [[Curve Fitting]] / [[Least Squares]]

## Design Principles

- State assumptions (continuity, smoothness, nonsingularity).
- Separate mathematical convergence guarantees from implementation heuristics.
- Always define a stopping criterion and an error measure.
- Prefer stable algorithms (pivoting, QR) when conditioning matters.

## Connections

- Theory: [[Calculus]], [[Linear Algebra]]
- Full path list: [[LEARNING_PATHS]]

## References

NIST DLMF Chapter 3 is a compact reference for numerical linear algebra, interpolation, and quadrature.[^dlmf3]

[^dlmf3]: NIST DLMF, *Chapter 3 Numerical Methods*, https://dlmf.nist.gov/3
