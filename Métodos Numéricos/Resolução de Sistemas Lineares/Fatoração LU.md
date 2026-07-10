---
dg-publish: true
---

# LU Factorization

## Summary

LU factorization writes a nonsingular matrix as $A=LU$ with $L$ unit lower triangular and $U$ upper triangular. Solving $Ax=b$ becomes $Ly=b$ then $Ux=y$. With row exchanges, the stable form is $PA=LU$.

## Prerequisites

- [[Métodos Diretos - Sistema Triangular]]
- [[Método de Eliminação de Gauss]]

## Problem Type

Factor $A$ once, then solve one or many systems with different right-hand sides.

## Method Definition

Without pivoting (Doolittle form): run Gaussian elimination on $A$, store multipliers $m_{ij}$ in the strict lower part of $L$ (unit diagonal), and store the resulting upper matrix in $U$.[^burden]

With partial pivoting: apply row swaps, track them in a permutation matrix $P$, and obtain $PA=LU$.

## Assumptions / Requirements

- All leading principal minors nonzero for $A=LU$ without pivoting
- Otherwise use partial pivoting ($PA=LU$)
- Convention here: $\operatorname{diag}(L)=1$

## Algorithm (no pivoting)

1. Set $U\leftarrow A$, $L\leftarrow I$.
2. For $k=1,\ldots,n-1$:
   - For $i=k+1,\ldots,n$:
     - $\ell_{ik}\leftarrow u_{ik}/u_{kk}$
     - Row $i$ of $U$ $\leftarrow$ row $i - \ell_{ik}\cdot$ row $k$
3. Solve $Ly=b$, then $Ux=y$.

## Algorithm (partial pivoting)

At stage $k$, swap for the largest $|u_{ik}|$ with $i\ge k$, record the swap in $P$, then eliminate as above (also swap the already-computed part of $L$ consistently). Result: $PA=LU$.

## Worked Example

$$
A=\begin{pmatrix}2&3&1\\4&7&7\\6&18&22\end{pmatrix}
$$

Stage $k=1$: multipliers $\ell_{21}=2$, $\ell_{31}=3$.

$$
U\leftarrow\begin{pmatrix}2&3&1\\0&1&5\\0&9&19\end{pmatrix}
$$

Stage $k=2$: multiplier $\ell_{32}=9/1=9$.

$$
U\leftarrow\begin{pmatrix}2&3&1\\0&1&5\\0&0&-26\end{pmatrix},\quad
L=\begin{pmatrix}1&0&0\\2&1&0\\3&9&1\end{pmatrix}
$$

Check $LU=A$:

$$
LU=\begin{pmatrix}2&3&1\\4&7&7\\6&18&22\end{pmatrix}=A.
$$

Solve $Ax=b$ with $b=(1,2,3)^\top$. First $Ly=b$:

$$
y_1=1,\qquad y_2=2-2\cdot 1=0,\qquad y_3=3-3\cdot 1-9\cdot 0=0.
$$

Then $Ux=y$: $x_3=0$, $x_2=0$, $x_1=1/2$. Check: $A(1/2,0,0)^\top$ is half the first column of $A$, namely $(1,2,3)^\top=b$, so the residual is zero.

## Convergence

Direct $O(n^3)$ factorization; each subsequent solve is $O(n^2)$.

## Error / Accuracy

Verify $LU\approx A$ (or $PA\approx LU$) and the residual of $Ax=b$. Prefer pivoting when pivots are small.

## Common Failure Modes

- Zero pivot without row exchange
- Forgetting that $L$ stores multipliers from elimination
- Confusing $A=LU$ with $PA=LU$ after swaps

## Connections

- [[Método de Eliminação de Gauss]]
- [[Métodos Diretos - Sistema Triangular]]
- [[Resolução de Sistemas Lineares]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, LU factorization; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
