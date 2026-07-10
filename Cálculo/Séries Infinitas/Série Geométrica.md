---
dg-publish: true
tags:
  - calculus
  - series
---

# Geometric Series

## Summary

A geometric series has a constant ratio between consecutive terms. It converges precisely when $|r|<1$, with sum $a/(1-r)$.

## Prerequisites

[[Soma de Séries por Somas Parciais]]

## Definition

$$
\sum_{n=0}^\infty ar^n=a+ar+ar^2+\cdots.
$$

## Theorem

- If $|r|<1$, the series converges to $\dfrac{a}{1-r}$.
- If $|r|\ge 1$ and $a\neq 0$, the series diverges.

Special cases: $r=1$ gives $a+a+a+\cdots$; $r=-1$ oscillates; $r=0$ is the trivial one-term series $a$.

## Worked Example

With $a=2$, $r=1/2$:

$$
2+1+\frac{1}{2}+\frac{1}{4}+\cdots=\frac{2}{1-1/2}=4.
$$

## Common Mistakes

- Using $a/(1-r)$ when $|r|\ge 1$.
- Off-by-one errors in the starting index (sum from $n=1$ vs $n=0$).

## Connections

- [[Séries de Potências]], [[Teste da Razão]], remainder formulas in [[Estimativa Para a Soma de uma Série]]

## References

Geometric series are foundational in OpenStax Calculus Volume 2.[^openstax-geom]

[^openstax-geom]: OpenStax, *Calculus Volume 2*, Section 5.2, https://openstax.org/details/books/calculus-volume-2
