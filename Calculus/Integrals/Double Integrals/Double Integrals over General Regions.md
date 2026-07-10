---
dg-publish: true
tags:
  - calculus
  - integrals
  - multivariable
---

# Double Integrals over General Regions

## Summary

To integrate over a nonrectangular plane region $D$, describe $D$ as a Type I region (functions of $x$ as vertical bounds) or Type II region (functions of $y$ as horizontal bounds), then write an iterated integral with variable limits.

## Prerequisites

[[Double Integrals]], [[Fubini's Theorem]]

## Definition / Procedure

### Type I

$$
D=\{(x,y):a\le x\le b,\ g_1(x)\le y\le g_2(x)\},
\qquad
\iint_D f\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx.
$$

### Type II

$$
D=\{(x,y):c\le y\le d,\ h_1(y)\le x\le h_2(y)\},
\qquad
\iint_D f\,dA=\int_c^d\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy.
$$

Sketch $D$, choose the description that yields simple limits, and evaluate the inner integral first.

## Conditions / Assumptions

- $f$ continuous on the closed bounded region $D$.
- Bounding curves $g_i$, $h_i$ continuous.

## Worked Example

Let $D$ be the triangle with vertices $(0,0)$, $(1,0)$, $(1,1)$, so $0\le x\le 1$ and $0\le y\le x$. For $f=1$,

$$
\iint_D 1\,dA=\int_0^1\int_0^x 1\,dy\,dx=\int_0^1 x\,dx=\frac{1}{2}
$$

(the area of the triangle). As Type II: $0\le y\le 1$, $y\le x\le 1$ gives the same area.

## Common Mistakes

- Using constant limits on a nonrectangular region.
- Reversing order without recomputing bounds from a sketch.

## Connections

- [[Fubini's Theorem]], [[Double Integrals in Polar Coordinates]] for circular regions

## References

General plane regions appear in OpenStax Calculus Volume 3.[^openstax-genreg]

[^openstax-genreg]: OpenStax, *Calculus Volume 3*, Section 5.2, https://openstax.org/details/books/calculus-volume-3
