---
dg-publish: true
tags:
  - calculus
  - derivatives
---

# Differentiability of a Function

## Summary

Differentiability means the function admits a good local linear approximation. In one variable this is equivalent to existence of $f'(x_0)$. In several variables, existence of partial derivatives is weaker than differentiability.

## Prerequisites

[[Derivadas]], [[Derivadas Parciais]], [[Limites]]

## Definition

### One variable

$f$ is differentiable at $x_0$ if there exists $L$ such that

$$
\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)-Lh}{h}=0.
$$

Then $L=f'(x_0)$.

### Two variables

$f$ is differentiable at $(x_0,y_0)$ if there exist $A,B$ such that

$$
f(x,y)=f(x_0,y_0)+A(x-x_0)+B(y-y_0)+r(x,y),
$$

with

$$
\lim_{(x,y)\to(x_0,y_0)}\frac{r(x,y)}{\sqrt{(x-x_0)^2+(y-y_0)^2}}=0.
$$

Necessarily $A=f_x(x_0,y_0)$ and $B=f_y(x_0,y_0)$ when the partials exist.

## Conditions / Assumptions

- Differentiability $\implies$ continuity.
- Continuity of partial derivatives on a neighborhood is a **sufficient** condition for differentiability at the point (not necessary).
- Existence of partials alone is **not** sufficient in several variables.

## Worked Example

$f(x)=|x|$ is continuous everywhere but not differentiable at $0$.

$f(x,y)=x^2+y^2$ has continuous partials $f_x=2x$, $f_y=2y$, hence is differentiable on $\mathbb{R}^2$. The linear approximation at $(x_0,y_0)$ is

$$
f(x_0,y_0)+2x_0(x-x_0)+2y_0(y-y_0).
$$

## Common Mistakes

- Equating “partials exist” with “differentiable” in $\mathbb{R}^2$.
- Forgetting that differentiability yields the tangent-plane approximation with little-$o$ error in the distance.

## Connections

- [[Plano Tangente]], [[Diferencial de Uma Função]], [[Derivada Direcional]]

## References

Differentiability criteria appear in OpenStax Calculus Volume 3.[^openstax-diff]

[^openstax-diff]: OpenStax, *Calculus Volume 3*, Section 4.4, https://openstax.org/details/books/calculus-volume-3
