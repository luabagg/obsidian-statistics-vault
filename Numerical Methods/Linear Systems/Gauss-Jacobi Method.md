---
dg-publish: true
---

# Gauss–Jacobi Method

## Summary

Jacobi iteration updates every unknown from the previous full vector. It is simple to parallelize and converges when the iteration matrix has spectral radius less than one (strict diagonal dominance is a common sufficient test).

## Prerequisites

- [[Iterative Methods]]
- Component form of $Ax=b$

## Problem Type

Iteratively solve $Ax=b$ with $a_{ii}\neq 0$.

## Method Definition

Write $A=D+L+U$ with $D$ diagonal and $L,U$ strict lower/upper parts. Jacobi uses

$$
x^{(k+1)}=D^{-1}\big(b-(L+U)x^{(k)}\big),
$$

or componentwise

$$
x_i^{(k+1)}=\frac{1}{a_{ii}}\left(b_i-\sum_{j\neq i}a_{ij}x_j^{(k)}\right).
$$

Iteration matrix: $T_J=-D^{-1}(L+U)=I-D^{-1}A$.[^burden]

## Assumptions / Requirements

- Nonzero diagonals
- Prefer a starting vector $x^{(0)}$ (often $0$)

## Algorithm

1. Choose $x^{(0)}$, tolerance $\varepsilon$, max iterations.
2. For each $i$, compute $x_i^{\text{new}}$ from all $x_j^{\text{old}}$, $j\neq i$.
3. Set $x^{\text{old}}\leftarrow x^{\text{new}}$ only after all $i$ are updated.
4. Stop on $\|x^{\text{new}}-x^{\text{old}}\|_\infty<\varepsilon$ or residual test.

## Convergence

Converges for every start iff $\rho(T_J)<1$. Strict diagonal dominance of $A$ is sufficient. See [[Sufficient Convergence Condition for Gauss-Jacobi]].

## Error / Accuracy

Use infinity-norm step and residual $\|b-Ax\|_\infty$.

## Worked Example

$$
\begin{cases}
2x_1+x_2=8\\
x_1+3x_2=10
\end{cases}
\qquad\Rightarrow\qquad
\begin{aligned}
x_1^{(k+1)}&=\frac12(8-x_2^{(k)})\\
x_2^{(k+1)}&=\frac13(10-x_1^{(k)})
\end{aligned}
$$

With $x^{(0)}=(0,0)$:

| $k$ | $x_1$ | $x_2$ |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 4 | $10/3\approx 3.333$ |
| 2 | $2.333$ | $2$ |
| 3 | $3$ | $2.556$ |
| 4 | $2.722$ | $2.333$ |

True solution: $(x_1,x_2)=(14/5,12/5)=(2.8,2.4)$. Residual of iterates shrinks toward zero.

## Common Failure Modes

- Zero diagonal entry
- Updating in place (that would be Gauss–Seidel)
- Expecting convergence without $\rho(T_J)<1$

## Connections

- [[Gauss-Seidel Method]]
- [[Iterative Methods]]
- [[Numerical Methods/Linear Systems/Solving Linear Systems]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Jacobi iteration; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
