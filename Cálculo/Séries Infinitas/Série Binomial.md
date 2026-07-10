---
dg-publish: true
tags:
  - calculus
  - series
aliases:
  - Binomial Series
---

# Binomial Series

## Summary

The binomial series expands \((1+x)^\alpha\) for real (or complex) \(\alpha\) as a power series valid for \(|x|<1\). Coefficients use falling products, not ordinary factorials, when \(\alpha\) is not a nonnegative integer.

## Prerequisites

[[Série de Maclaurin]], [[Séries de Potências]]

## Main Result / Formula

\[
(1+x)^\alpha=\sum_{k=0}^\infty \binom{\alpha}{k} x^k,
\qquad |x|<1,
\]

where

\[
\binom{\alpha}{k}=\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}
\quad(k\ge 1),\qquad \binom{\alpha}{0}=1.
\]

If \(\alpha\) is a nonnegative integer, the series terminates and becomes the ordinary binomial theorem for all \(x\).

## Worked Example

\[
(1+x)^{-1/2}=1-\frac12 x+\frac{(-1/2)(-3/2)}{2!}x^2+\cdots,\qquad |x|<1.
\]

## Common Mistakes

- Writing \(\binom{\alpha}{k}=\alpha!/(k!(\alpha-k)!)\) for non-integer \(\alpha\).

## Connections

- Related: [[Série de Taylor]], [[Séries de Potências]]

## References

The generalized binomial series is standard advanced calculus material.[^ost2]

[^ost2]: OpenStax, *Calculus Volume 2*, https://openstax.org/details/books/calculus-volume-2
