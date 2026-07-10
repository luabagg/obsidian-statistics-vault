---
dg-publish: true
tags:
  - precalculus
  - polynomials
  - rational-functions
aliases:
  - Polynomials
  - Rational Functions
---

# Polynomials and Rational Functions

## Summary

Polynomials are continuous, smooth algebraic building blocks. Rational functions are ratios of polynomials and introduce vertical asymptotes, holes, and horizontal (or slant) asymptotes. Together they support equation solving, graphing, and limits in calculus.

## Prerequisites

[[Functions]]. Hub: [[Pre-Calculus]].

## Definition / Statement

A **polynomial** of degree $n$ (with $n$ a nonnegative integer) has the form

$$
p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0,
$$

where $a_n \neq 0$ and coefficients $a_i$ are real (or complex). A constant nonzero polynomial has degree $0$; the zero polynomial is often assigned no degree or degree $-\infty$.

A **rational function** is

$$
r(x) = \frac{p(x)}{q(x)},
$$

where $p$ and $q$ are polynomials and $q$ is not the zero polynomial. The domain of $r$ is all $x$ with $q(x) \neq 0$.

## Notation

| Symbol | Meaning |
|---|---|
| $\deg(p)$ | degree of polynomial $p$ |
| $a_n$ | leading coefficient of $p$ |
| $r(x)=p(x)/q(x)$ | rational function |
| hole | removable discontinuity after canceling a common factor |

## Conditions / Assumptions

- Real coefficients unless stated otherwise.
- Domain of $r$ excludes roots of the denominator.
- Before analyzing asymptotes, reduce $r$ by canceling common factors of $p$ and $q$ (over the reals or as factored forms allow). Canceled factors produce **holes**, not vertical asymptotes.

## Main Result / Formula

**End behavior of a polynomial** (leading term $a_n x^n$ dominates as $|x|\to\infty$):

- If $n$ is even and $a_n > 0$: $p(x) \to +\infty$ as $x \to \pm\infty$.
- If $n$ is even and $a_n < 0$: $p(x) \to -\infty$ as $x \to \pm\infty$.
- If $n$ is odd and $a_n > 0$: $p(x) \to -\infty$ as $x \to -\infty$, and $p(x) \to +\infty$ as $x \to +\infty$.
- If $n$ is odd and $a_n < 0$: the opposite one-sided limits at infinity.

**Zeros**: if $p(c)=0$, then $(x-c)$ is a factor of $p$ (Factor Theorem).

**Vertical asymptotes of a reduced rational function**: if $q(c)=0$ and $p(c)\neq 0$ after reduction, then $x=c$ is a vertical asymptote.

**Horizontal asymptotes** for $r(x)=p(x)/q(x)$ with $\deg(p)=m$, $\deg(q)=n$, leading coefficients $a$ and $b$:

- If $m < n$: $y = 0$ is a horizontal asymptote.
- If $m = n$: $y = a/b$ is a horizontal asymptote.
- If $m = n+1$: no horizontal asymptote; there is a **slant (oblique) asymptote** found by polynomial division.
- If $m > n+1$: no horizontal or slant asymptote of that simple type; the end behavior is polynomial-like.

## Worked Example

Consider

$$
r(x) = \frac{x^2 - 1}{x^2 - x - 2} = \frac{(x-1)(x+1)}{(x-2)(x+1)}.
$$

For $x \neq -1$, cancel $(x+1)$:

$$
r(x) = \frac{x-1}{x-2}, \quad x \neq -1.
$$

- Hole at $x = -1$ (common factor), with height $\frac{-1-1}{-1-2} = \frac{2}{3}$ on the reduced form.
- Vertical asymptote: $x = 2$.
- Degrees equal, leading coefficients both $1$ on the unreduced form (and reduced form also degree $1$ over $1$): horizontal asymptote $y = 1$.

## Common Mistakes

- Calling every denominator zero a vertical asymptote without canceling first (holes vs. asymptotes).
- Forgetting domain restrictions after canceling.
- Mixing horizontal-asymptote cases when degrees differ by more than one.
- Treating “end behavior of $p$” as if constant term mattered for large $|x|$.

## Connections

- Related: [[Functions]], [[Exponentials and Logarithms]]
- Next: [[Trigonometry]] or [[Exponentials and Logarithms]]
- Later: limits at infinity and discontinuities in [[Calculus]]; completing the square in [[Completing the Square]]

## References

Polynomial and rational graph features follow OpenStax Precalculus treatment of polynomial and rational functions.[^openstax-poly]

[^openstax-poly]: OpenStax, *Precalculus 2e*, Polynomial and Rational Functions, https://openstax.org/details/books/precalculus-2e
