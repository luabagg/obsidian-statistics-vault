---
dg-publish: true
tags:
  - linear-algebra
  - least-squares
  - qr
aliases:
  - Least Squares
  - QR Factorization
  - Normal Equations
---

# Least Squares and QR

## Summary

When $A\mathbf{x}=\mathbf{b}$ is inconsistent, least squares finds $\hat{\mathbf{x}}$ minimizing $\|A\mathbf{x}-\mathbf{b}\|$. The residual is orthogonal to $\operatorname{Col}(A)$. QR factorization provides a stable way to compute $\hat{\mathbf{x}}$ without forming $A^T A$ explicitly in unstable ways.

## Prerequisites

[[Orthogonality and Projections]], [[Matrices and Row Reduction]], [[Systems of Linear Equations]]. Hub: [[Álgebra Linear]].

## Definition / Statement

Given $A\in\mathbb{R}^{m\times n}$ and $\mathbf{b}\in\mathbb{R}^m$, a **least-squares solution** is any $\hat{\mathbf{x}}\in\mathbb{R}^n$ minimizing

$$
\|A\mathbf{x}-\mathbf{b}\|_2 = \sqrt{(A\mathbf{x}-\mathbf{b})\cdot(A\mathbf{x}-\mathbf{b})}.
$$

If the columns of $A$ are linearly independent, $\hat{\mathbf{x}}$ is unique and satisfies the **normal equations**

$$
A^T A\hat{\mathbf{x}} = A^T\mathbf{b}.
$$

A **QR factorization** of full-column-rank $A$ writes

$$
A = QR,
$$

where $Q\in\mathbb{R}^{m\times n}$ has orthonormal columns ($Q^T Q=I_n$) and $R\in\mathbb{R}^{n\times n}$ is upper triangular and invertible.

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $A$ | data / design matrix | $m\times n$, typically $m\geq n$ |
| $\mathbf{b}$ | observations | $m\times 1$ |
| $\hat{\mathbf{x}}$ | least-squares coefficient vector | $n\times 1$ |
| $Q,R$ | thin QR factors | $m\times n$, $n\times n$ |
| $\mathbf{r}=\mathbf{b}-A\hat{\mathbf{x}}$ | residual | $m\times 1$ |

## Notation

| Symbol | Meaning |
|---|---|
| $\|\,\cdot\,\|_2$ | Euclidean norm |
| $A^T A\hat{\mathbf{x}}=A^T\mathbf{b}$ | normal equations |
| $A=QR$ | thin QR factorization |

## Conditions / Assumptions

- Prefer the Euclidean norm (least squares = $L^2$).
- Unique $\hat{\mathbf{x}}$ when $\operatorname{rank}(A)=n$ (full column rank), so $A^T A$ is invertible.
- If columns are dependent, least-squares solutions still exist but are not unique; use pseudoinverse or additional constraints.
- QR assumes full column rank for the thin $R$ to be invertible.

## Matrix / Vector Form

**Normal equations**

$$
A^T A\hat{\mathbf{x}} = A^T\mathbf{b}, \qquad
\hat{\mathbf{x}} = (A^T A)^{-1}A^T\mathbf{b}
\quad(\operatorname{rank} A = n).
$$

**Geometry**: $A\hat{\mathbf{x}}=\operatorname{proj}_{\operatorname{Col}(A)}\mathbf{b}$ and $A^T(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$.

**Via QR** ($A=QR$):

$$
A^T A = R^T Q^T Q R = R^T R,
$$
$$
R^T R\hat{\mathbf{x}} = R^T Q^T\mathbf{b} \implies R\hat{\mathbf{x}} = Q^T\mathbf{b}
$$

(solve by forward/back substitution on the triangular system).

## Procedure

1. Check whether $A\mathbf{x}=\mathbf{b}$ is consistent; if not, use least squares.
2. If using normal equations: form $A^T A$ and $A^T\mathbf{b}$, solve the $n\times n$ system (watch conditioning).
3. If using QR: factor $A=QR$ (Gram–Schmidt, Householder, or library routine), solve $R\hat{\mathbf{x}}=Q^T\mathbf{b}$.
4. Report residual norm $\|\mathbf{b}-A\hat{\mathbf{x}}\|$ as a fit diagnostic.

## Worked Example

Fit a line $y = c_0 + c_1 x$ through points $(0,1)$, $(1,1)$, $(2,3)$ in the least-squares sense.

$$
A=\begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix},
\quad
\mathbf{b}=\begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix},
\quad
\mathbf{c}=\begin{pmatrix} c_0 \\ c_1 \end{pmatrix}.
$$

$$
A^T A=\begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix},
\quad
A^T\mathbf{b}=\begin{pmatrix} 5 \\ 7 \end{pmatrix}.
$$

Solve $\begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}\begin{pmatrix} c_0 \\ c_1 \end{pmatrix}=\begin{pmatrix} 5 \\ 7 \end{pmatrix}$:
subtract first equation from second after scaling gives $2c_1=2$, so $c_1=1$, then $3c_0+3=5$, so $c_0=\tfrac{2}{3}$.

Model: $y=\tfrac{2}{3}+x$.

## Common Mistakes

- Minimizing $\|A^T\mathbf{x}-\mathbf{b}\|$ instead of $\|A\mathbf{x}-\mathbf{b}\|$.
- Using $A^{-1}$ when $A$ is not square.
- Ignoring rank deficiency when $A^T A$ is singular.
- Forgetting that least squares yields the projection of $\mathbf{b}$ onto $\operatorname{Col}(A)$, not necessarily $\mathbf{b}$ itself.

## Connections

- Related: [[Orthogonality and Projections]], [[Matrices and Row Reduction]], [[Systems of Linear Equations]]
- Applied statistics/numerics: [[Mínimos Quadrados]] when present under numerical methods
- Next: applications in regression and numerical linear algebra under [[Métodos Numéricos]]

## References

Least squares and QR as in MIT 18.06.[^mit-ls]

[^mit-ls]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
