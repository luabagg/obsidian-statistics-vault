---
dg-publish: true
---

# Simpson’s Rule (1/3)

## Summary

Simpson’s 1/3 rule integrates a quadratic interpolant on two equal subintervals (three nodes). Composite Simpson is fourth-order accurate for smooth $f$ and exact for cubics.

## Prerequisites

- [[Regra dos Trapézios]]
- Even number of subintervals for the composite rule

## Problem Type

Approximate $\int_a^b f(x)\,dx$ with higher accuracy than the trapezoidal rule.

## Method Definition

**One panel (two subintervals):** set $h=(b-a)/2$ and nodes $a$, $a+h$, $b$.

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\Big(f(a)+4f(a+h)+f(b)\Big).
$$

**Composite rule:** $n$ even, $h=(b-a)/n$, $x_i=a+ih$:

$$
\int_a^b f \approx \frac{h}{3}\left(
f(x_0)+f(x_n)
+4\sum_{i\text{ odd}}f(x_i)
+2\sum_{i\text{ even},\,0<i<n}f(x_i)
\right).
$$

Weights pattern: $1,4,2,4,2,\ldots,4,1$.[^burden]

## Assumptions / Requirements

- $f$ continuous; for the classical error, $f\in C^4[a,b]$
- Composite: $n$ even

## Error / Accuracy

Single panel error involves $f^{(4)}(\xi)$ and is $O(h^5)$ locally; composite error is $O(h^4)$:

$$
E=-\frac{(b-a)}{180} h^4 f^{(4)}(\xi)
$$

for some $\xi\in(a,b)$.

## Worked Example

Compute $\int_0^1 x^2\,dx$ with one Simpson panel.

Here $h=(1-0)/2=1/2$, nodes $0$, $1/2$, $1$:

$$
\int_0^1 x^2\,dx \approx \frac{1/2}{3}\Big(0+4\cdot\bigl(\tfrac12\bigr)^2+1\Big)
=\frac{1}{6}\Big(0+4\cdot\frac14+1\Big)
=\frac{1}{6}\cdot 2=\frac13.
$$

Exact value is $1/3$ (Simpson is exact for quadratics). Using the wrong step $h=(b-a)/3$ would incorrectly produce $2/9$.

## Common Failure Modes

- Setting $h=(b-a)/3$ for the three-point formula (incorrect)
- Composite rule with odd $n$
- Mixing 1/3 and 3/8 weight patterns

## Connections

- [[Regra de Simpson (três oitavos)]]
- [[Regra dos Trapézios]]
- [[Métodos Numéricos]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Simpson’s rules; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
