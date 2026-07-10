---
dg-publish: true
tags:
  - calculus
  - integrals
---

# Riemann Sums

## Summary

A Riemann sum approximates a definite integral by summing sample heights times subinterval widths. Refining the partition makes the sum approach the integral when $f$ is Riemann integrable.

## Prerequisites

[[Limits]], [[Integrals]]

## Definition

Partition $[a,b]$ into $n$ subintervals of width $\Delta x=(b-a)/n$ (equal partitions for simplicity). Choose sample points $x_i^*$ in the $i$-th subinterval. The Riemann sum is

$$
\sum_{i=1}^n f(x_i^*)\Delta x.
$$

Common choices: left endpoints, right endpoints, or midpoints.

For a rectangle $[a,b]\times[c,d]$ and $f(x,y)$,

$$
\sum_{i=1}^{m}\sum_{j=1}^{n} f(x_i^*,y_j^*)\,\Delta x\,\Delta y.
$$

## Conditions / Assumptions

- Continuous functions on compact rectangles are Riemann integrable; the mesh of the partition must tend to zero.
- State whether left, right, or midpoint samples are used—do not mix them inconsistently.

## Worked Example

Approximate $\int_0^1 x^2\,dx$ with $n=4$ **midpoint** rule: $\Delta x=1/4$, midpoints $1/8,3/8,5/8,7/8$.

$$
\begin{aligned}
S_4&=\Bigl[\bigl(\tfrac{1}{8}\bigr)^2+\bigl(\tfrac{3}{8}\bigr)^2+\bigl(\tfrac{5}{8}\bigr)^2+\bigl(\tfrac{7}{8}\bigr)^2\Bigr]\cdot\frac{1}{4}\\
&=\bigl(\tfrac{1+9+25+49}{64}\bigr)\cdot\frac{1}{4}=\frac{84}{64}\cdot\frac{1}{4}=\frac{21}{64}=0.328125.
\end{aligned}
$$

The exact value is $1/3\approx 0.333\ldots$.

Double integral midpoint sample for $\iint_{[0,1]^2}xy\,dA$ with a $2\times 2$ grid: midpoints $(1/4,1/4)$, $(3/4,1/4)$, $(1/4,3/4)$, $(3/4,3/4)$, and $\Delta x\Delta y=(1/2)(1/2)=1/4$.

$$
S=\bigl(\tfrac{1}{16}+\tfrac{3}{16}+\tfrac{3}{16}+\tfrac{9}{16}\bigr)\cdot\frac{1}{4}=\bigl(1\bigr)\cdot\frac{1}{4}=\frac{1}{4},
$$

which matches $\int_0^1\int_0^1 xy\,dx\,dy=1/4$ exactly for this function and grid.

## Common Mistakes

- Using wrong sample points (e.g. calling endpoints “midpoints”).
- Multiplying by $\Delta x\Delta y$ incorrectly (using $0.25\cdot 0.25$ when each side step is $0.5$).

## Connections

- Limit of Riemann sums: definition of [[Integrals]]
- Multivariable: [[Double Integrals]], [[Fubini's Theorem]]

## References

Riemann sums are introduced in OpenStax Calculus Volume 1.[^openstax-riemann]

[^openstax-riemann]: OpenStax, *Calculus Volume 1*, Section 5.1–5.2, https://openstax.org/details/books/calculus-volume-1
