---
dg-publish: true
tags:
  - calculus
  - series
---

# Ratio Test

## Summary

The ratio test examines $L=\lim|a_{n+1}/a_n|$. Absolute convergence holds if $L<1$; divergence if $L>1$; the test is inconclusive if $L=1$.

## Prerequisites

[[Absolute Convergence]], factorials and exponentials helpful

## Theorem

For $\sum a_n$, if

$$
L=\lim_{n\to\infty}\Bigl|\frac{a_{n+1}}{a_n}\Bigr|
$$

exists, then:

- $L<1$: absolute convergence;
- $L>1$ or $L=\infty$: divergence;
- $L=1$: inconclusive (e.g. all $p$-series).

## Worked Example

$\sum (1/2)^n$: $L=1/2<1$, absolute convergence.

$\sum n!/(2n)!$:

$$
\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\frac{n+1}{(2n+2)(2n+1)}\to 0<1,
$$

so absolute convergence.

For $\sum x^n/n$, $L=|x|$: absolute convergence when $|x|<1$, divergence when $|x|>1$; endpoints need separate checks.

## Common Mistakes

- Concluding anything from $L=1$.
- Dropping absolute values for alternating terms when testing absolute convergence.

## Connections

- [[Root Test]], [[Power Series]] (radius via ratios of coefficients)

## References

The ratio test is in OpenStax Calculus Volume 2.[^openstax-ratio]

[^openstax-ratio]: OpenStax, *Calculus Volume 2*, Section 5.6, https://openstax.org/details/books/calculus-volume-2
