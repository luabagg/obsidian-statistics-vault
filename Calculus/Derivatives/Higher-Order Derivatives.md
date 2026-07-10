---
dg-publish: true
tags:
  - calculus
  - derivatives
---

# Higher-Order Derivatives

## Summary

Higher-order derivatives are derivatives of derivatives. The second derivative $f''$ measures how the first derivative changes (concavity in one variable). Mixed partials of several variables are related by Clairaut’s theorem under continuity hypotheses.

## Prerequisites

[[Derivatives]], [[Partial Derivatives]]

## Definition

For a single-variable function,

$$
f''(x)=\frac{d}{dx}f'(x)=\frac{d^2f}{dx^2},
$$

and inductively $f^{(n)}=\frac{d}{dx}f^{(n-1)}$.

For $f(x,y)$, second partials include $f_{xx}$, $f_{yy}$, and mixed partials $f_{xy}$, $f_{yx}$.

## Conditions / Assumptions

- Each differentiation step requires differentiability of the previous derivative on the region of interest.
- Equality of mixed partials $f_{xy}=f_{yx}$ holds when those partials are continuous (Clairaut); see [[Clairaut's Theorem]].

## Worked Example

If $f(x)=x^3$, then $f'(x)=3x^2$, $f''(x)=6x$, $f'''(x)=6$, and $f^{(n)}(x)=0$ for $n\ge 4$.

If $g(x)=e^x$, then $g^{(n)}(x)=e^x$ for every $n\ge 0$.

For $f(x,y)=x^2 y$, $f_x=2xy$, $f_{xy}=2x$, $f_{yx}=2x$.

## Common Mistakes

- Claiming that the Newtonian potential $1/r$ is harmonic in **two** dimensions. In $\mathbb{R}^2\setminus\{0\}$, $\ln r$ is harmonic (away from the origin), while $1/r$ is harmonic in three dimensions (Coulomb potential), not in 2D.
- Omitting mixed-partial continuity hypotheses when swapping differentiation order.

## Connections

- [[Clairaut's Theorem]], [[Maxima and Minima]] (Hessian uses second partials)
- Series: Taylor polynomials use $f^{(n)}$

## References

Higher derivatives and notation appear in OpenStax Calculus Volume 1; mixed partials in Volume 3.[^openstax-higher]

[^openstax-higher]: OpenStax, *Calculus Volume 1*, Section 3.7; *Calculus Volume 3*, Section 4.3, https://openstax.org/details/books/calculus-volume-1
