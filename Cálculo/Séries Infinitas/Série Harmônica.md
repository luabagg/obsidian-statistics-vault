---
dg-publish: true
tags:
  - calculus
  - series
---

# Harmonic Series

## Summary

The harmonic series $\sum 1/n$ diverges, even though its terms tend to zero. Partial sums grow like $\ln n+\gamma$. Rearrangement theorems apply to the **alternating** harmonic series, not to the divergent ordinary harmonic series.

## Prerequisites

[[Soma de Séries por Somas Parciais]], [[Teste da Integral]]

## Definition

$$
\sum_{n=1}^\infty\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots.
$$

The $n$th harmonic number is $H_n=\sum_{k=1}^n 1/k$.

## Theorem

The harmonic series **diverges**. One proof uses the integral test:

$$
\int_1^\infty\frac{1}{x}\,dx=\infty,
$$

so $\sum 1/n$ diverges. Grouping also shows $H_{2^m}\ge 1+m/2\to\infty$.

Asymptotically,

$$
H_n=\ln n+\gamma+o(1),
$$

where $\gamma\approx 0.57721$ is the Euler–Mascheroni constant.

## Worked Example

$H_5=1+1/2+1/3+1/4+1/5=137/60$.

The alternating harmonic series $\sum(-1)^{n+1}/n$ converges (to $\ln 2$) and is conditionally convergent; **its** rearrangements can change the sum. The ordinary harmonic series does not converge, so it has no finite sum to rearrange.

## Common Mistakes

- Believing $a_n\to 0$ implies convergence (false; harmonic is the classic counterexample).
- Attributing Riemann’s rearrangement theorem to $\sum 1/n$ itself.

## Connections

- [[Série P]] ($p=1$ boundary case)
- [[Séries Alternadas]], [[Convergência Absoluta]]

## References

Divergence of the harmonic series is standard in OpenStax Calculus Volume 2.[^openstax-harm]

[^openstax-harm]: OpenStax, *Calculus Volume 2*, Section 5.2–5.3, https://openstax.org/details/books/calculus-volume-2
