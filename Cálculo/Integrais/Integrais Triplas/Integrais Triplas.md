---
dg-publish: true
tags:
  - calculus
  - integrals
  - multivariable
---

%% Begin Waypoint %%

- [[Integrais Triplas]]

%% End Waypoint %%

# Triple Integrals

## Summary

A triple integral $\iiint_E f(x,y,z)\,dV$ accumulates a scalar over a solid region $E$. With $f=1$ it measures volume; with density $\rho$ it measures mass. Evaluate as iterated integrals in Cartesian, cylindrical, or spherical coordinates.

## Prerequisites

[[Integrais Duplas]], [[Teorema de Fubini]], [[Coordenadas Cilíndricas]], [[Coordenadas Esféricas]]

## Formula

Cartesian:

$$
\iiint_E f\,dV=\int\!\!\int\!\!\int f(x,y,z)\,dx\,dy\,dz
$$

with limits describing $E$.

Cylindrical: $dV=r\,dr\,d\theta\,dz$.

Spherical: $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ (OpenStax $\phi$-from-$z$ convention).

## Conditions / Assumptions

- Continuity of $f$ on a closed bounded solid is a sufficient elementary hypothesis.
- Match the coordinate system to the symmetry of $E$ or $f$.

## Worked Example

Over the unit cube $0\le x,y,z\le 1$,

$$
\iiint_E (x+y+z)\,dV=\int_0^1\int_0^1\int_0^1(x+y+z)\,dx\,dy\,dz=\frac{3}{2}.
$$

Volume of the unit ball in spherical coordinates:

$$
\int_0^{2\pi}\int_0^\pi\int_0^1 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta=\frac{4\pi}{3}.
$$

## Common Mistakes

- Omitting $r$ or $\rho^2\sin\phi$ in non-Cartesian coordinates.
- Swapping the meanings of spherical $\theta$ and $\phi$ relative to the conversion formulas in use.

## Connections

- [[Integrais Duplas]], [[Coordenadas Cilíndricas]], [[Coordenadas Esféricas]]

## References

Triple integrals and coordinate changes are in OpenStax Calculus Volume 3.[^openstax-triple]

[^openstax-triple]: OpenStax, *Calculus Volume 3*, Sections 5.4–5.5, https://openstax.org/details/books/calculus-volume-3
