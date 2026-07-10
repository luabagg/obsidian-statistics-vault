---
dg-publish: true
tags:
  - geometry
  - analytic-geometry
  - lines
  - planes
aliases:
  - Lines
  - Planes
  - Parametric Line
---

# Lines and Planes

## Summary

Lines and planes are the basic flat objects of analytic geometry. Direction vectors describe lines; normal vectors describe planes. Cartesian, parametric, and point–direction forms convert geometry into solvable equations.

## Prerequisites

[[Distance and Midpoint]], [[Vectors and Dot Product]] (dot product for planes and angles). Hub: [[Geometria Analítica]].

## Object / Concept

- A **line** in $\mathbb{R}^2$ or $\mathbb{R}^3$ is determined by a point and a nonzero direction vector.
- A **plane** in $\mathbb{R}^3$ is determined by a point and a nonzero normal vector (or by a point and two nonparallel direction vectors).

## Coordinate System

Standard Cartesian coordinates in $\mathbb{R}^2$ or $\mathbb{R}^3$.

## Notation

| Symbol | Meaning |
|---|---|
| $\mathbf{r}_0 = (x_0,y_0,z_0)$ | a known point on the line/plane |
| $\mathbf{d} = \langle a,b,c \rangle$ | direction vector of a line |
| $\mathbf{n} = \langle A,B,C \rangle$ | normal vector to a plane |
| $t,s$ | real parameters |

## Conditions / Assumptions

- Direction vector $\mathbf{d} \neq \mathbf{0}$.
- Normal vector $\mathbf{n} \neq \mathbf{0}$.
- Two direction vectors spanning a plane must be linearly independent.

## Equations

### Line through $\mathbf{r}_0$ with direction $\mathbf{d}$

**Parametric form** (in $\mathbb{R}^3$):

$$
x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct, \quad t \in \mathbb{R}.
$$

**Vector form**:

$$
\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{d}.
$$

**Symmetric form** (when $a,b,c \neq 0$):

$$
\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}.
$$

### Line in the plane $\mathbb{R}^2$

Slope–intercept (nonvertical): $y = mx + b$.

Point–slope: $y - y_0 = m(x - x_0)$.

General linear: $Ax + By + C = 0$ with $(A,B)\neq(0,0)$.

Two distinct points $(x_1,y_1)$, $(x_2,y_2)$ determine slope

$$
m = \frac{y_2-y_1}{x_2-x_1}
$$

when $x_2 \neq x_1$; if $x_2=x_1$ the line is vertical: $x = x_1$.

### Plane through $\mathbf{r}_0$ with normal $\mathbf{n}=\langle A,B,C\rangle$

$$
A(x-x_0) + B(y-y_0) + C(z-z_0) = 0,
$$

or equivalently

$$
Ax + By + Cz + D = 0, \quad D = -(Ax_0+By_0+Cz_0).
$$

A point $\mathbf{r}$ lies on the plane if and only if $\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0)=0$.

## Worked Example

Line through $(1,2,3)$ parallel to $\langle 2,-1,4\rangle$:

$$
x=1+2t,\quad y=2-t,\quad z=3+4t.
$$

Plane through $(1,0,0)$ with normal $\langle 1,1,1\rangle$:

$$
1(x-1) + 1(y-0) + 1(z-0) = 0 \implies x + y + z = 1.
$$

## Common Mistakes

- Using a normal vector as if it were a direction vector of a line in the plane (they are orthogonal, not parallel).
- Writing symmetric form when a component of $\mathbf{d}$ is zero.
- Confusing “parallel to a plane” (direction $\perp$ normal) with “perpendicular to a plane” (direction $\parallel$ normal).

## Connections

- Related: [[Vectors and Dot Product]], [[Distance and Midpoint]]
- Next: [[Conic Sections]]; linear systems in [[Systems of Linear Equations]]
- Later: subspaces and hyperplanes in [[Vector Spaces and Bases]]

## References

Lines and planes in coordinates follow OpenStax Calculus Volume 3 (vectors and geometry of space).[^openstax-lines]

[^openstax-lines]: OpenStax, *Calculus Volume 3*, https://openstax.org/details/books/calculus-volume-3
