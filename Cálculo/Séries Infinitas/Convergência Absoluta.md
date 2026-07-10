---
dg-publish: true
tags:
  - calculus
  - series
---

# Absolute Convergence

## Summary

A series $\sum a_n$ converges absolutely if $\sum |a_n|$ converges. Absolute convergence implies ordinary convergence. Series that converge but not absolutely are called conditionally convergent.

## Prerequisites

[[Séries Infinitas]], [[Séries Alternadas]], [[Teste da Razão]]

## Definition

- **Absolute convergence:** $\sum |a_n|$ converges.
- **Conditional convergence:** $\sum a_n$ converges but $\sum |a_n|$ diverges.

## Theorem

If $\sum |a_n|$ converges, then $\sum a_n$ converges. The converse is false: the alternating harmonic series converges, but $\sum 1/n$ diverges.

Absolutely convergent series may be rearranged freely without changing the sum; conditionally convergent series may not (Riemann rearrangement theorem).

## Worked Example

$\sum (1/2)^n$ converges absolutely.

$\sum (-1)^{n+1}/n$ converges conditionally.

$\sum x^n/n!$ converges absolutely for every real $x$ (ratio test / exponential series).

## Common Mistakes

- Equating “converges” with “converges absolutely.”
- Rearranging conditionally convergent series and expecting the same sum.

## Connections

- Tests that imply absolute convergence: [[Teste da Razão]], [[Teste da Raíz]], comparison on $|a_n|$
- [[Séries Alternadas]] for conditional examples

## References

Absolute vs conditional convergence is in OpenStax Calculus Volume 2.[^openstax-abs]

[^openstax-abs]: OpenStax, *Calculus Volume 2*, Section 5.5, https://openstax.org/details/books/calculus-volume-2
