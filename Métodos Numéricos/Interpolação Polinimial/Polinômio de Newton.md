---
dg-publish: true
tags:
  - numerical-methods
  - interpolation
aliases:
  - Newton Interpolation
---

# Newton Interpolation Polynomial

## Summary

Newton form builds the interpolant using divided differences. Adding a node only appends one term, which is convenient for adaptive interpolation.

## Prerequisites

[[Interpolação Polinimial]], [[Polinômio de Lagrange]]

## Method Definition

\[
P_n(x)=a_0+a_1(x-x_0)+a_2(x-x_0)(x-x_1)+\cdots+a_n\prod_{j=0}^{n-1}(x-x_j),
\]

where \(a_k=f[x_0,\ldots,x_k]\) are divided differences:

\[
f[x_i]=y_i,\qquad
f[x_i,\ldots,x_{i+k}]=\frac{f[x_{i+1},\ldots,x_{i+k}]-f[x_i,\ldots,x_{i+k-1}]}{x_{i+k}-x_i}.
\]

## Error / Accuracy

Same pointwise error formula as Lagrange:

\[
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_i).
\]

## Worked Example

Nodes \((0,2),(1,3),(2,5)\):

\[
\begin{aligned}
f[x_0]&=2,\\
f[x_0,x_1]&=\frac{3-2}{1-0}=1,\\
f[x_1,x_2]&=\frac{5-3}{2-1}=2,\\
f[x_0,x_1,x_2]&=\frac{2-1}{2-0}=\frac12.
\end{aligned}
\]

\[
P(x)=2+1\cdot(x-0)+\frac12(x-0)(x-1)=\frac12 x^2+\frac12 x+2,
\]

matching the Lagrange interpolant.

## Common Failure Modes

- Incorrect denominator \(x_{i+k}-x_i\) in divided differences.
- Treating Newton form as a different polynomial from Lagrange; uniqueness says they coincide.

## Connections

- Related: [[Polinômio de Lagrange]], [[Interpolação Polinimial pela Definição]]

## References

Divided-difference Newton interpolation is classical numerical analysis.[^dlmf-interp]

[^dlmf-interp]: NIST DLMF, *§3.3 Interpolation*, https://dlmf.nist.gov/3.3
