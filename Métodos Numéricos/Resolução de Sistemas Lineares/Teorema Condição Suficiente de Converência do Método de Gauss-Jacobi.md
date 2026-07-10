---
dg-publish: true
---

# Sufficient Convergence Condition for Gauss–Jacobi

## Summary

Strict diagonal dominance of $A$ is a practical sufficient condition for Jacobi (and often Gauss–Seidel) convergence. The sharp criterion for any stationary iteration $x^{(k+1)}=Tx^{(k)}+c$ is $\rho(T)<1$.

## Prerequisites

- [[Método de Gauss-Jacobi]]
- Matrix norms and eigenvalues (spectral radius)

## Problem Type

Decide whether Jacobi iteration for $Ax=b$ is guaranteed to converge.

## Method Definition

Jacobi matrix: with $A=D+L+U$,

$$
T_J=-D^{-1}(L+U)=I-D^{-1}A.
$$

**Spectral radius criterion (necessary and sufficient).** The iteration converges for every $x^{(0)}$ if and only if

$$
\rho(T_J)=\max_i|\lambda_i(T_J)|<1.
$$

**Norm criterion (sufficient).** If $\|T_J\|<1$ for some subordinate matrix norm, then $\rho(T_J)<1$, so the method converges.[^burden]

**Strict diagonal dominance (sufficient).** If

$$
|a_{ii}|>\sum_{j\neq i}|a_{ij}|\quad\text{for all }i,
$$

then $\|T_J\|_\infty<1$, hence Jacobi converges.

## Assumptions / Requirements

- $a_{ii}\neq 0$ so $D^{-1}$ exists
- Dominance is strict for the simple $\infty$-norm argument above

## Worked Example 1 (borderline dominance)

$$
A=\begin{pmatrix}2&1&-1\\-1&4&1\\1&-1&6\end{pmatrix}
$$

Row 1: $|2|=|1|+|-1|$ (not strict). Rows 2–3 are strictly dominant. Dominance test is inconclusive; one must inspect $\rho(T_J)$ (or run the iteration carefully).

## Worked Example 2 (strict dominance)

$$
A=\begin{pmatrix}10&-1&2&0\\-1&11&-1&3\\2&-1&10&-1\\0&3&-1&8\end{pmatrix}
$$

Each row satisfies $|a_{ii}|>\sum_{j\neq i}|a_{ij}|$, so Jacobi converges for every start.

## Error / Accuracy

Even when convergence is guaranteed, monitor $\|x^{(k+1)}-x^{(k)}\|$ and $\|b-Ax^{(k)}\|$.

## Common Failure Modes

- Treating weak dominance ($|a_{ii}|\ge\sum_{j\neq i}|a_{ij}|$) as an automatic guarantee
- Confusing sufficient conditions with necessary ones
- Applying a Jacobi bound unchanged to Gauss–Seidel without using $T_{GS}$

## Connections

- [[Método de Gauss-Jacobi]], [[Método de Gauss-Seidel]]
- [[Métodos Iterativos]]
- [[Resolução de Sistemas Lineares]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, iterative methods; Saad, *Iterative Methods for Sparse Linear Systems*; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
