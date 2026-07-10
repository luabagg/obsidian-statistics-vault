---
dg-publish: true
tags:
  - geometry
  - vectors
  - analytic-geometry
aliases:
  - Vectors
  - Dot Product
  - Scalar Product
---

# Vectors and Dot Product

## Summary

Vectors encode magnitude and direction. The dot product measures alignment: it yields lengths, angles, and orthogonal projections, and is the bridge from analytic geometry to linear algebra orthogonality.

## Prerequisites

[[Distance and Midpoint]]. Helpful: [[Trigonometry]]. Hub: [[Analytic Geometry]].

## Object / Concept

A **vector** in $\mathbb{R}^n$ is an ordered $n$-tuple $\mathbf{v} = \langle v_1,\ldots,v_n\rangle$ (equivalently a column). Vectors add componentwise and scale by real numbers.

The **dot product** (standard inner product) of $\mathbf{u}=\langle u_1,\ldots,u_n\rangle$ and $\mathbf{v}=\langle v_1,\ldots,v_n\rangle$ is

$$
\mathbf{u}\cdot\mathbf{v} = u_1 v_1 + \cdots + u_n v_n.
$$

## Notation

| Symbol | Meaning |
|---|---|
| $\mathbf{u},\mathbf{v},\mathbf{w}$ | vectors |
| $\|\mathbf{v}\|$ | Euclidean norm (length) of $\mathbf{v}$ |
| $\mathbf{u}\cdot\mathbf{v}$ | dot product |
| $\operatorname{proj}_{\mathbf{v}}\mathbf{u}$ | orthogonal projection of $\mathbf{u}$ onto $\mathbf{v}$ |
| $\mathbf{0}$ | zero vector |

## Conditions / Assumptions

- Real Euclidean space $\mathbb{R}^n$ with the standard dot product.
- Projection formula requires $\mathbf{v} \neq \mathbf{0}$.
- Angle formula requires $\mathbf{u},\mathbf{v} \neq \mathbf{0}$.

## Equations

**Length**

$$
\|\mathbf{v}\| = \sqrt{\mathbf{v}\cdot\mathbf{v}} = \sqrt{v_1^2 + \cdots + v_n^2}.
$$

**Angle $\theta$ between nonzero vectors**

$$
\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta, \qquad
\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}.
$$

**Orthogonality**: $\mathbf{u}\perp\mathbf{v}$ if and only if $\mathbf{u}\cdot\mathbf{v} = 0$.

**Unit vector** in the direction of $\mathbf{v}\neq\mathbf{0}$:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}.
$$

**Orthogonal projection** of $\mathbf{u}$ onto $\mathbf{v}\neq\mathbf{0}$:

$$
\operatorname{proj}_{\mathbf{v}}\mathbf{u}
= \Biggl(\frac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}\Biggr)\mathbf{v}
= \Biggl(\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\Biggr)\mathbf{v}.
$$

The residual $\mathbf{u} - \operatorname{proj}_{\mathbf{v}}\mathbf{u}$ is orthogonal to $\mathbf{v}$.

**Algebraic properties**

$$
\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u},\quad
\mathbf{u}\cdot(\mathbf{v}+\mathbf{w})=\mathbf{u}\cdot\mathbf{v}+\mathbf{u}\cdot\mathbf{w},\quad
(c\mathbf{u})\cdot\mathbf{v}=c(\mathbf{u}\cdot\mathbf{v}).
$$

## Geometric Interpretation

- $\mathbf{u}\cdot\mathbf{v} > 0$: acute angle; $=0$: right angle; $<0$: obtuse angle.
- $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\mathbf{u}\cdot\mathbf{v}$ (law of cosines in vector form).
- Projection extracts the component of $\mathbf{u}$ parallel to $\mathbf{v}$.

## Worked Example

Let $\mathbf{u}=\langle 3,4\rangle$ and $\mathbf{v}=\langle 1,0\rangle$.

$$
\mathbf{u}\cdot\mathbf{v} = 3, \quad \|\mathbf{u}\|=5, \quad \|\mathbf{v}\|=1,
$$
$$
\cos\theta = \frac{3}{5}, \quad
\operatorname{proj}_{\mathbf{v}}\mathbf{u} = \frac{3}{1}\langle 1,0\rangle = \langle 3,0\rangle.
$$

## Common Mistakes

- Dividing by $\|\mathbf{v}\|$ instead of $\|\mathbf{v}\|^2$ in the projection formula.
- Claiming $\mathbf{u}\cdot\mathbf{v}=\|\mathbf{u}\|\,\|\mathbf{v}\|$ without $\cos\theta$ (only if $\theta=0$).
- Treating the zero vector as having a well-defined direction or unit vector.

## Connections

- Related: [[Lines and Planes]], [[Distance and Midpoint]]
- Next: [[Conic Sections]]; [[Orthogonality and Projections]] in linear algebra
- Later: least squares via projections — [[Least Squares and QR]]

## References

Vector algebra and the dot product follow OpenStax Calculus Volume 3.[^openstax-dot]

[^openstax-dot]: OpenStax, *Calculus Volume 3*, https://openstax.org/details/books/calculus-volume-3
