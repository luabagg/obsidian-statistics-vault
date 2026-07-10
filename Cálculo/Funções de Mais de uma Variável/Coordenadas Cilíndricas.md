---
dg-publish: true
tags:
  - calculus
  - multivariable
  - coordinates
---

# Cylindrical Coordinates

## Summary

Cylindrical coordinates $(r,\theta,z)$ extend polar coordinates by a vertical $z$. They suit problems with axial symmetry about the $z$-axis. The volume element is $r\,dr\,d\theta\,dz$.

## Prerequisites

[[Coordenadas Polares]]

## Definition

- $r=\sqrt{x^2+y^2}\ge 0$: distance from the $z$-axis.
- $\theta$: angle in the $xy$-plane from the positive $x$-axis, typically $[0,2\pi)$ or $(-\pi,\pi]$.
- $z$: same as Cartesian $z$.

Cartesian relations:

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad z=z.
$$

## Inverse Formulas

$$
r=\sqrt{x^2+y^2},\qquad
\theta=\operatorname{atan2}(y,x),\qquad
z=z.
$$

Use $\operatorname{atan2}(y,x)$ (two-argument arctangent), not $\arctan(y/x)$ alone, so the quadrant is correct when $x\le 0$.

## Formula

Volume element:

$$
dV=r\,dr\,d\theta\,dz.
$$

Gradient in orthonormal cylindrical basis (for reference):

$$
\nabla f=\frac{\partial f}{\partial r}\mathbf{e}_r+\frac{1}{r}\frac{\partial f}{\partial\theta}\mathbf{e}_\theta+\frac{\partial f}{\partial z}\mathbf{e}_z\quad(r>0).
$$

## Conditions / Assumptions

- $r=0$ is the entire $z$-axis; $\theta$ is undefined there.
- Jacobian factor $r$ is required for integrals.

## Worked Example

Cartesian point $(2\sqrt{3},\,6,\,4)$:

$$
r=\sqrt{12+36}=\sqrt{48}=4\sqrt{3},\qquad
\theta=\operatorname{atan2}(6,2\sqrt{3})=\pi/3,\qquad
z=4.
$$

So $(r,\theta,z)=(4\sqrt{3},\pi/3,4)$.

## Common Mistakes

- Using $\theta=\arctan(y/x)$ without quadrant correction.
- Omitting the factor $r$ in triple integrals.
- Allowing negative $r$ without adjusting $\theta$ by $\pi$.

## Connections

- [[Coordenadas Polares]], [[Coordenadas Esféricas]], [[Integrais Triplas]]

## References

Cylindrical coordinates appear in OpenStax Calculus Volume 3.[^openstax-cyl]

[^openstax-cyl]: OpenStax, *Calculus Volume 3*, Section 5.5, https://openstax.org/details/books/calculus-volume-3
