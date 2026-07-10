---
dg-publish: true
---

# Gauss–Seidel Method

## Summary

Gauss–Seidel is the in-place sibling of Jacobi: each new component is used immediately in later equations of the same sweep. It often converges faster than Jacobi on the same matrix, but its iteration matrix differs.

## Prerequisites

- [[Método de Gauss-Jacobi]]
- [[Métodos Iterativos]]

## Problem Type

Iteratively solve $Ax=b$ with $a_{ii}\neq 0$.

## Method Definition

With $A=D+L+U$ (standard splitting),

$$
(D+L)x^{(k+1)}=b-Ux^{(k)},
$$

componentwise

$$
x_i^{(k+1)}=\frac{1}{a_{ii}}\left(
b_i-\sum_{j=1}^{i-1}a_{ij}x_j^{(k+1)}-\sum_{j=i+1}^{n}a_{ij}x_j^{(k)}
\right).
$$

Iteration matrix: $T_{GS}=-(D+L)^{-1}U$.[^burden]

## Assumptions / Requirements

- Nonzero diagonals
- Do **not** use $T_J=D^{-1}(L+U)$ when analyzing Gauss–Seidel

## Algorithm

1. Start from $x^{(0)}$.
2. For $i=1,\ldots,n$, overwrite $x_i$ with the formula above.
3. After a full sweep, test $\|x^{(k+1)}-x^{(k)}\|$ and/or residual.

## Convergence

- $\rho(T_{GS})<1$ is necessary and sufficient for convergence of this stationary iteration
- Strict diagonal dominance of $A$ is a **sufficient** condition
- **Sassenfeld criterion** (useful hand test for GS): define

$$
\beta_i=\frac{1}{|a_{ii}|}\left(\sum_{j<i}|a_{ij}|\beta_j+\sum_{j>i}|a_{ij}|\right)
$$

If $\max_i\beta_i<1$, Gauss–Seidel converges.

## Error / Accuracy

Same practical stops as Jacobi: step size and residual norms.

## Worked Example

$$
A=\begin{pmatrix}4&1&1\\1&5&2\\2&3&10\end{pmatrix},\quad
b=\begin{pmatrix}7\\-8\\6\end{pmatrix}
$$

Sassenfeld:

$$
\beta_1=\frac{1+1}{4}=0.5,\quad
\beta_2=\frac{1\cdot 0.5+2}{5}=0.5,\quad
\beta_3=\frac{2\cdot 0.5+3\cdot 0.5}{10}=0.25.
$$

$\max\beta_i=0.5<1$ ⇒ Gauss–Seidel converges.

For comparison only, Jacobi’s $T_J=-D^{-1}(L+U)$ has

$$
\|T_J\|_\infty=0.6<1,
$$

so Jacobi also converges here—but that bound is about **Jacobi**, not a substitute for $T_{GS}$.

One GS sweep from $x^{(0)}=0$:

$$
x_1=\frac{7}{4}=1.75,\quad
x_2=\frac{-8-1.75}{5}=-1.95,\quad
x_3=\frac{6-2\cdot 1.75-3(-1.95)}{10}=0.835.
$$

## Common Failure Modes

- Analyzing GS with Jacobi’s iteration matrix alone
- Zero pivots on the diagonal
- Confusing SOR ($\omega\neq 1$) with plain GS

## Connections

- [[Métodos Iterativos]] (includes SOR)
- [[Método de Gauss-Jacobi]]
- [[Resolução de Sistemas Lineares]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Gauss–Seidel and Sassenfeld; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
