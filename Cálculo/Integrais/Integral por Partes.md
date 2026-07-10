---
dg-publish: true
tags:
  - calculus
  - integrals
---

# Integration by Parts

## Summary

Integration by parts is the integral form of the product rule. Choose factors $u$ and $dv$ so that $\int v\,du$ is easier than $\int u\,dv$.

## Prerequisites

[[Integrais]], [[Derivadas]], product rule

## Formula

$$
\int u\,dv=uv-\int v\,du.
$$

For definite integrals,

$$
\int_a^b u\,dv=\bigl[uv\bigr]_a^b-\int_a^b v\,du.
$$

## Conditions / Assumptions

- $u$ and $v$ should be continuously differentiable on the interval of integration (sufficient for elementary use).
- Strategy (LIATE/ILATE heuristics): prefer $u$ to be a log, inverse trig, algebraic, trig, or exponential factor in that rough order—but check that $dv$ is easy to integrate.

## Worked Example

### Classic parts: $\int x e^x\,dx$

Let $u=x$, $dv=e^x\,dx$, so $du=dx$, $v=e^x$. Then

$$
\int x e^x\,dx=x e^x-\int e^x\,dx=x e^x-e^x+C=e^x(x-1)+C.
$$

### Substitution, not parts: $\int x^2 e^{x^3}\,dx$

Here the derivative of the exponent is proportional to $x^2$. Set $w=x^3$, $dw=3x^2\,dx$:

$$
\int x^2 e^{x^3}\,dx=\frac{1}{3}\int e^w\,dw=\frac{1}{3}e^{x^3}+C.
$$

Parts is the wrong primary tool for this integral.

## Common Mistakes

- Writing a broken formula that confuses antiderivatives of $u$ and $v$ with $u$ and $dv$.
- Using parts on a pure substitution problem such as $\int x^2 e^{x^3}\,dx$ and producing algebraically incorrect reductions.

## Connections

- Related techniques: [[Integrais]], [[Derivadas]], substitution, and reduction formulas
- Series: [[Séries Infinitas]] and term-by-term integration

## References

Integration by parts is in OpenStax Calculus Volume 2.[^openstax-parts]

[^openstax-parts]: OpenStax, *Calculus Volume 2*, Section 3.1, https://openstax.org/details/books/calculus-volume-2
