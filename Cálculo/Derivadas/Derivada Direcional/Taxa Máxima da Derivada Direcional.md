---
dg-publish: true
tags:
  - calculus
  - derivatives
  - multivariable
---

# Maximum Directional Derivative

## Summary

Among all unit directions, the directional derivative is maximized in the direction of the gradient. That maximum value equals the gradient’s magnitude $\|\nabla f\|$. The steepest descent direction is $-\nabla f/\|\nabla f\|$.

## Prerequisites

[[Derivada Direcional]]

## Theorem

If $f$ is differentiable at $\mathbf{a}$ and $\nabla f(\mathbf{a})\neq\mathbf{0}$, then for unit vectors $\mathbf{u}$,

$$
D_{\mathbf{u}}f(\mathbf{a})=\|\nabla f(\mathbf{a})\|\,\cos\theta,
$$

where $\theta$ is the angle between $\nabla f(\mathbf{a})$ and $\mathbf{u}$. Therefore

$$
\max_{\|\mathbf{u}\|=1}D_{\mathbf{u}}f(\mathbf{a})=\|\nabla f(\mathbf{a})\|,
$$

attained at $\mathbf{u}=\nabla f(\mathbf{a})/\|\nabla f(\mathbf{a})\|$, and

$$
\min_{\|\mathbf{u}\|=1}D_{\mathbf{u}}f(\mathbf{a})=-\|\nabla f(\mathbf{a})\|.
$$

## Notation Caution

Do **not** write $|D_{\mathbf{u}}f(\mathbf{a})|$ for the maximum rate. The absolute value $|D_{\mathbf{u}}f|$ is the magnitude of the rate in a **fixed** direction $\mathbf{u}$; the maximum over directions is $\|\nabla f\|$.

## Conditions / Assumptions

- Differentiability at the point (so $D_{\mathbf{u}}f=\nabla f\cdot\mathbf{u}$).
- If $\nabla f(\mathbf{a})=\mathbf{0}$, every directional derivative is zero (critical point).

## Worked Example

For $f(x,y)=x^2+y^2$ at $(1,1)$, $\nabla f(1,1)=(2,2)$ and

$$
\|\nabla f(1,1)\|=\sqrt{8}=2\sqrt{2}.
$$

The maximum directional derivative is $2\sqrt{2}$ in the direction $(1/\sqrt{2},1/\sqrt{2})$.

## Common Mistakes

- Using $|D_{\mathbf{u}}f|$ as if it meant “max over $\mathbf{u}$.”
- Forgetting to normalize the gradient when stating the maximizing direction.

## Connections

- [[Derivada Direcional]], [[Valores de Máximo e Mínimo]], optimization with constraints [[Método dos Multiplicadores de Lagrange]]

## References

The steepest-ascent theorem is standard in multivariable calculus.[^openstax-maxdir]

[^openstax-maxdir]: OpenStax, *Calculus Volume 3*, Section 4.6, https://openstax.org/details/books/calculus-volume-3
