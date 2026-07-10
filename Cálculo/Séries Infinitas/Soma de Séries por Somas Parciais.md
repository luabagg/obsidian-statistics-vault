---
dg-publish: true
tags:
  - calculus
  - series
---

# Series Sums via Partial Sums

## Summary

The sum of an infinite series is defined as the limit of its partial sums. Closed forms for $S_n$ (geometric, telescoping) make convergence transparent.

## Prerequisites

[[Sequências]]

## Definition

For $\sum_{k=1}^\infty a_k$, the $n$th partial sum is

$$
S_n=\sum_{k=1}^n a_k=a_1+\cdots+a_n.
$$

The series converges to $S$ if and only if $\lim_{n\to\infty}S_n=S$.

## Worked Example

Geometric series with $a=1$, $r=1/2$:

$$
S_n=\sum_{k=0}^{n-1}\Bigl(\frac{1}{2}\Bigr)^k=\frac{1-(1/2)^n}{1-1/2}=2\bigl(1-2^{-n}\bigr)\to 2.
$$

General geometric partial sum ($r\neq 1$):

$$
S_n=a\frac{1-r^n}{1-r}.
$$

## Common Mistakes

- Identifying the series sum with a single term $a_n$.
- Using $S_n=a/(1-r)$ for finite $n$ without the $r^n$ correction.

## Connections

- [[Série Geométrica]], [[Série Telescópica]], [[Séries Infinitas]]

## References

Partial sums define series convergence in OpenStax Calculus Volume 2.[^openstax-partialsums]

[^openstax-partialsums]: OpenStax, *Calculus Volume 2*, Section 5.2, https://openstax.org/details/books/calculus-volume-2
