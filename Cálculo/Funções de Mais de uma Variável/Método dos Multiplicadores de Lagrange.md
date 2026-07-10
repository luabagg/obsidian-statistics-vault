---
dg-publish: true
tags:
  - calculus
  - multivariable
  - optimization
---

# Method of Lagrange Multipliers

## Summary

Lagrange multipliers locate constrained extrema of $f$ subject to $g=\text{constant}$ by solving $\nabla f=\lambda\nabla g$ together with the constraint. Critical points of the Lagrangian must still be classified (max, min, or saddle-type on the constraint).

## Prerequisites

[[Derivadas Parciais]], [[Valores de Máximo e Mínimo]], gradients

## Theorem / Procedure

To extremize $f(\mathbf{x})$ subject to $g(\mathbf{x})=c$ (one constraint), introduce $\lambda$ and solve

$$
\nabla f(\mathbf{x})=\lambda\nabla g(\mathbf{x}),\qquad g(\mathbf{x})=c,
$$

equivalently $\nabla L=\mathbf{0}$ for

$$
L(\mathbf{x},\lambda)=f(\mathbf{x})-\lambda\bigl(g(\mathbf{x})-c\bigr).
$$

## Conditions / Assumptions

- $f$ and $g$ are $C^1$ near the solution.
- $\nabla g\neq\mathbf{0}$ at candidate points (constraint qualification).
- On a **closed bounded** constraint set (compact), extrema exist; on unbounded constraints, there may be no maximum or no minimum.

## Worked Example

Optimize $f(x,y)=x^2+y^2$ subject to $x+y=1$.

Solve $2x=\lambda$, $2y=\lambda$, $x+y=1$. Then $x=y=1/2$, so the only critical point is $(1/2,1/2)$ with $f=1/2$.

On the line $x+y=1$, $f(x,1-x)=x^2+(1-x)^2=2x^2-2x+1$, whose graph is a parabola opening upward. Thus $(1/2,1/2)$ is a **minimum**, not a maximum. As $|x|\to\infty$ along the line, $f\to\infty$, so **no maximum exists**.

A corrected “maximize” example: maximize $f(x,y)=xy$ on $x+y=1$ with $x,y\ge 0$ (compact segment) yields maximum $1/4$ at $(1/2,1/2)$.

## Common Mistakes

- Reporting a Lagrange critical point as a maximum without checking the constraint geometry.
- Ignoring points where $\nabla g=\mathbf{0}$.
- Forgetting that unbounded constraints need behavior at infinity.

## Connections

- Unconstrained test: [[Valores de Máximo e Mínimo]]
- Geometry: $\nabla f$ parallel to $\nabla g$ means level curves of $f$ and $g$ share a tangent

## References

Lagrange multipliers are treated in OpenStax Calculus Volume 3.[^openstax-lagrange]

[^openstax-lagrange]: OpenStax, *Calculus Volume 3*, Section 4.8, https://openstax.org/details/books/calculus-volume-3
