---
dg-publish: true
tags:
  - numerical-methods
  - quadrature
aliases:
  - Trapezoidal Rule
---

# Trapezoidal Rule

## Summary

The trapezoidal rule approximates the area under \(y=f(x)\) by trapezoids. The composite rule is second-order accurate for smooth \(f\).

## Prerequisites

[[Integrals]], [[Riemann Sum]]

## Formula / Iteration Rule

With \(h=(b-a)/n\), \(x_i=a+ih\), \(y_i=f(x_i)\),

\[
\int_a^b f(x)\,dx
\approx \frac{h}{2}\big(y_0+2y_1+\cdots+2y_{n-1}+y_n\big).
\]

## Error / Accuracy

If \(f''\) is continuous,

\[
E=-\frac{(b-a)}{12}h^2 f''(\xi)
\]

for some \(\xi\in(a,b)\). Thus the error is \(O(h^2)\).

## Worked Example

\(\int_0^1 x^2\,dx\) with \(n=2\), \(h=1/2\):

\[
\frac{1/2}{2}\big(0+2\cdot(1/2)^2+1\big)=\frac14\cdot\frac{3}{2}=\frac38=0.375.
\]

Exact: \(1/3\approx 0.333\).

## Common Failure Modes

- Claiming a specific absolute accuracy from a large \(n\) without using the error formula or a comparison integral.
- Applying the smooth-error formula across singularities.

## Visual Explanation

![[TrapezoidalRule.mp4]]

## Connections

- Related: [[Midpoint Rule]], [[Simpson 1-3 Rule]]

## References

Composite trapezoidal quadrature is standard.[^dlmf-quad]

[^dlmf-quad]: NIST DLMF, *§3.5 Quadrature*, https://dlmf.nist.gov/3.5
