---
dg-publish: true
tags:
  - calculus
  - limits
  - multivariable
---

# Limits and Continuity of Functions of Two Variables

## Summary

For $f(x,y)$, the limit as $(x,y)\to(a,b)$ must approach the same value along **every** path in the plane. Different path limits prove nonexistence; matching on several paths never proves existence by itself. Continuity requires the limit to exist and equal the function value.

## Prerequisites

[[Limits]], [[Multivariable Functions]]

## Definition

$$
\lim_{(x,y)\to(a,b)}f(x,y)=L
$$

means: for every $\varepsilon>0$ there exists $\delta>0$ such that

$$
0<\sqrt{(x-a)^2+(y-b)^2}<\delta \implies |f(x,y)-L|<\varepsilon.
$$

The function $f$ is continuous at $(a,b)$ if $f(a,b)$ is defined and

$$
\lim_{(x,y)\to(a,b)}f(x,y)=f(a,b).
$$

## Conditions / Assumptions

- **Direct substitution** is valid when $f$ is known continuous at $(a,b)$ (polynomials, rational functions off their zero-denominator sets, compositions of continuous functions).
- Path tests: if two paths give different limits, the two-variable limit **does not exist**. Agreement on many paths is inconclusive for existence.

## Worked Example

Consider

$$
f(x,y)=\frac{x^2-y^2}{x^2+y^2},\qquad (x,y)\neq(0,0).
$$

- Along $y=0$: $\lim_{x\to 0}f(x,0)=1$.
- Along $y=x$: $\lim_{x\to 0}f(x,x)=0$.

The path limits disagree, so $\lim_{(x,y)\to(0,0)}f(x,y)$ does not exist. Defining $f(0,0)=1$ (or any value) cannot make $f$ continuous at the origin.

By contrast, $g(x,y)=x^2+y^2$ is continuous everywhere by the polynomial continuity theorem, so $\lim_{(x,y)\to(a,b)}g(x,y)=a^2+b^2$ by substitution.

## Common Mistakes

- Using direct substitution when the expression is undefined or the candidate is not continuous.
- Concluding that a limit exists because it is the same along lines $y=mx$ only.
- Typo-level confusion between continuity ($L=f(a,b)$) and mere existence of $L$.

## Connections

- Next: [[Partial Derivatives]], [[Differentiability of a Function]]
- Path issues reappear for directional derivatives vs total differentiability

## References

Multivariable limits and continuity are treated in OpenStax Calculus Volume 3.[^openstax-mv-limits]

[^openstax-mv-limits]: OpenStax, *Calculus Volume 3*, Section 4.2, https://openstax.org/details/books/calculus-volume-3
