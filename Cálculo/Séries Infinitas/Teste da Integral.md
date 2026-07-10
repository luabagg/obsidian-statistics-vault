---
dg-publish: true
tags:
  - calculus
  - series
---

# Integral Test

## Summary

For a positive, continuous, eventually decreasing function $f$, the series $\sum f(n)$ and the improper integral $\int_1^\infty f(x)\,dx$ either both converge or both diverge.

## Prerequisites

[[Integrais]], improper integrals, [[Sequências]]

## Theorem

Let $f$ be positive, continuous, and decreasing on $[N,\infty)$ for some integer $N\ge 1$. Then

$$
\sum_{n=N}^\infty f(n)\quad\text{converges}\iff\int_N^\infty f(x)\,dx\text{ converges}.
$$

## Worked Example

For $f(x)=x^{-p}$ ($p>0$):

$$
\int_1^\infty x^{-p}\,dx
$$

converges if and only if $p>1$. Thus $\sum 1/n^p$ converges iff $p>1$ (see [[Série P]]).

For $\sum 1/\sqrt{n}$, $\int_1^\infty x^{-1/2}\,dx=\infty$, so the series diverges.

## Common Mistakes

- Using the integral’s value as the sum of the series (they are not equal; the integral only decides convergence and bounds remainders).
- Applying the test when $f$ is not eventually decreasing.

## Connections

- [[Série P]], [[Série Harmônica]], remainder bounds in [[Estimativa Para a Soma de uma Série]]

## References

The integral test is in OpenStax Calculus Volume 2.[^openstax-inttest]

[^openstax-inttest]: OpenStax, *Calculus Volume 2*, Section 5.3, https://openstax.org/details/books/calculus-volume-2
