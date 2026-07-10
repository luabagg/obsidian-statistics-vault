---
dg-publish: true
tags:
  - calculus
  - series
---

# Telescoping Series

## Summary

A telescoping series has partial sums in which most intermediate terms cancel, leaving only a few boundary terms. The classic example comes from partial fractions of $1/(n(n+1))$. Telescoping series are **not** the same as Taylor series.

## Prerequisites

[[Series Sums by Partial Sums]], partial fractions

## Definition

A series $\sum a_n$ is telescoping if $a_n=b_n-b_{n+1}$ (or a short fixed-length difference) for some sequence $\{b_n\}$. Then

$$
S_N=\sum_{n=1}^N(b_n-b_{n+1})=b_1-b_{N+1},
$$

and $\sum_{n=1}^\infty a_n=\lim_{N\to\infty}S_N=b_1-\lim_{N\to\infty}b_{N+1}$ when the limit exists.

## Conditions / Assumptions

- Algebraic cancellation must be valid for the indices used.
- Convergence requires $\lim b_{N+1}$ to exist (finite).

## Worked Example

$$
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}.
$$

Partial sums:

$$
S_N=\sum_{n=1}^N\Bigl(\frac{1}{n}-\frac{1}{n+1}\Bigr)=1-\frac{1}{N+1}\to 1.
$$

Thus $\sum_{n=1}^\infty 1/(n(n+1))=1$.

## Common Mistakes

- Calling a Taylor expansion a “telescoping series.”
- Writing the false identity $1/x=\sum_{n=0}^\infty(-1)^n x^n$ as a telescoping series (that sum is the geometric series for $1/(1+x)$ when $|x|<1$, not $1/x$).

## Connections

- [[Geometric Series]] (another closed-form partial sum)
- Comparison and $p$-series for related rational terms: [[P Series]], [[Comparison Tests]]

## References

Telescoping examples appear with partial sums in OpenStax Calculus Volume 2.[^openstax-tele]

[^openstax-tele]: OpenStax, *Calculus Volume 2*, Section 5.2, https://openstax.org/details/books/calculus-volume-2
