---
dg-publish: true
tags:
  - calculus
  - derivatives
  - multivariable
---

# Partial Derivatives

## Summary

A partial derivative measures how a multivariable function changes when one variable varies and the others are held fixed. Geometrically, it is the slope of the curve obtained by slicing the graph with a plane of constant remaining variables.

## Prerequisites

[[Derivadas]], [[Funções de Mais de uma Variável]]

## Definition

For $f(x,y)$,

$$
f_x(x,y)=\frac{\partial f}{\partial x}=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h},
$$

when the limit exists, and similarly for $f_y$.

## Conditions / Assumptions

- When computing $\partial f/\partial x$, treat every other independent variable as constant.
- Existence of partials at a point does not imply continuity or differentiability of $f$ there.

## Worked Example

If $f(x,y)=x^2+3xy-4y^2$, then

$$
\frac{\partial f}{\partial x}=2x+3y,\qquad\frac{\partial f}{\partial y}=3x-8y.
$$

If $f(x,y)=x^2 y+4y^3$, then $f_x=2xy$ and $f_y=x^2+12y^2$.

The gradient packages the first partials:

$$
\nabla f=(f_x,f_y).
$$

## Common Mistakes

- Differentiating with respect to $x$ while still treating $y$ as a function of $x$ unless the context is a total derivative (chain rule).
- Confusing $\partial f/\partial x$ with the directional derivative in a non-axis direction.

## Connections

- [[Regras da Cadeia]], [[Derivada Direcional]], [[Diferenciabilidade de uma  Função]], [[Teorema de Clairaut]]

## References

Partial derivatives are introduced in OpenStax Calculus Volume 3.[^openstax-partial]

[^openstax-partial]: OpenStax, *Calculus Volume 3*, Section 4.3, https://openstax.org/details/books/calculus-volume-3
