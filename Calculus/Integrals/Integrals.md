---
dg-publish: true
dg-show-local-graph: true
tags:
  - calculus
  - integrals
---

%% Begin Waypoint %%
- **[[Integrals]]**
	- **[[Double Integrals]]**
	- [[Fubini's Theorem]]
	- [[Integration by Parts]]
	- [[Riemann Sum]]
	- **[[Triple Integrals]]**

%% End Waypoint %%

# Integrals

## Summary

Integrals measure accumulation: areas under curves, net change, and higher-dimensional mass/volume. Indefinite integrals denote families of antiderivatives; definite integrals are limits of Riemann sums and are evaluated with the Fundamental Theorem when an antiderivative is known.

## Prerequisites

[[Limits]], [[Derivatives]], [[Fundamental Theorem of Calculus]]

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

Integration by parts: $\int u\,dv=uv-\int v\,du$ (see [[Integration by Parts]]).

## Common Mistakes

- Dropping $+C$ for indefinite integrals.
- Applying FTC without an antiderivative valid on the whole interval.

## Connections

- Building blocks: [[Riemann Sum]], [[Fundamental Theorem of Calculus]]
- Techniques: [[Integration by Parts]]
- Multivariable: [[Double Integrals]], [[Fubini's Theorem]], [[Triple Integrals]]

## References

Integral calculus is developed in OpenStax Calculus Volumes 1–2.[^openstax-int]

[^openstax-int]: OpenStax, *Calculus Volume 1*, Chapters 4–5; *Volume 2*, Chapter 1, https://openstax.org/details/books/calculus-volume-1
