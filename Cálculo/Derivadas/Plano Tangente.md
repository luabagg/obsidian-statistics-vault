---
dg-publish: true
tags:
  - calculus
  - derivatives
  - multivariable
---

# Tangent Plane

## Summary

The tangent plane is the best linear approximation to a smooth surface $z=f(x,y)$ at a point. For an implicitly defined surface $F(x,y,z)=0$, the gradient $\nabla F$ is normal to the tangent plane.

## Prerequisites

[[Derivadas Parciais]], [[Diferenciabilidade de uma  Função]]

## Formula

### Graph $z=f(x,y)$

If $f$ is differentiable at $(x_0,y_0)$ and $z_0=f(x_0,y_0)$, the tangent plane is

$$
z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0).
$$

### Level surface $F(x,y,z)=0$

If $\nabla F(x_0,y_0,z_0)\neq\mathbf{0}$, the tangent plane is

$$
F_x(x_0,y_0,z_0)(x-x_0)+F_y(x_0,y_0,z_0)(y-y_0)+F_z(x_0,y_0,z_0)(z-z_0)=0.
$$

## Conditions / Assumptions

- Differentiability of $f$ (or $C^1$ partials as a convenient sufficient condition).
- For implicit surfaces, $\nabla F\neq\mathbf{0}$ at the point (regular point).

## Worked Example

For $z=x^2+y^2$ at $(1,1,2)$, $f_x=2x$, $f_y=2y$, so

$$
z-2=2(x-1)+2(y-1)\implies z=2x+2y-2.
$$

## Common Mistakes

- Using the plane equation without evaluating partials at the point of tangency.
- Dropping the $z$-term when the surface is given implicitly.

## Connections

- [[Diferencial de Uma Função]], [[Derivada Implícita]], [[Derivada Direcional]]

## References

Tangent planes are developed in OpenStax Calculus Volume 3.[^openstax-plane]

[^openstax-plane]: OpenStax, *Calculus Volume 3*, Section 4.4, https://openstax.org/details/books/calculus-volume-3
