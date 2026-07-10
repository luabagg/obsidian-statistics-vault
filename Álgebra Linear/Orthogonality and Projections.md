---
dg-publish: true
tags:
  - linear-algebra
  - orthogonality
  - projections
aliases:
  - Orthogonal
  - Orthonormal
  - Orthogonal Projection
---

# Orthogonality and Projections

## Summary

Orthogonality means a zero inner product. Orthonormal bases make coordinates and projections simple. Orthogonal projections solve nearest-point problems and are the geometric engine of least squares.

## Prerequisites

[[Vector Spaces and Bases]], [[Vectors and Dot Product]]. Hub: [[Álgebra Linear]].

## Definition / Statement

Vectors $\mathbf{u},\mathbf{v}$ in $\mathbb{R}^n$ are **orthogonal** if $\mathbf{u}\cdot\mathbf{v}=0$. A set is orthogonal if every pair of distinct vectors is orthogonal; it is **orthonormal** if it is orthogonal and each vector has length $1$.

A subspace $W\subseteq\mathbb{R}^n$ has **orthogonal complement**

$$
W^\perp = \{\mathbf{x}\in\mathbb{R}^n : \mathbf{x}\cdot\mathbf{w}=0\text{ for all }\mathbf{w}\in W\}.
$$

The **orthogonal projection** of $\mathbf{b}$ onto $W$ is the unique $\hat{\mathbf{b}}\in W$ such that $\mathbf{b}-\hat{\mathbf{b}}\in W^\perp$.

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $W$ | subspace | $k=\dim W$ |
| $Q$ | matrix with orthonormal columns | $n\times k$ |
| $P$ | projection matrix onto a subspace | $n\times n$ |
| $\hat{\mathbf{b}}$ | projection of $\mathbf{b}$ onto $W$ | $n\times 1$ |

## Notation

| Symbol | Meaning |
|---|---|
| $\mathbf{u}\perp\mathbf{v}$ | $\mathbf{u}\cdot\mathbf{v}=0$ |
| $\operatorname{proj}_W\mathbf{b}$ | orthogonal projection of $\mathbf{b}$ onto $W$ |
| $Q^T Q=I$ | orthonormal columns of $Q$ |

## Conditions / Assumptions

- Standard Euclidean inner product on $\mathbb{R}^n$.
- Projection onto $\operatorname{span}\{\mathbf{a}\}$ with $\mathbf{a}\neq\mathbf{0}$ uses the formula below.
- For a matrix $A$ with full column rank, the projection onto $\operatorname{Col}(A)$ uses the normal equations (see [[Least Squares and QR]]).

## Matrix / Vector Form

**Projection onto a line** spanned by $\mathbf{a}\neq\mathbf{0}$:

$$
\operatorname{proj}_{\mathbf{a}}\mathbf{b}
= \frac{\mathbf{a}\cdot\mathbf{b}}{\mathbf{a}\cdot\mathbf{a}}\,\mathbf{a}
= \frac{\mathbf{a}^T\mathbf{b}}{\mathbf{a}^T\mathbf{a}}\,\mathbf{a}.
$$

**Projection onto $\operatorname{Col}(A)$** when $A$ has linearly independent columns:

$$
\hat{\mathbf{b}} = A\hat{\mathbf{x}}, \qquad
A^T A\hat{\mathbf{x}} = A^T\mathbf{b},
$$
$$
\hat{\mathbf{b}} = A(A^T A)^{-1}A^T\mathbf{b}.
$$

The matrix $P=A(A^T A)^{-1}A^T$ is the orthogonal projection matrix onto $\operatorname{Col}(A)$: $P^T=P$ and $P^2=P$.

**Orthonormal columns** $Q$: projection simplifies to

$$
\hat{\mathbf{b}} = QQ^T\mathbf{b}.
$$

**Pythagorean theorem**: if $\mathbf{u}\perp\mathbf{v}$, then $\|\mathbf{u}+\mathbf{v}\|^2=\|\mathbf{u}\|^2+\|\mathbf{v}\|^2$.

## Geometric Interpretation

- $\hat{\mathbf{b}}$ is the closest point in $W$ to $\mathbf{b}$.
- Residual $\mathbf{b}-\hat{\mathbf{b}}$ is perpendicular to every vector in $W$.
- Orthonormal frames measure lengths of coordinates by the ordinary Euclidean norm of the coefficient vector.

## Worked Example

Project $\mathbf{b}=\langle 3,4\rangle$ onto $\mathbf{a}=\langle 1,0\rangle$:

$$
\operatorname{proj}_{\mathbf{a}}\mathbf{b} = \frac{3}{1}\langle 1,0\rangle = \langle 3,0\rangle,
\quad
\mathbf{b}-\hat{\mathbf{b}} = \langle 0,4\rangle \perp \mathbf{a}.
$$

## Common Mistakes

- Using $\mathbf{a}^T\mathbf{b}/\|\mathbf{a}\|$ instead of $\mathbf{a}^T\mathbf{b}/\|\mathbf{a}\|^2$ (or $\mathbf{a}^T\mathbf{a}$).
- Forgetting that $QQ^T$ is the projection only when columns of $Q$ are orthonormal (for orthogonal but not unit columns, scale correctly).
- Confusing $Q^T Q=I_k$ (always for orthonormal columns) with $QQ^T=I_n$ (only if $k=n$).

## Connections

- Related: [[Vectors and Dot Product]], [[Vector Spaces and Bases]], [[Least Squares and QR]]
- Next: [[Least Squares and QR]]
- Spectral: real symmetric matrices have orthonormal eigenbases ([[Eigenvalues and Eigenvectors]])

## References

Orthogonality and projections follow MIT 18.06.[^mit-ortho]

[^mit-ortho]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
