---
dg-publish: true
tags:
  - calculus
  - multivariable
  - optimization
---

# Maxima and Minima of Functions of Two Variables

## Summary

Local extrema of $f(x,y)$ occur at critical points where $\nabla f=\mathbf{0}$ (or where $f$ is not differentiable). The second-derivative (Hessian) test classifies many critical points. On a closed bounded region, also check the boundary.

## Prerequisites

[[Derivadas Parciais]], [[Derivadas de Ordem Superior]], [[Teorema de Clairaut]]

## Procedure

1. Solve $f_x=0$, $f_y=0$ for critical points in the open domain.
2. At each critical point where second partials exist, compute

$$
D=f_{xx}f_{yy}-(f_{xy})^2.
$$

3. Classify:
   - $D>0$ and $f_{xx}>0$: local minimum.
   - $D>0$ and $f_{xx}<0$: local maximum.
   - $D<0$: saddle point.
   - $D=0$: test inconclusive.
4. For absolute extrema on a closed bounded region $R$, also optimize $f$ on $\partial R$ (one-variable calculus or Lagrange constraints).

## Conditions / Assumptions

- Second partials continuous near the critical point for the standard Hessian test.
- Clairaut’s theorem ensures $f_{xy}=f_{yx}$ under continuity of mixed partials, so $D$ is well-defined from either order.

## Worked Example

Let $f(x,y)=x^2+y^2-2x-4y+1$.

Critical point: $f_x=2x-2=0$, $f_y=2y-4=0$ $\Rightarrow$ $(1,2)$.

Second partials: $f_{xx}=2$, $f_{yy}=2$, $f_{xy}=0$, so $D=4>0$ and $f_{xx}>0$: local minimum. Value $f(1,2)=-4$.

## Common Mistakes

- Stopping after finding critical points without the Hessian test or boundary analysis.
- Using $D=f_{xx}+f_{yy}$ (trace) instead of the Hessian determinant.
- Claiming a local extremum is global without further argument.

## Connections

- Constrained extrema: [[Método dos Multiplicadores de Lagrange]]
- Second partials: [[Derivadas de Ordem Superior]]

## References

The second-derivative test for functions of two variables is in OpenStax Calculus Volume 3.[^openstax-extrema]

[^openstax-extrema]: OpenStax, *Calculus Volume 3*, Section 4.7, https://openstax.org/details/books/calculus-volume-3
