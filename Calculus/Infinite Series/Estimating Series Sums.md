---
dg-publish: true
tags:
  - calculus
  - series
---

# Estimating the Sum of a Series

## Summary

When a series converges, partial sums $S_N$ approximate the total sum $S$. Remainder bounds quantify the error $|S-S_N|$ using integral tails, alternating-series estimates, or exact remainders for geometric series.

## Prerequisites

[[Series Sums by Partial Sums]], [[Geometric Series]], [[Alternating Series]], [[Integral Test]]

## Formulas

### Geometric series (exact)

For $|r|<1$,

$$
\sum_{n=0}^\infty ar^n=\frac{a}{1-r},\qquad
R_N=\sum_{n=N+1}^\infty ar^n=\frac{ar^{N+1}}{1-r}.
$$

### Alternating series remainder

If $\sum(-1)^{n+1}b_n$ satisfies the alternating series test with $b_n\downarrow 0$, then

$$
|S-S_N|\le b_{N+1}.
$$

### Integral remainder (decreasing positive $f$)

If $a_n=f(n)$ with $f$ positive, continuous, and eventually decreasing,

$$
\int_{N+1}^\infty f(x)\,dx\le R_N\le\int_N^\infty f(x)\,dx
$$

(under standard integral-test hypotheses).

## Worked Example

For $\sum_{n=0}^\infty (1/2)^n$, the exact sum is $2$. After three terms $S_2=1+1/2+1/4=1.75$, the remainder is

$$
R_2=\frac{(1/2)^3}{1-1/2}=\frac{1}{4}=0.25,
$$

so $S=1.75+0.25=2$ exactly—not a hand-wavy “about $1.8$.”

For the alternating harmonic series, $|S-S_5|\le 1/6$.

## Common Mistakes

- Guessing remainders without a theorem (“looks like $1.8$”).
- Broken MathJax such as $\ln$n$ instead of $\ln n$.
- Using alternating bounds on non-alternating series.

## Connections

- [[Alternating Series]], [[Integral Test]], [[Taylor Series]] (Lagrange remainder)

## References

Remainder estimates appear with the integral and alternating tests in OpenStax Calculus Volume 2.[^openstax-est]

[^openstax-est]: OpenStax, *Calculus Volume 2*, Sections 5.3–5.5, https://openstax.org/details/books/calculus-volume-2
