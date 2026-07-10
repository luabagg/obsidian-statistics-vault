---
dg-publish: true
tags:
  - calculus
  - series
---

# Power Series

## Summary

A power series $\sum a_n(x-c)^n$ converges inside an open interval (or disk) centered at $c$ of radius $R$, and may or may not converge at the endpoints. The radius is often found with the ratio test.

## Prerequisites

[[Teste da Razão]], [[Série Geométrica]], [[Convergência Absoluta]]

## Definition

$$
\sum_{n=0}^\infty a_n(x-c)^n.
$$

## Radius of Convergence

If the following limit exists,

$$
R=\lim_{n\to\infty}\Bigl|\frac{a_n}{a_{n+1}}\Bigr|,
$$

with the conventions $R=0$ or $R=\infty$ when the limit is $0$ or $\infty$. Equivalently, if $L=\lim|a_{n+1}/a_n|$, then $R=1/L$ when $L$ exists in $[0,\infty]$.

(Do not invert the ratio formula inconsistently: $R=\lim|a_n/a_{n+1}|$, not $1/R=\lim|a_n/a_{n+1}|$ unless you define the limit the other way.)

Inside $|x-c|<R$ the series converges absolutely; outside $|x-c|>R$ it diverges. Endpoints $x=c\pm R$ require separate tests.

## Worked Example

Consider $\sum_{n=0}^\infty\bigl((x-2)/3\bigr)^n=\sum (1/3^n)(x-2)^n$.

Here $a_n=3^{-n}$, so

$$
R=\lim_{n\to\infty}\frac{3^{-n}}{3^{-(n+1)}}=3.
$$

Absolute convergence for $|x-2|<3$, i.e. $-1<x<5$.

- At $x=-1$: terms are $\bigl((-3)/3\bigr)^n=(-1)^n$, which do not tend to $0$ → **diverges**.
- At $x=5$: terms are $1^n=1\not\to 0$ → **diverges**.

Interval of convergence: $(-1,5)$.

## Common Mistakes

- Including an endpoint without checking the resulting numerical series.
- Writing that $\sum(-1)^n$ converges (it does not).

## Connections

- [[Série de Taylor]], [[Série de Maclaurin]], [[Série Binomial]]

## References

Power series and radius of convergence are in OpenStax Calculus Volume 2.[^openstax-power]

[^openstax-power]: OpenStax, *Calculus Volume 2*, Section 6.1, https://openstax.org/details/books/calculus-volume-2
