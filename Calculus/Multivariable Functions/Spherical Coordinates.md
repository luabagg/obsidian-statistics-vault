---
dg-publish: true
tags:
  - calculus
  - multivariable
  - coordinates
---

# Spherical Coordinates

## Summary

Spherical coordinates $(\rho,\theta,\phi)$ locate a point by distance from the origin, azimuth angle in the $xy$-plane, and polar angle down from the positive $z$-axis. They are ideal for spheres and cones about the $z$-axis. The volume element is $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.

## Prerequisites

[[Polar Coordinates]], [[Cylindrical Coordinates]], basic trigonometry

## Definition / Notation

Standard calculus convention (as in OpenStax):

| Symbol | Meaning | Range |
|--------|---------|-------|
| $\rho$ | distance from origin | $\rho\ge 0$ |
| $\theta$ | azimuth angle from positive $x$-axis in the $xy$-plane | $[0,2\pi)$ (or $[-\pi,\pi)$) |
| $\phi$ | polar angle from positive $z$-axis | $[0,\pi]$ |

Conversion to Cartesian:

$$
\begin{aligned}
x&=\rho\sin\phi\cos\theta,\\
y&=\rho\sin\phi\sin\theta,\\
z&=\rho\cos\phi.
\end{aligned}
$$

Inverse (principal values):

$$
\rho=\sqrt{x^2+y^2+z^2},\quad
\phi=\arccos\Bigl(\frac{z}{\rho}\Bigr)\ (\rho>0),\quad
\theta=\operatorname{atan2}(y,x).
$$

## Formula

Volume element:

$$
dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.
$$

## Geometric Sets

- $\rho=\text{const}$: sphere centered at the origin.
- $\phi=\text{const}$ ($0<\phi<\pi/2$): cone opening from the positive $z$-axis with opening angle $\phi$ (not “angle with the $x$-axis”).
- $\theta=\text{const}$: half-plane hinged on the $z$-axis.

## Conditions / Assumptions

- $\sin\phi\ge 0$ on $[0,\pi]$, so the Jacobian factor $\rho^2\sin\phi$ is nonnegative.
- Physics texts sometimes swap the names of $\theta$ and $\phi$; keep the conversion formulas consistent with your convention.

## Worked Example

Point $(\rho,\theta,\phi)=(3,\pi/4,\pi/3)$:

$$
x=3\sin(\pi/3)\cos(\pi/4)=\frac{3\sqrt{6}}{4},\quad
y=\frac{3\sqrt{6}}{4},\quad
z=3\cos(\pi/3)=\frac{3}{2}.
$$

Constant $\phi=\pi/3$ is the cone making angle $\pi/3$ with the positive $z$-axis.

## Common Mistakes

- Defining $\phi$ as the angle with the $xy$-plane (that would be $\pi/2-\phi$ in this convention).
- Forgetting $\sin\phi$ in $dV$.
- Allowing $\phi>\pi$ or negative $\rho$ without a careful identification scheme.

## Connections

- Triple integrals: [[Triple Integrals]]
- Related systems: [[Cylindrical Coordinates]]

## References

Spherical coordinates and the Jacobian are standard in OpenStax Calculus Volume 3.[^openstax-sph]

[^openstax-sph]: OpenStax, *Calculus Volume 3*, Section 5.5, https://openstax.org/details/books/calculus-volume-3
