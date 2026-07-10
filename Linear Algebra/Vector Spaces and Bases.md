---
dg-publish: true
tags:
  - linear-algebra
  - vector-spaces
  - bases
aliases:
  - Vector Space
  - Basis
  - Dimension
  - Linear Independence
---

# Vector Spaces and Bases

## Summary

A vector space is a set closed under addition and scalar multiplication with the usual algebraic axioms. Bases give coordinate systems: every vector has unique coordinates, and dimension is the number of basis vectors.

## Prerequisites

[[Matrices and Row Reduction]], [[Systems of Linear Equations]]. Hub: [[Linear Algebra]].

## Definition / Statement

A **vector space** $V$ over $\mathbb{R}$ is a set with addition and scalar multiplication satisfying the standard axioms (associativity, commutativity of addition, zero vector, additive inverses, distributive laws, $1\cdot\mathbf{v}=\mathbf{v}$).

Common examples: $\mathbb{R}^n$, matrix spaces $\mathbb{R}^{m\times n}$, polynomial spaces, solution spaces of homogeneous linear systems (null spaces).

A set $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ is **linearly independent** if

$$
c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1=\cdots=c_k=0.
$$

Otherwise it is **linearly dependent**.

The **span** of $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ is the set of all linear combinations of those vectors.

A **basis** of $V$ is a linearly independent spanning set. All bases of a finite-dimensional space have the same number of vectors; that number is $\dim V$.

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $V$ | vector space | $\dim V = n$ if finite-dimensional |
| $\operatorname{Col}(A)$ | column space of $A$ | $\operatorname{rank}(A)$ |
| $\operatorname{Nul}(A)$ | null space of $A$ | $n - \operatorname{rank}(A)$ for $A\in\mathbb{R}^{m\times n}$ |
| $\operatorname{Row}(A)$ | row space of $A$ | $\operatorname{rank}(A)$ |

## Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{span}\{\mathbf{v}_i\}$ | all linear combinations of the $\mathbf{v}_i$ |
| $\dim V$ | dimension of $V$ |
| $[\mathbf{x}]_{\mathcal{B}}$ | coordinates of $\mathbf{x}$ in basis $\mathcal{B}$ |

## Conditions / Assumptions

- Real scalars unless complex spaces are specified.
- Finite-dimensional discussion unless stated otherwise.
- Rank–nullity for $A\in\mathbb{R}^{m\times n}$:
  $$
  \dim\operatorname{Nul}(A) + \operatorname{rank}(A) = n.
  $$

## Matrix / Vector Form

If $\mathcal{B}=\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ is a basis of $\mathbb{R}^n$ and $B$ is the matrix with those columns, then

$$
\mathbf{x} = B[\mathbf{x}]_{\mathcal{B}} \implies [\mathbf{x}]_{\mathcal{B}} = B^{-1}\mathbf{x}.
$$

Pivot columns of $A$ form a basis for $\operatorname{Col}(A)$. Free-variable special solutions form a basis for $\operatorname{Nul}(A)$.

## Geometric Interpretation

- Independent vectors point in “essentially different” directions (no one is a combination of the others).
- A basis is a coordinate frame for the whole space.
- Null space: directions mapped to $\mathbf{0}$ by $A$; column space: reachable right-hand sides $\mathbf{b}$.

## Worked Example

In $\mathbb{R}^3$, let $\mathbf{v}_1=\langle 1,0,0\rangle$, $\mathbf{v}_2=\langle 1,1,0\rangle$, $\mathbf{v}_3=\langle 1,1,1\rangle$.

The matrix with these columns is upper triangular with nonzero diagonals after mild reduction, so they are independent and form a basis of $\mathbb{R}^3$. Coordinates of $\mathbf{e}_3=\langle 0,0,1\rangle$:

$$
c_1\mathbf{v}_1+c_2\mathbf{v}_2+c_3\mathbf{v}_3=\mathbf{e}_3 \implies c_3=1,\; c_2=-1,\; c_1=0,
$$

so $[\mathbf{e}_3]_{\mathcal{B}} = \langle 0,-1,1\rangle$.

## Common Mistakes

- Thinking any set of $n$ vectors in $\mathbb{R}^n$ is a basis (must also be independent).
- Confusing $\operatorname{Col}(A)$ (in $\mathbb{R}^m$) with $\operatorname{Row}(A)$ (in $\mathbb{R}^n$).
- Claiming dependent sets cannot span a space (they can; bases are independent spanning sets).

## Connections

- Related: [[Matrices and Row Reduction]], [[Orthogonality and Projections]], [[Eigenvalues and Eigenvectors]]
- Next: [[Determinants]] or [[Eigenvalues and Eigenvectors]]
- Geometry: directions and planes in [[Lines and Planes]]

## References

Vector spaces, bases, and rank–nullity follow MIT 18.06.[^mit-vs]

[^mit-vs]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
