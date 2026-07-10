---
dg-publish: true
tags:
  - geometry
  - analytic-geometry
aliases:
  - Distance Formula
  - Midpoint Formula
---

# Distance and Midpoint

## Summary

The distance formula is the Pythagorean theorem in coordinates. The midpoint formula averages coordinates. Together they define length and midpoints of segments in the plane and in space.

## Prerequisites

Coordinate plane (and optionally $\mathbb{R}^3$). Hub: [[Analytic Geometry]].

## Object / Concept

For points $P$ and $Q$, the **distance** $d(P,Q)$ is the Euclidean length of the segment $PQ$. The **midpoint** $M$ is the point halfway from $P$ to $Q$ along that segment.

## Coordinate System

Cartesian coordinates in $\mathbb{R}^2$ or $\mathbb{R}^3$ with the standard Euclidean metric.

## Notation

| Symbol | Meaning |
|---|---|
| $P=(x_1,y_1)$, $Q=(x_2,y_2)$ | points in the plane |
| $P=(x_1,y_1,z_1)$, $Q=(x_2,y_2,z_2)$ | points in space |
| $d(P,Q)$ | Euclidean distance |
| $M$ | midpoint of $PQ$ |

## Conditions / Assumptions

- Euclidean (Pythagorean) distance, not taxicab or other metrics.
- Real coordinates.

## Equations

**Plane**

$$
d(P,Q) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2},
$$
$$
M = \Biggl(\frac{x_1+x_2}{2},\, \frac{y_1+y_2}{2}\Biggr).
$$

**Space**

$$
d(P,Q) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2},
$$
$$
M = \Biggl(\frac{x_1+x_2}{2},\, \frac{y_1+y_2}{2},\, \frac{z_1+z_2}{2}\Biggr).
$$

**Circle** with center $C=(h,k)$ and radius $r > 0$: all points $P$ with $d(P,C)=r$, i.e.

$$
(x-h)^2 + (y-k)^2 = r^2.
$$

## Worked Example

Points $A=(1,2)$ and $B=(4,6)$:

$$
d(A,B) = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9+16} = 5,
$$
$$
M = \Biggl(\frac{1+4}{2},\, \frac{2+6}{2}\Biggr) = \Biggl(\frac{5}{2},\, 4\Biggr).
$$

## Common Mistakes

- Omitting the square root when a true distance (not squared distance) is required.
- Subtracting coordinates in inconsistent order (order cancels after squaring for distance, but midpoint needs correct averages).
- Using 2D formulas for points given in 3D.

## Connections

- Related: [[Completing the Square]], [[Vectors and Dot Product]], [[Conic Sections]]
- Next: [[Lines and Planes]]
- Linear algebra: norms via [[Orthogonality and Projections]]

## References

Distance and midpoint formulas are standard in OpenStax Precalculus analytic geometry.[^openstax-dist]

[^openstax-dist]: OpenStax, *Precalculus 2e*, https://openstax.org/details/books/precalculus-2e
