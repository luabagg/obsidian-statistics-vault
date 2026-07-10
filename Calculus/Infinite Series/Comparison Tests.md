---
dg-publish: true
tags:
  - calculus
  - series
---

# Comparison Tests

## Summary

Comparison tests decide convergence of series with nonnegative terms by relating them to a known series. The direct comparison test uses inequalities; the limit comparison test uses asymptotic ratios.

## Prerequisites

[[P Series]], [[Geometric Series]], [[Harmonic Series]]

## Theorems

### Direct comparison

Assume $0\le a_n\le b_n$ for all $n$ large.

- If $\sum b_n$ converges, then $\sum a_n$ converges.
- If $\sum a_n$ diverges, then $\sum b_n$ diverges.

### Limit comparison

If $a_n>0$, $b_n>0$, and

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=L\in(0,\infty),
$$

then $\sum a_n$ and $\sum b_n$ both converge or both diverge.

## Worked Example

### Correct comparison for $1/(n(n+1))$

For $n\ge 1$, $0<\dfrac{1}{n(n+1)}<\dfrac{1}{n^2}$. Since $\sum 1/n^2$ converges ($p=2$), so does $\sum 1/(n(n+1))$.

Alternatively, partial fractions show the series telescopes to $1$.

### False claim to avoid

The inequality $\dfrac{1}{n(n+1)}<\dfrac{1}{2^n}$ is **not** true for all large $n$. Polynomial decay is slower than exponential decay, so $1/(n(n+1))\gg 1/2^n$ as $n\to\infty$. Do not compare this series to a geometric series via a false bound.

### Limit comparison

For $a_n=1/(n^2+n)$ and $b_n=1/n^2$, $a_n/b_n\to 1$, so $\sum a_n$ converges.

## Common Mistakes

- Comparing with the wrong direction of the inequality.
- Using a false geometric bound for rational terms.
- Applying comparison tests to series with negative terms without absolute values.

## Connections

- [[P Series]], [[Integral Test]], [[Absolute Convergence]]

## References

Comparison tests are in OpenStax Calculus Volume 2.[^openstax-comp]

[^openstax-comp]: OpenStax, *Calculus Volume 2*, Section 5.4, https://openstax.org/details/books/calculus-volume-2
