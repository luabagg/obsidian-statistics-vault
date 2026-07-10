---
dg-publish: true
tags:
  - calculus
  - derivatives
  - multivariable
---

# Clairaut’s Theorem (Equality of Mixed Partials)

## Summary

If the mixed second partial derivatives of $f$ are continuous in a neighborhood of a point, then the order of differentiation does not matter: $f_{xy}=f_{yx}$ at that point.

## Prerequisites

[[Derivadas Parciais]], [[Derivadas de Ordem Superior]]

## Theorem

Let $f$ be defined on an open set containing $(a,b)$. If $f_{xy}$ and $f_{yx}$ exist on a neighborhood of $(a,b)$ and are continuous at $(a,b)$, then

$$
f_{xy}(a,b)=f_{yx}(a,b).
$$

## Conditions / Assumptions

- Continuity of the mixed partials is a standard sufficient condition.
- There exist pathological examples where mixed partials exist but are unequal when continuity fails; such examples are rare in applications.

## Worked Example

For $f(x,y)=x^3 y+2xy-5$,

$$
f_y=x^3+2x,\qquad f_{xy}=3x^2+2,
$$

$$
f_x=3x^2 y+2y,\qquad f_{yx}=3x^2+2.
$$

The mixed partials agree (and are continuous) on $\mathbb{R}^2$.

## Common Mistakes

- Assuming $f_{xy}=f_{yx}$ with no regularity hypothesis.
- Mixing subscript order conventions; here $f_{xy}=(f_x)_y$.

## Connections

- Used when forming the Hessian in [[Valores de Máximo e Mínimo]]
- Related to exact differentials and conservative fields (vector calculus)

## References

Clairaut’s theorem is stated in OpenStax Calculus Volume 3.[^openstax-clairaut]

[^openstax-clairaut]: OpenStax, *Calculus Volume 3*, Section 4.3, https://openstax.org/details/books/calculus-volume-3
