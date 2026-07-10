---
dg-publish: true
tags:
  - calculus
  - derivatives
---

# Implicit Differentiation

## Summary

When a relation $F(x,y)=C$ defines $y$ as a function of $x$ only implicitly, differentiate both sides with respect to $x$ and solve for $y'$. Use the chain rule on every term involving $y$.

## Prerequisites

[[Derivadas]], [[Regras da Cadeia]]

## Procedure

1. Differentiate each term of $F(x,y)=C$ with respect to $x$, treating $y=y(x)$.
2. Collect all terms that contain $y'$.
3. Solve linearly for $y'$.

For a level set $F(x,y)=C$ with $F_y\neq 0$,

$$
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$

## Conditions / Assumptions

- Local solvability for $y$ as a $C^1$ function of $x$ requires $F_y\neq 0$ at the point (implicit function theorem).
- At points where $F_y=0$ and $F_x\neq 0$, the tangent may be vertical.

## Worked Example

### Circle

From $x^2+y^2=100$,

$$
2x+2y\,y'=0\implies y'=-\frac{x}{y}\quad(y\neq 0).
$$

### Exponential relation (correct isolation)

From $e^{xy}+x^2-y^2=5$,

$$
e^{xy}\bigl(y+x y'\bigr)+2x-2y y'=0.
$$

Collect $y'$ terms:

$$
e^{xy}y + 2x + y'\bigl(x e^{xy}-2y\bigr)=0,
$$

so

$$
y'=\frac{-e^{xy}y-2x}{x e^{xy}-2y},
$$

provided the denominator is nonzero. Equivalently, $y'=-F_x/F_y$ with $F=e^{xy}+x^2-y^2$.

### Implicit partial derivatives

For $x^3+y^3+z^3+6xyz=1$ with $z=z(x,y)$,

$$
\frac{\partial z}{\partial x}=\frac{-(x^2+2yz)}{z^2+2xy},\qquad
\frac{\partial z}{\partial y}=\frac{-(y^2+2xz)}{z^2+2xy},
$$

when $z^2+2xy\neq 0$.

## Common Mistakes

- Forgetting the chain-rule factor $y'$ when differentiating $y^2$, $e^{xy}$, etc.
- Incorrect algebra when isolating $y'$ (must move all $y'$ terms to one side before dividing).
- Using $-F_x/F_y$ without checking $F_y\neq 0$.

## Connections

- Related formula for level curves: [[Regras da Cadeia]]
- Surfaces: [[Plano Tangente]]

## References

Implicit differentiation is developed in OpenStax Calculus Volume 1; the multivariable form uses the implicit function theorem setup in Volume 3.[^openstax-implicit]

[^openstax-implicit]: OpenStax, *Calculus Volume 1*, Section 3.8; *Calculus Volume 3*, Section 4.8, https://openstax.org/details/books/calculus-volume-1
