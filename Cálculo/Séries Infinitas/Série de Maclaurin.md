---
dg-publish: true
tags:
  - calculus
  - series
---

# Maclaurin Series

## Summary

A Maclaurin series is a Taylor series centered at $0$. Many elementary functions have simple Maclaurin expansions used for approximation and analysis.

## Prerequisites

[[Série de Taylor]], [[Séries de Potências]], [[Derivadas de Ordem Superior]]

## Formula

If $f$ is infinitely differentiable at $0$, its Maclaurin series is

$$
f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(0)}{n!}x^n,
$$

when the series equals $f$ on an interval (checked via remainder theorems).

## Worked Example

$$
e^x=\sum_{n=0}^\infty\frac{x^n}{n!},\qquad
\sin x=\sum_{n=0}^\infty(-1)^n\frac{x^{2n+1}}{(2n+1)!},\qquad
\cos x=\sum_{n=0}^\infty(-1)^n\frac{x^{2n}}{(2n)!}.
$$

Each of these converges for all real $x$ (radius $R=\infty$).

## Common Mistakes

- Assuming every $C^\infty$ function equals its Maclaurin series (counterexamples exist; check remainders).
- Using degree-truncated polynomials without an error bound when accuracy matters.

## Connections

- General center: [[Série de Taylor]]
- Special case: [[Série Binomial]] for $(1+x)^\alpha$

## References

Maclaurin series are in OpenStax Calculus Volume 2.[^openstax-mac]

[^openstax-mac]: OpenStax, *Calculus Volume 2*, Section 6.3, https://openstax.org/details/books/calculus-volume-2
