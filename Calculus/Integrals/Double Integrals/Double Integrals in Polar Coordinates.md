---
dg-publish: true
tags:
  - calculus
  - integrals
  - multivariable
  - coordinates
---

# Double Integrals in Polar Coordinates

## Summary

When a region or integrand is circularly symmetric, switch to polar coordinates with $x=r\cos\theta$, $y=r\sin\theta$, and **area element** $dA=r\,dr\,d\theta$. The extra factor $r$ is the absolute value of the Jacobian.

## Prerequisites

[[Double Integrals]], [[Polar Coordinates]]

## Formula

$$
\iint_R f(x,y)\,dA=\iint_{R'} f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta.
$$

## Conditions / Assumptions

- $f$ continuous on the compact region; $r\ge 0$.
- Describe $R'$ with constant or simple bounds in $(r,\theta)$ when possible (polar rectangles, sectors, annuli).

## Worked Example

### Disk area

Area of $x^2+y^2\le R^2$:

$$
A=\int_0^{2\pi}\int_0^R r\,dr\,d\theta=\int_0^{2\pi}\frac{R^2}{2}\,d\theta=\pi R^2.
$$

(Not $2\pi R^2$.)

### Integrand $x^2+y^2$ on the disk

$$
\iint_{x^2+y^2\le R^2}(x^2+y^2)\,dA=\int_0^{2\pi}\int_0^R r^2\cdot r\,dr\,d\theta=\int_0^{2\pi}\frac{R^4}{4}\,d\theta=\frac{\pi R^4}{2}.
$$

## Common Mistakes

- Forgetting the Jacobian factor $r$.
- Computing disk area as $2\pi R^2$ by integrating $r$ incorrectly or double-counting.
- Using Cartesian limits after substituting polar expressions.

## Connections

- [[Polar Coordinates]], [[Double Integrals over General Regions]], cylindrical/spherical analogs in 3D

## References

Polar double integrals are in OpenStax Calculus Volume 3.[^openstax-polardbl]

[^openstax-polardbl]: OpenStax, *Calculus Volume 3*, Section 5.3, https://openstax.org/details/books/calculus-volume-3
