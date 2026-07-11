---
dg-publish: true
tags:
  - numerical-methods
  - curve-fitting
  - hub
aliases:
  - Curve Fitting
---

# Curve Fitting

## Summary

Curve fitting chooses a model family and parameters that match data in an approximate sense. Least squares is the default criterion when errors are roughly additive and isotropic.

## Prerequisites

[[Linear Algebra]], [[Least Squares]]

## Learning Order

1. [[Least Squares]] — linear regression / polynomial models linear in parameters
2. Cross-link theory: [[Least Squares and QR]]
3. Related interpolation (exact through nodes): [[Polynomial Interpolation]]

## Key Distinctions

- **Interpolation** forces $P(x_i)=y_i$ exactly.
- **Fitting / regression** allows residual $y_i-f(x_i)\neq 0$ and minimizes a loss.
- A model can be nonlinear in $x$ yet linear in parameters (e.g. $a+bx+cx^2$).

## Worked Example Pointer

For $(1,2),(2,3),(3,5)$, the OLS line is $y=\frac13+\frac32 x$. Details in [[Least Squares]].

## Connections

- Hub: [[Numerical Methods]]
- Linear algebra: [[Orthogonality and Projections]]

## References

Least-squares curve fitting is standard numerical linear algebra.[^mit-1806]

[^mit-1806]: MIT OpenCourseWare, *18.06SC Linear Algebra*, https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
