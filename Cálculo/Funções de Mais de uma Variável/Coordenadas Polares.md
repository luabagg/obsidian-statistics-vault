---
dg-publish: true
tags:
  - calculus
  - multivariable
  - coordinates
---

# Polar Coordinates

## Summary

Polar coordinates $(r,\theta)$ describe a plane point by distance from the origin and angle from the positive $x$-axis. They simplify circles, spirals, and many double integrals.

## Prerequisites

Prerequisites: trigonometry and the Cartesian plane.

## Formula

### Polar to Cartesian

$$
x=r\cos\theta,\qquad y=r\sin\theta.
$$

### Cartesian to polar

$$
r=\sqrt{x^2+y^2},\qquad
\theta=\operatorname{atan2}(y,x).
$$

The two-argument arctangent fixes the quadrant; $\arctan(y/x)$ alone is insufficient when $x\le 0$.

## Conditions / Assumptions

- Common ranges: $r\ge 0$ and $\theta\in[0,2\pi)$ or $(-\pi,\pi]$.
- Non-uniqueness: $(r,\theta)$ and $(r,\theta+2\pi k)$ represent the same ray; with signed radius, $(-r,\theta+\pi)$ is the same point as $(r,\theta)$.

## Worked Example

$(r,\theta)=(2,\pi/3)$ gives $x=2\cos(\pi/3)=1$, $y=2\sin(\pi/3)=\sqrt{3}$.

For area integrals, $dA=r\,dr\,d\theta$ (see [[Integrais Duplas em Coordenadas Polares]]).

## Common Mistakes

- Forgetting quadrant adjustments for $\theta$.
- Using $dA=dr\,d\theta$ without the Jacobian factor $r$.

## Connections

- Double integrals: [[Integrais Duplas em Coordenadas Polares]]
- 3D extensions: [[Coordenadas Cilíndricas]], [[Coordenadas Esféricas]]

## References

Polar coordinates are reviewed in OpenStax Calculus Volume 2/3 as needed for integration.[^openstax-polar]

[^openstax-polar]: OpenStax, *Calculus Volume 3*, Section 5.3, https://openstax.org/details/books/calculus-volume-3
