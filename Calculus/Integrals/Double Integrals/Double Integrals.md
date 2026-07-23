---
dg-publish: true
dg-show-local-graph: true
tags:
  - calculus
  - integrals
  - double-integrals
---

%% Begin Waypoint %%
- **[[Double Integrals]]**
	- [[Double Integrals in Polar Coordinates]]
	- [[Double Integrals over General Regions]]
%% End Waypoint %%

# Double Integrals

## Summary

A double integral $\iint_R f(x,y)\,dA$ accumulates the values of $f$ over a region $R$ in the plane. For $f\ge 0$ it represents volume under the surface $z=f(x,y)$. On rectangles it is the limit of double Riemann sums and equals an iterated integral.

## Prerequisites

[[Integrals]], [[Riemann Sum]], [[Fubini's Theorem]]

## Definition

For $f$ defined on a rectangle $R=[a,b]\times[c,d]$, partition into subrectangles of area $\Delta A_{ij}$, pick sample points $(x_{ij}^*,y_{ij}^*)$, and form

$$
\sum_i\sum_j f(x_{ij}^*,y_{ij}^*)\Delta A_{ij}.
$$

If the mesh tends to zero and the sums approach a common limit independent of choices, that limit is $\iint_R f\,dA$.

For continuous $f$ on $R$,

$$
\iint_R f(x,y)\,dA=\int_a^b\int_c^d f(x,y)\,dy\,dx.
$$

## Conditions / Assumptions

- Continuity on a closed bounded rectangle is sufficient.
- For nonrectangular regions, extend $f$ by zero or describe $R$ as Type I/II; see [[Double Integrals over General Regions]].

## Worked Example

$$
\iint_{[0,1]\times[0,2]} (2x+y)\,dA=\int_0^1\int_0^2(2x+y)\,dy\,dx=\int_0^1\bigl[2xy+\tfrac{1}{2}y^2\bigr]_0^2 dx=\int_0^1(4x+2)\,dx=4.
$$

## Common Mistakes

- Forgetting which variable the inner integral treats as constant.
- Omitting $dA$ interpretation when switching to polar form (need factor $r$).

## Connections

- [[Fubini's Theorem]], [[Double Integrals over General Regions]], [[Double Integrals in Polar Coordinates]], [[Triple Integrals]]

## References

Double integrals are introduced in OpenStax Calculus Volume 3.[^openstax-double]

[^openstax-double]: OpenStax, *Calculus Volume 3*, Section 5.1, https://openstax.org/details/books/calculus-volume-3
