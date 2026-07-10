---
dg-publish: true
---

# Direct Methods: Triangular Systems

## Summary

After elimination or factorization, linear systems reduce to triangular solves. Forward substitution handles lower-triangular $L$; back substitution handles upper-triangular $U$.

## Prerequisites

- Matrix notation for $Ax=b$
- Nonzero diagonal pivots

## Problem Type

Solve $Lx=b$ or $Ux=b$ with $L$ lower triangular and $U$ upper triangular.

## Method Definition

**Forward substitution** for $Lx=b$ with $l_{ii}\neq 0$:

$$
x_1=\frac{b_1}{l_{11}},\qquad
x_i=\frac{1}{l_{ii}}\left(b_i-\sum_{j=1}^{i-1} l_{ij}x_j\right),\quad i=2,\ldots,n.
$$

**Back substitution** for $Ux=b$ with $u_{ii}\neq 0$:

$$
x_n=\frac{b_n}{u_{nn}},\qquad
x_i=\frac{1}{u_{ii}}\left(b_i-\sum_{j=i+1}^{n} u_{ij}x_j\right),\quad i=n-1,\ldots,1.
$$

## Assumptions / Requirements

- Square triangular matrix with nonzero diagonals
- Exact arithmetic cost is $O(n^2)$

## Algorithm

1. Confirm triangular structure and $a_{ii}\neq 0$.
2. Sweep down (forward) or up (back), substituting known unknowns immediately.
3. Optionally form residual $b-Ax$ for verification.

## Worked Example

Upper triangular:

$$
U=\begin{pmatrix}3&-1&2\\0&4&1\\0&0&5\end{pmatrix},\quad
b=\begin{pmatrix}5\\6\\10\end{pmatrix}
$$

$$
x_3=\frac{10}{5}=2,\quad
x_2=\frac{6-1\cdot 2}{4}=1,\quad
x_1=\frac{5-(-1)\cdot 1-2\cdot 2}{3}=\frac{2}{3}.
$$

Check: $Ux=(5,6,10)^\top=b$.

Lower triangular:

$$
L=\begin{pmatrix}2&0&0\\3&5&0\\1&-2&4\end{pmatrix},\quad
b=\begin{pmatrix}4\\9\\-3\end{pmatrix}
$$

$$
x_1=2,\quad
x_2=\frac{9-3\cdot 2}{5}=\frac{3}{5},\quad
x_3=\frac{-3-1\cdot 2-(-2)(3/5)}{4}=\frac{-3-2+6/5}{4}=-\frac{19}{20}.
$$

## Common Failure Modes

- Zero pivot on the diagonal
- Treating a nearly triangular matrix as exact without residual checks

## Connections

- [[Método de Eliminação de Gauss]], [[Fatoração LU]]
- [[Resolução de Sistemas Lineares]]

## References

Standard triangular solves after Gaussian elimination / LU factorization.[^burden]

[^burden]: Burden & Faires, *Numerical Analysis*; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
