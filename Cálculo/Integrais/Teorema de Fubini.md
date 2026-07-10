---
dg-publish: true
tags:
  - calculus
  - integrals
  - multivariable
---

# Fubini’s Theorem

## Summary

Fubini’s theorem justifies evaluating a double (or triple) integral as an iterated integral, integrating one variable at a time. On a rectangle, if $f$ is continuous, the order of integration may be swapped freely.

## Prerequisites

[[Integrais]], [[Soma de Riemann]], [[Integrais Duplas]]

## Theorem

### Continuous functions on a rectangle

Let $f$ be continuous on $R=[a,b]\times[c,d]$. Then $f$ is integrable on $R$ and

$$
\iint_R f(x,y)\,dA=\int_a^b\int_c^d f(x,y)\,dy\,dx=\int_c^d\int_a^b f(x,y)\,dx\,dy.
$$

### Type I and Type II regions

For a Type I region $D=\{(x,y):a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$ with $f$ continuous on $D$,

$$
\iint_D f\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx.
$$

For a Type II region $D=\{(x,y):c\le y\le d,\ h_1(y)\le x\le h_2(y)\}$,

$$
\iint_D f\,dA=\int_c^d\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy.
$$

When both descriptions apply, either order is valid; choose the easier limits.

## Conditions / Assumptions

- Continuity on a compact region is the elementary sufficient condition.
- If $f$ is only integrable (or improper), more care is needed; absolute integrability allows reordering in advanced settings.

## Worked Example

On $[0,1]\times[0,1]$,

$$
\int_0^1\int_0^1 (x+2y)\,dy\,dx=\int_0^1\bigl[xy+y^2\bigr]_0^1 dx=\int_0^1(x+1)\,dx=\frac{3}{2},
$$

and the reverse order yields the same value.

## Common Mistakes

- Changing order without redrawing the region and updating limits.
- Applying Fubini to a non-integrable singularity without checking absolute convergence.

## Connections

- [[Integrais Duplas]], [[Integrais Duplas Sobre Regiões Gerais]], [[Integrais Triplas]]

## References

Fubini’s theorem and iterated integrals appear in OpenStax Calculus Volume 3.[^openstax-fubini]

[^openstax-fubini]: OpenStax, *Calculus Volume 3*, Section 5.1–5.2, https://openstax.org/details/books/calculus-volume-3
