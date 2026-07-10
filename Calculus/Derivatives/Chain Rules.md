---
dg-publish: true
tags:
  - calculus
  - derivatives
aliases:
  - Chain Rule
---

# Chain Rule

## Summary

The chain rule differentiates compositions. In several variables it multiplies Jacobian factors along each path of dependence.

## Prerequisites

[[Derivatives]], [[Partial Derivatives]]

## Main Result / Formula

### One variable

If \(y=f(u)\) and \(u=g(x)\), then

\[
\frac{dy}{dx}=f'(u)\,g'(x).
\]

### Two variables, one independent

If \(z=f(x,y)\) and \(x=x(t)\), \(y=y(t)\), then

\[
\frac{dz}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}.
\]

Special case \(z=f(x,y)\) with \(x=g(y)\):

\[
\frac{dz}{dy}=f_x(g(y),y)\,g'(y)+f_y(g(y),y).
\]

### Implicit differentiation form

If \(F(x,y)=c\) defines \(y=y(x)\) with \(F_y\neq 0\), then

\[
\frac{dy}{dx}=-\frac{F_x}{F_y}.
\]

This is **not** a formula for \(\partial z/\partial y\) of an unconstrained \(z=f(x,y)\).

## Worked Example

Let \(z=x^2+y^2\) and \(x=t\), \(y=t^2\). Then

\[
\frac{dz}{dt}=2x\cdot 1+2y\cdot 2t=2t+4t^3.
\]

## Common Mistakes

- Writing \(\partial z/\partial y=(\partial z/\partial x)(\partial x/\partial y)\) and dropping the direct \(f_y\) term.
- Mixing the implicit formula \(-F_x/F_y\) into unconstrained partial derivatives.

## Connections

- Related: [[Implicit Differentiation]], [[Directional Derivative]], [[Chain Rules]]

## References

The multivariable chain rule is standard calculus.[^ost3]

[^ost3]: OpenStax, *Calculus Volume 3*, https://openstax.org/details/books/calculus-volume-3
