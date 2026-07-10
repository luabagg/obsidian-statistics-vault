---
dg-publish: true
---

# Simpson’s Rule (3/8)

## Summary

Simpson’s 3/8 rule integrates a cubic interpolant on three equal subintervals (four nodes). Composite use requires the number of subintervals to be a multiple of 3.

## Prerequisites

- [[Regra de Simpson (um terço)]]
- Equally spaced nodes

## Problem Type

Approximate $\int_a^b f(x)\,dx$, often combining 3/8 panels with 1/3 panels when $n\bmod 6$ constraints appear.

## Method Definition

**One 3/8 panel:** $n=3$ subintervals, $h=(b-a)/3$, nodes $x_0,x_1,x_2,x_3$.

$$
\int_a^b f(x)\,dx \approx \frac{3h}{8}\big(f(x_0)+3f(x_1)+3f(x_2)+f(x_3)\big).
$$

**Composite ( $n$ multiple of 3):** weights follow the repeating pattern

$$
1,3,3,2,3,3,2,\ldots,3,3,1
$$

scaled by $3h/8$.[^burden]

## Assumptions / Requirements

- $f$ continuous; classical error analysis assumes sufficient smoothness
- $n$ divisible by 3 for a pure composite 3/8 rule

## Error / Accuracy

Single 3/8 panel error is $O(h^5)$ involving $f^{(4)}$, same order family as Simpson 1/3; constants differ. For smooth $f$, 1/3 is usually preferred panel-for-panel, while 3/8 is useful for fitting $n\bmod 3$ constraints.

## Worked Example

Integrate $f(x)=x^2$ on $[0,3]$ with one 3/8 panel ($h=1$).

Nodes: $0,1,2,3$ with values $0,1,4,9$.

$$
\int_0^3 x^2\,dx \approx \frac{3\cdot 1}{8}\big(0+3\cdot 1+3\cdot 4+9\big)
=\frac{3}{8}(0+3+12+9)=\frac{3}{8}\cdot 24=9.
$$

Exact integral: $\bigl[x^3/3\bigr]_0^3=9$. Exact again for a quadratic.

**Counterexample of a wrong formula:** applying trapezoidal-style weights $h/3(y_0+4\sum y_i+y_n)$ with $h=1$ on $[0,4]$ is **not** Simpson 3/8 and need not be accurate; always use $3h/8$ with pattern $1,3,3,1$ per block of three subintervals.

## Common Failure Modes

- Using coefficient $h/3$ instead of $3h/8$
- $n$ not a multiple of 3
- Confusing with composite Simpson 1/3 weights $1,4,2,4,\ldots$

## Connections

- [[Regra de Simpson (um terço)]]
- [[Regra dos Trapézios]]
- [[Métodos Numéricos]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Simpson’s 3/8 rule; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
