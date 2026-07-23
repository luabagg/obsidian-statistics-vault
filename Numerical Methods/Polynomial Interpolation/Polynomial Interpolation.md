---
dg-publish: true
dg-show-local-graph: true
tags:
  - numerical-methods
  - interpolation
  - hub
aliases:
  - Polynomial Interpolation
---

%% Begin Waypoint %%
- **[[Polynomial Interpolation]]**
	- [[Existence and Uniqueness of Interpolating Polynomial]]
	- [[Lagrange Polynomial]]
	- [[Newton Polynomial]]
	- [[Polynomial Interpolation by Definition]]
%% End Waypoint %%

# Polynomial Interpolation

## Summary

Polynomial interpolation constructs a polynomial that passes through given data points. For distinct nodes, the polynomial of degree at most $n$ through $n+1$ points is unique.

## Prerequisites

[[Polynomials and Rational Functions]], [[Systems of Linear Equations]]

## Learning Order

1. [[Existence and Uniqueness of Interpolating Polynomial]]
2. [[Polynomial Interpolation by Definition]] (Vandermonde)
3. [[Lagrange Polynomial]]
4. [[Newton Polynomial]]

## Limitations

High-degree equispaced interpolation can oscillate (Runge phenomenon). Piecewise polynomials/splines are often preferable for large data sets (not covered in this hub’s child notes yet).

## Connections

- Contrast with approximate fitting: [[Curve Fitting]]
- Hub: [[Numerical Methods]]

## References

Existence/uniqueness and classical forms are standard numerical analysis.[^dlmf-interp]

[^dlmf-interp]: NIST DLMF, *§3.3 Interpolation*, https://dlmf.nist.gov/3.3
