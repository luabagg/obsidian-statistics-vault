---
dg-publish: true
tags:
  - calculus
  - series
---

# Taylor Series

## Summary

The Taylor series of $f$ about $a$ is the power series built from derivatives of $f$ at $a$. Truncations give polynomial approximations; Lagrange’s form bounds the remainder.

## Prerequisites

[[Higher-Order Derivatives]], [[Power Series]], [[Maclaurin Series]]

## Formula

$$
f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n,
$$

when the series represents $f$. The degree-$n$ Taylor polynomial is

$$
P_n(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

### Lagrange remainder

If $f^{(n+1)}$ exists on an interval containing $a$ and $x$, then

$$
f(x)=P_n(x)+R_n(x),\qquad
R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}
$$

for some $c$ between $a$ and $x$. Hence if $|f^{(n+1)}|\le M$ on that interval,

$$
|R_n(x)|\le\frac{M}{(n+1)!}|x-a|^{n+1}.
$$

### Radius via coefficients

If $a_n=f^{(n)}(a)/n!$ and $\lim|a_n/a_{n+1}|$ exists, that limit is the radius $R$.

## Worked Example

About $a=0$: $e^x$, $\sin x$, and $\cos x$ have the standard series with $R=\infty$.

For $\cos x$, $|f^{(n+1)}|\le 1$, so the remainder of $P_n$ satisfies $|R_n(x)|\le |x|^{n+1}/(n+1)!$.

## Common Mistakes

- Confusing the formal Taylor series with equality $f(x)=\text{series}$ without remainder control.
- Applying the ratio formula to $a_n(x-a)^n$ including the $(x-a)^n$ factor instead of pure coefficients.

## Connections

- [[Maclaurin Series]], [[Power Series]], [[Estimating Series Sums]]

## References

Taylor series and remainders are in OpenStax Calculus Volume 2.[^openstax-taylor]

[^openstax-taylor]: OpenStax, *Calculus Volume 2*, Section 6.3, https://openstax.org/details/books/calculus-volume-2
