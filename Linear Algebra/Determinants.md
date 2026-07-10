---
dg-publish: true
tags:
  - linear-algebra
  - determinants
aliases:
  - Determinant
  - det
---

# Determinants

## Summary

The determinant is a scalar associated to a square matrix. It measures signed volume scaling of the linear map, vanishes exactly when the matrix is singular, and appears in the eigenvalue equation $\det(A-\lambda I)=0$.

## Prerequisites

[[Matrices and Row Reduction]]. Hub: [[Linear Algebra]].

## Definition / Statement

For a square matrix $A\in\mathbb{R}^{n\times n}$, the **determinant** $\det(A)$ (also written $|A|$) is the unique alternating multilinear function of the columns with $\det(I)=1$. Computationally it is defined recursively by cofactor expansion, or via row reduction.

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $A$ | square matrix | $n\times n$ |
| $\det(A)$ | determinant | scalar |
| $\operatorname{adj}(A)$ | adjugate (transpose of cofactor matrix) | $n\times n$ |

## Notation

| Symbol | Meaning |
|---|---|
| $\det(A)$, $|A|$ | determinant of $A$ |
| $C_{ij}$ | $(i,j)$-cofactor |
| $A_{ij}$ | minor deleting row $i$, column $j$ |

## Conditions / Assumptions

- $A$ must be square for $\det(A)$ to be defined in this sense.
- $\det(A)\neq 0$ if and only if $A$ is invertible.
- Over $\mathbb{R}$, $\lvert\det(A)\rvert$ is the volume scaling factor of the unit cube under $A$.

## Matrix / Vector Form

**$2\times 2$**

$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc.
$$

**$3\times 3$** (cofactor expansion along the first row)

$$
\det\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
=
a_{11}(a_{22}a_{33}-a_{23}a_{32})
- a_{12}(a_{21}a_{33}-a_{23}a_{31})
+ a_{13}(a_{21}a_{32}-a_{22}a_{31}).
$$

**Product and transpose**

$$
\det(AB)=\det(A)\det(B), \qquad \det(A^T)=\det(A).
$$

**Inverse** (when $\det(A)\neq 0$)

$$
A^{-1} = \frac{1}{\det(A)}\operatorname{adj}(A).
$$

**Row-reduction rules** (sign and scale carefully):

- Swapping two rows multiplies $\det$ by $-1$.
- Multiplying a row by $c$ multiplies $\det$ by $c$.
- Adding a multiple of one row to another leaves $\det$ unchanged.
- Determinant of a triangular matrix is the product of diagonal entries.

## Geometric Interpretation

- $\det(A)=0$: columns lie in a lower-dimensional flat; volume collapses.
- $\det(A)>0$: orientation-preserving map; $\det(A)<0$: orientation-reversing.

## Worked Example

$$
\det\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 1\cdot 4 - 2\cdot 3 = -2 \neq 0,
$$

so the matrix is invertible. For

$$
B=\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix},
\quad \det(B)=1\cdot 4\cdot 6=24.
$$

## Common Mistakes

- Using $ad+bc$ instead of $ad-bc$ for $2\times 2$.
- Applying the $2\times 2$ pattern naively to $3\times 3$ without cofactors (the “diagonal trick” needs care with signs).
- Concluding $\det(A+B)=\det(A)+\det(B)$ (false in general).
- Computing determinants of non-square matrices.

## Connections

- Related: [[Matrices and Row Reduction]], [[Eigenvalues and Eigenvectors]], [[Systems of Linear Equations]]
- Next: [[Eigenvalues and Eigenvectors]]
- Volume links: bases and parallelepipeds in [[Vector Spaces and Bases]]

## References

Determinant properties and computations follow MIT 18.06.[^mit-det]

[^mit-det]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
