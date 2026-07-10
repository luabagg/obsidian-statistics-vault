---
dg-publish: true
tags:
  - geometry
  - conic-sections
  - analytic-geometry
aliases:
  - Conics
  - Circle Ellipse Parabola Hyperbola
---

# Conic Sections

## Summary

Conic sections—circles, ellipses, parabolas, and hyperbolas—arise as plane slices of a cone and as quadratic curves in the plane. Standard forms make centers, foci, directrices, and axes readable after translation (often via completing the square).

## Prerequisites

[[Distance and Midpoint]], [[Completamento de quadrados]]. Helpful: [[Polynomials and Rational Functions]]. Hub: [[Geometria Analítica]].

## Object / Concept

A **conic section** is the set of points satisfying a second-degree equation

$$
Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
$$

(with not all of $A,B,C$ zero). When $B=0$ and axes are aligned with the coordinate axes, the standard forms below apply after translation.

## Coordinate System

Cartesian plane; standard forms assume axes parallel to the coordinate axes (no $xy$ term).

## Notation

| Symbol | Meaning |
|---|---|
| $(h,k)$ | center or vertex (as appropriate) |
| $a,b$ | semi-axis lengths (ellipse/hyperbola) |
| $p$ or $4p$ | focal length parameter for parabolas |
| $r$ | radius of a circle |

## Conditions / Assumptions

- Real points: some coefficient choices give empty sets, points, or degenerate pairs of lines.
- Forms below assume no rotation ($B=0$).
- For ellipse/hyperbola, $a>0$, $b>0$; for circle, $r>0$.

## Equations

**Circle** (center $(h,k)$, radius $r>0$)

$$
(x-h)^2 + (y-k)^2 = r^2.
$$

**Ellipse** (center $(h,k)$, axes parallel to coordinate axes)

$$
\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1.
$$

If $a>b$, major axis is horizontal; if $b>a$, major axis is vertical. For a circle, $a=b=r$.

**Parabola** (vertex $(h,k)$)

$$
\begin{aligned}
(y-k)^2 &= 4p(x-h) && \text{(opens horizontally)}, \\
(x-h)^2 &= 4p(y-k) && \text{(opens vertically)}.
\end{aligned}
$$

Focus is a distance $|p|$ from the vertex along the axis of symmetry.

**Hyperbola** (center $(h,k)$)

$$
\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1
\quad\text{(opens horizontally)},
$$
$$
\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1
\quad\text{(opens vertically)}.
$$

Asymptotes (horizontal-opening case):

$$
y-k = \pm \frac{b}{a}(x-h).
$$

## Visual / Geometric Interpretation

- Circle: constant distance from a center.
- Ellipse: sum of distances to two foci is constant.
- Parabola: equidistant from focus and directrix.
- Hyperbola: absolute difference of distances to two foci is constant.

## Worked Example

Identify $\dfrac{(x-1)^2}{9} + \dfrac{(y+2)^2}{4} = 1$.

- Ellipse, center $(1,-2)$.
- $a^2=9$, $b^2=4$ so $a=3$, $b=2$.
- Major axis horizontal; vertices at $(1\pm 3,-2)$, i.e. $(4,-2)$ and $(-2,-2)$.

## Common Mistakes

- Swapping $a^2$ and $b^2$ roles when deciding major-axis orientation for ellipses.
- Treating $x^2/a^2 - y^2/b^2 = -1$ without rewriting into a standard hyperbola form.
- Forgetting to complete the square before reading $(h,k)$.
- Using $r^2$ as radius instead of $r$.

## Connections

- Related: [[Completamento de quadrados]], [[Distance and Midpoint]], [[Lines and Planes]]
- Next: quadratic forms and eigenvalues in [[Eigenvalues and Eigenvectors]]
- Calculus: conics as level curves and optimization constraints

## References

Standard forms of conic sections follow OpenStax Precalculus analytic geometry.[^openstax-conics]

[^openstax-conics]: OpenStax, *Precalculus 2e*, Analytic Geometry, https://openstax.org/details/books/precalculus-2e
