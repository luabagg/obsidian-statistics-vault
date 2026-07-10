---
dg-publish: true
---

# Midpoint Rule

## Summary

The composite midpoint rule approximates $\int_a^b f(x)\,dx$ by summing rectangle areas with heights evaluated at subinterval midpoints. It is a second-order method for smooth integrands.

## Prerequisites

- Definite integrals and partitions of $[a,b]$
- Boundedness of $f''$ for the error formula

## Problem Type

Approximate $I=\int_a^b f(x)\,dx$ from samples of $f$.

## Method Definition

Partition $[a,b]$ into $n$ equal parts of width $h=(b-a)/n$. On $[x_{i-1},x_i]$ with midpoint $m_i=x_{i-1}+h/2$,

$$
\int_{x_{i-1}}^{x_i} f(x)\,dx \approx h\, f(m_i).
$$

Composite rule:[^burden]

$$
\int_a^b f(x)\,dx \approx h\sum_{i=1}^{n} f\!\left(a+\bigl(i-\tfrac12\bigr)h\right).
$$

## Assumptions / Requirements

- $f$ continuous on $[a,b]$ (integrable)
- For the standard error bound, $f\in C^2[a,b]$

## Algorithm

1. Choose $n$, set $h=(b-a)/n$.
2. Sum $h\,f(a+(i-1/2)h)$ for $i=1,\ldots,n$.

## Error / Accuracy

If $|f''(x)|\le M$ on $[a,b]$, the composite midpoint error satisfies

$$
|E|\le \frac{(b-a)}{24}\, h^2 M = \frac{(b-a)^3}{24 n^2} M.
$$

Order $O(h^2)$, same order as the composite trapezoidal rule (with a smaller constant for many $f$).

## Worked Example

Approximate $\int_0^1 x^2\,dx=1/3$ with $n=2$ ($h=1/2$).

Midpoints: $1/4$, $3/4$.

$$
I\approx \frac12\Bigl((1/4)^2+(3/4)^2\Bigr)=\frac12\Bigl(\frac{1}{16}+\frac{9}{16}\Bigr)=\frac{5}{16}=0.3125.
$$

Error $|1/3-5/16|=1/48\approx 0.0208$. Bound with $f''=2$, $M=2$:

$$
\frac{(1)^3}{24\cdot 4}\cdot 2=\frac{1}{48},
$$

sharp on this example.

## Common Failure Modes

- Using endpoint samples instead of midpoints
- Applying the $O(h^2)$ bound when $f''$ is unbounded near an endpoint

## Connections

- [[Trapezoidal Rule]]
- [[Simpson 1-3 Rule]]
- [[Numerical Methods]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, midpoint / rectangle rules; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
