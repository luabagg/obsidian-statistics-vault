---
dg-publish: true
tags:
  - calculus
  - derivatives
  - integrals
  - limits
---

# Fundamental Theorem of Calculus

## Summary

The Fundamental Theorem of Calculus (FTC) links differentiation and integration. Part 1 says that the integral-from-a-fixed-lower-limit defines an antiderivative. Part 2 evaluates definite integrals using any antiderivative.

## Prerequisites

[[Limites]], [[Derivadas]], [[Integrais]], [[Soma de Riemann]]

## Definition / Theorem

Let $f$ be continuous on the closed interval $[a,b]$.

### Part 1

Define

$$
F(x)=\int_a^x f(t)\,dt,\qquad x\in[a,b].
$$

Then $F$ is differentiable on $(a,b)$ and $F'(x)=f(x)$. (At the endpoints one uses one-sided derivatives.)

### Part 2

If $F$ is any antiderivative of $f$ on $[a,b]$ (so $F'=f$), then

$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

## Conditions / Assumptions

- Continuity of $f$ on $[a,b]$ is a standard sufficient hypothesis for both parts as stated in elementary calculus.
- Part 2 still holds under weaker integrability conditions if $F'=f$ almost everywhere and $F$ is absolutely continuous, but that is beyond this note.
- The lower limit in Part 1 may be any fixed point in the interval; changing it only shifts $F$ by a constant.

## Worked Example

1. If $G(x)=\int_0^x t^2\,dt$, then $G'(x)=x^2$ by Part 1.
2. $\int_1^3(2x+1)\,dx$: an antiderivative is $F(x)=x^2+x$, so

$$
F(3)-F(1)=(9+3)-(1+1)=10.
$$

## Common Mistakes

- Applying Part 2 without an antiderivative that is valid on the whole interval.
- Forgetting the chain rule when the upper limit is a function: $\frac{d}{dx}\int_a^{u(x)}f(t)\,dt=f(u(x))u'(x)$.

## Connections

- Builds on [[Soma de Riemann]] and [[Derivadas]]
- Used constantly in [[Integrais]] and applications

## References

Both parts appear with continuity hypotheses in OpenStax Calculus Volume 1.[^openstax-ftc]

[^openstax-ftc]: OpenStax, *Calculus Volume 1*, Section 5.3, https://openstax.org/details/books/calculus-volume-1
