---
dg-publish: true
dg-show-local-graph: true
tags:
  - calculus
  - integrals
---

%% Begin Waypoint %%
- **[[Integrais]]**
	- **[[Integrais Duplas]]**
	- **[[Integrais Triplas]]**
	- [[Integral por Partes]]
	- [[Soma de Riemann]]
	- [[Teorema de Fubini]]

%% End Waypoint %%

# Integrals

## Summary

Integrals measure accumulation: areas under curves, net change, and higher-dimensional mass/volume. Indefinite integrals denote families of antiderivatives; definite integrals are limits of Riemann sums and are evaluated with the Fundamental Theorem when an antiderivative is known.

## Prerequisites

[[Limites]], [[Derivadas]], [[Teorema Fundamental do Cálculo]]

## Definition

### Indefinite integral

$$
\int f(x)\,dx=F(x)+C,\qquad F'=f.
$$

### Definite integral

$$
\int_a^b f(x)\,dx=\lim_{\|P\|\to 0}\sum f(x_i^*)\Delta x_i
$$

when the limit exists (e.g. $f$ continuous on $[a,b]$).

## Conditions / Assumptions

- Continuity on $[a,b]$ guarantees Riemann integrability.
- Improper integrals need separate limit analysis at singularities or infinite bounds.

## Worked Example

$$
\int 3x^2\,dx=x^3+C,\qquad
\int_0^1 x^2\,dx=\Bigl[\frac{x^3}{3}\Bigr]_0^1=\frac{1}{3}.
$$

Integration by parts: $\int u\,dv=uv-\int v\,du$ (see [[Integral por Partes]]).

## Common Mistakes

- Dropping $+C$ for indefinite integrals.
- Applying FTC without an antiderivative valid on the whole interval.

## Connections

- Building blocks: [[Soma de Riemann]], [[Teorema Fundamental do Cálculo]]
- Techniques: [[Integral por Partes]]
- Multivariable: [[Integrais Duplas]], [[Teorema de Fubini]], [[Integrais Triplas]]

## References

Integral calculus is developed in OpenStax Calculus Volumes 1–2.[^openstax-int]

[^openstax-int]: OpenStax, *Calculus Volume 1*, Chapters 4–5; *Volume 2*, Chapter 1, https://openstax.org/details/books/calculus-volume-1
