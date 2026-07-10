---
dg-publish: true
tags:
  - linear-algebra
  - eigenvalues
  - eigenvectors
aliases:
  - Eigenvalues
  - Eigenvectors
  - Spectrum
  - Characteristic Polynomial
---

# Eigenvalues and Eigenvectors

## Summary

An eigenvector of a square matrix is a nonzero vector mapped to a scalar multiple of itself. Eigenvalues are those scalars. The spectral picture diagonalizes (or Jordan-reduces) linear maps and underpins differential equations, PCA, and stability analysis.

## Prerequisites

[[Determinants]], [[Vector Spaces and Bases]], [[Matrices and Row Reduction]]. Hub: [[Linear Algebra]].

## Definition / Statement

Let $A\in\mathbb{R}^{n\times n}$ (or $\mathbb{C}^{n\times n}$). A scalar $\lambda$ is an **eigenvalue** of $A$ if there exists a nonzero vector $\mathbf{v}$ (an **eigenvector**) such that

$$
A\mathbf{v} = \lambda\mathbf{v}.
$$

Equivalently,

$$
(A-\lambda I)\mathbf{v} = \mathbf{0}, \quad \mathbf{v}\neq\mathbf{0},
$$

so $A-\lambda I$ is singular:

$$
\det(A-\lambda I) = 0.
$$

The polynomial $p_A(\lambda)=\det(A-\lambda I)$ is the **characteristic polynomial** (degree $n$).

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $A$ | square matrix | $n\times n$ |
| $\lambda$ | eigenvalue | scalar |
| $\mathbf{v}$ | eigenvector | $n\times 1$, nonzero |
| $E_\lambda=\operatorname{Nul}(A-\lambda I)$ | eigenspace | subspace of $\mathbb{R}^n$ or $\mathbb{C}^n$ |

## Notation

| Symbol | Meaning |
|---|---|
| $A\mathbf{v}=\lambda\mathbf{v}$ | eigen-equation |
| $p_A(\lambda)=\det(A-\lambda I)$ | characteristic polynomial |
| algebraic multiplicity | multiplicity of $\lambda$ as a root of $p_A$ |
| geometric multiplicity | $\dim E_\lambda$ |

## Conditions / Assumptions

- Eigenvectors are nonzero by definition; $\mathbf{0}$ is never called an eigenvector.
- Over $\mathbb{R}$, eigenvalues may be complex (come in conjugate pairs for real $A$).
- $A$ is diagonalizable if and only if there is a basis of $\mathbb{R}^n$ (or $\mathbb{C}^n$) consisting of eigenvectors, equivalently the sum of geometric multiplicities equals $n$ (over an algebraically closed field, algebraic and geometric multiplicities must match for each eigenvalue).
- Geometric multiplicity is at most algebraic multiplicity and at least $1$ for each eigenvalue.

## Matrix / Vector Form

**Characteristic equation**

$$
\det(A-\lambda I) = 0.
$$

**Diagonalization**: if $A=PDP^{-1}$ with $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ and columns of $P$ eigenvectors, then

$$
A^k = PD^k P^{-1}
$$

for integers $k\geq 0$ (and for negative $k$ if $A$ is invertible, i.e. no zero eigenvalue).

**Trace and determinant** (counting algebraic multiplicity):

$$
\operatorname{tr}(A)=\sum_i \lambda_i, \qquad \det(A)=\prod_i \lambda_i.
$$

## Geometric Interpretation

- On the line spanned by $\mathbf{v}$, $A$ acts as scaling by $\lambda$.
- $\lambda=1$: fixed directions; $\lambda=-1$: flips; $\lvert\lambda\rvert<1$: contraction along that axis (in iterative maps).

## Worked Example

$$
A=\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.
$$

$$
A-\lambda I=\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix},
\quad
\det(A-\lambda I)=(2-\lambda)^2-1=(\lambda-1)(\lambda-3).
$$

Eigenvalues $\lambda=1$ and $\lambda=3$.

For $\lambda=1$: $(A-I)\mathbf{v}=\mathbf{0}$ gives $v_1+v_2=0$, so $\mathbf{v}=\langle 1,-1\rangle$.

For $\lambda=3$: $(A-3I)\mathbf{v}=\mathbf{0}$ gives $-v_1+v_2=0$, so $\mathbf{v}=\langle 1,1\rangle$.

## Common Mistakes

- Writing $\det(A-\lambda I)=0$ as $\det(\lambda I-A)=0$ without tracking sign: both are fine if used consistently ($p(\lambda)=\det(\lambda I-A)$ is monic).
- Allowing $\mathbf{v}=\mathbf{0}$ as an eigenvector.
- Assuming every real matrix has a full set of real eigenvectors.
- Confusing algebraic and geometric multiplicity.

## Connections

- Related: [[Determinants]], [[Vector Spaces and Bases]], [[Orthogonality and Projections]] (symmetric matrices: real orthonormal eigenbases)
- Next: [[Orthogonality and Projections]], [[Least Squares and QR]]
- Applications: spectral methods, PCA, differential systems

## References

Eigenvalue theory as in MIT 18.06.[^mit-eigen]

[^mit-eigen]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
