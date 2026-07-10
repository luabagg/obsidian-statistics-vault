---
dg-publish: true
tags:
  - calculus
  - derivatives
---

# Differential of a Function

## Summary

The differential is the linear approximation to the change in a function. In one variable, $df=f'(x)\,dx$. In two variables, $df=f_x\,dx+f_y\,dy$.

## Prerequisites

[[Derivadas]], [[Derivadas Parciais]], [[Diferenciabilidade de uma  Função]]

## Formula

### One variable

If $f$ is differentiable,

$$
df=f'(x)\,dx.
$$

The actual increment is $\Delta f=f(x+\Delta x)-f(x)=df+\varepsilon$ with $\varepsilon/\Delta x\to 0$ as $\Delta x\to 0$.

### Two variables

$$
df=\frac{\partial f}{\partial x}\,dx+\frac{\partial f}{\partial y}\,dy.
$$

## Conditions / Assumptions

- Differentiability at the expansion point.
- The increments $dx,dy$ are independent variables in the linear map; in applications they are small changes.

## Worked Example

For $f(x)=x^2+3x-5$, $df=(2x+3)\,dx$. At $x=1$, $dx=0.1$, $df=0.5$.

For $f(x,y)=x^2+3xy-4y^2$,

$$
df=(2x+3y)\,dx+(3x-8y)\,dy.
$$

At $(1,2)$ with $dx=0.1$, $dy=0.2$:

$$
df=8(0.1)+(-13)(0.2)=0.8-2.6=-1.8.
$$

## Common Mistakes

- Treating $df$ as exact $\Delta f$ for large increments.
- Omitting one of the partial terms in several variables.

## Connections

- [[Plano Tangente]], [[Regras da Cadeia]], error estimation in measurements

## References

Differentials and linear approximation are covered in OpenStax Calculus.[^openstax-diffntl]

[^openstax-diffntl]: OpenStax, *Calculus Volume 1*, Section 4.2; *Calculus Volume 3*, Section 4.4, https://openstax.org/details/books/calculus-volume-1
