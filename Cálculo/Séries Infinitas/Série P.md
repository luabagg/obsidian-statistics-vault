---
dg-publish: true
tags:
  - calculus
  - series
---

# $p$-Series

## Summary

The $p$-series $\sum_{n=1}^\infty 1/n^p$ converges if and only if $p>1$, and diverges if $p\le 1$. The case $p=1$ is the harmonic series. The term test alone cannot prove divergence when $1/n^p\to 0$ (which holds for all $p>0$).

## Prerequisites

[[Série Harmônica]], [[Teste da Integral]]

## Theorem

For real $p$,

$$
\sum_{n=1}^\infty\frac{1}{n^p}
\begin{cases}
\text{converges}, & p>1,\\
\text{diverges}, & p\le 1.
\end{cases}
$$

Proof sketch: integral test with $f(x)=x^{-p}$ on $[1,\infty)$.

## Worked Example

- $\sum 1/n^2$ converges; in fact $\sum_{n=1}^\infty 1/n^2=\pi^2/6=\zeta(2)$.
- $\sum 1/\sqrt{n}$ diverges ($p=1/2\le 1$), even though terms $\to 0$.
- $\sum n=\sum n^{-(-1)}$ diverges ($p=-1\le 1$).

## Common Mistakes

- Claiming divergence of $\sum 1/n^p$ for $p>0$ solely because “terms do not go to zero”—they do go to zero for $p>0$; divergence for $0<p\le 1$ needs integral/comparison tests.
- Saying the series converges for $p\ge 1$ (false at $p=1$).

## Connections

- [[Teste da Integral]], [[Testes de Comparação]], [[Série Harmônica]]

## References

$p$-series are classified via the integral test in OpenStax Calculus Volume 2.[^openstax-pseries]

[^openstax-pseries]: OpenStax, *Calculus Volume 2*, Section 5.3, https://openstax.org/details/books/calculus-volume-2
