---
dg-publish: true
---

# Gaussian Elimination

## Summary

Gaussian elimination transforms $Ax=b$ into an upper-triangular system $Ux=c$ by elementary row operations, then recovers $x$ by back substitution. Partial pivoting improves numerical stability.

## Prerequisites

- [[Métodos Diretos - Sistema Triangular]]
- Elementary row operations

## Problem Type

Solve a square linear system $Ax=b$.

## Method Definition

Form the augmented matrix $[A|b]$. For each column $k=1,\ldots,n-1$, eliminate entries below the pivot $a_{kk}$ using multipliers $m_{ik}=a_{ik}/a_{kk}$. After triangularization, apply back substitution.[^burden]

With partial pivoting, swap row $k$ with the row of largest $|a_{ik}|$ for $i\ge k$ before eliminating.

## Assumptions / Requirements

- $A$ nonsingular (all pivots nonzero after possible row swaps)
- Prefer partial pivoting in floating-point arithmetic

## Algorithm

1. For $k=1$ to $n-1$:
   - Pivot: choose $p\ge k$ maximizing $|a_{pk}|$; swap rows $k$ and $p$ (and entries of $b$).
   - For $i=k+1$ to $n$: $m\leftarrow a_{ik}/a_{kk}$; row $i\leftarrow$ row $i - m\cdot$ row $k$.
2. Back-substitute on the resulting upper-triangular system.

## Convergence

Direct method: finishes in finitely many arithmetic operations ($O(n^3)$). No iteration.

## Error / Accuracy

Primary check: residual $r=b-Ax$. In exact arithmetic $r=0$. In floating point, small $\|r\|$ relative to $\|A\|\|x\|+\|b\|$ indicates a consistent solve.

## Worked Example

Solve

$$
\begin{cases}
2x+3y-z=1\\
4x-y+2z=7\\
-2x+2y+5z=0
\end{cases}
$$

Augmented matrix:

$$
\left[\begin{array}{ccc|c}
2&3&-1&1\\
4&-1&2&7\\
-2&2&5&0
\end{array}\right]
$$

Eliminate column 1:

$$
R_2\leftarrow R_2-2R_1,\quad R_3\leftarrow R_3+R_1
$$

$$
\left[\begin{array}{ccc|c}
2&3&-1&1\\
0&-7&4&5\\
0&5&4&1
\end{array}\right]
$$

Eliminate $y$ in row 3. Multiplier $m=5/(-7)=-5/7$, so

$$
R_3\leftarrow R_3-m R_2 = R_3+\frac{5}{7}R_2:
$$

$$
\left[\begin{array}{ccc|c}
2&3&-1&1\\
0&-7&4&5\\
0&0&\dfrac{48}{7}&\dfrac{32}{7}
\end{array}\right]
$$

Back substitution:

$$
z=\frac{32/7}{48/7}=\frac{2}{3},
$$

$$
-7y+4\cdot\frac{2}{3}=5\Rightarrow -7y=\frac{7}{3}\Rightarrow y=-\frac{1}{3},
$$

$$
2x+3\left(-\frac{1}{3}\right)-\frac{2}{3}=1\Rightarrow 2x=\frac{8}{3}\Rightarrow x=\frac{4}{3}.
$$

Solution: $\left(\frac{4}{3},-\frac{1}{3},\frac{2}{3}\right)$. Residual:

$$
A\begin{pmatrix}4/3\\-1/3\\2/3\end{pmatrix}-\begin{pmatrix}1\\7\\0\end{pmatrix}=\mathbf{0}.
$$

## Common Failure Modes

- Zero/tiny pivot without swapping
- Arithmetic sign errors in multipliers (classic source of wrong $z$)
- Accepting $x$ without checking $b-Ax$

## Connections

- [[Fatoração LU]] records the same multipliers in $L$
- [[Métodos Iterativos]] for large sparse alternatives
- [[Resolução de Sistemas Lineares]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Gaussian elimination; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
