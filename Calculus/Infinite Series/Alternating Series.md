---
dg-publish: true
tags:
  - calculus
  - series
---

# Alternating Series

## Summary

An alternating series has terms that change sign. Leibniz’s test gives a simple convergence criterion, and the error after $N$ terms is at most the next unused term’s magnitude.

## Prerequisites

[[Sequences]], [[Series Sums by Partial Sums]]

## Definition

Typical forms:

$$
\sum_{n=1}^\infty (-1)^{n+1}b_n\quad\text{or}\quad\sum_{n=1}^\infty (-1)^n b_n,
$$

with $b_n\ge 0$.

## Theorem (Leibniz / alternating series test)

If $(b_n)$ is eventually monotone decreasing and $\lim_{n\to\infty}b_n=0$, then the alternating series converges.

### Remainder

If the hypotheses hold for all $n\ge 1$ (or from the first unused index onward),

$$
|S-S_N|\le b_{N+1}.
$$

## Worked Example

The alternating harmonic series

$$
\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots
$$

has $b_n=1/n\downarrow 0$, so it converges (to $\ln 2$). It does **not** converge absolutely.

For $\sum_{n=1}^\infty(-1)^{n+1}/2^n$, $b_n=2^{-n}$ decreases to $0$, so the series converges (in fact absolutely, since it is geometric with ratio $-1/2$).

## Common Mistakes

- Applying the test when $b_n$ is not eventually decreasing.
- Confusing conditional convergence with absolute convergence.
- Off-by-one index errors in remainder statements.

## Connections

- [[Absolute Convergence]], [[Estimating Series Sums]], [[Harmonic Series]]

## References

The alternating series test is in OpenStax Calculus Volume 2.[^openstax-alt]

[^openstax-alt]: OpenStax, *Calculus Volume 2*, Section 5.5, https://openstax.org/details/books/calculus-volume-2
