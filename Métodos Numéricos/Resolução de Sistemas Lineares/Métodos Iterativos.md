---
dg-publish: true
---

# Iterative Methods for Linear Systems

## Summary

Stationary iterative methods rewrite $Ax=b$ as $x=Tx+c$ and generate $x^{(k+1)}=Tx^{(k)}+c$. Convergence hinges on the iteration matrix $T$.

## Prerequisites

- Matrix norms and spectral radius
- [[Resolução de Sistemas Lineares]]
- Splitting intuition from [[Método de Gauss-Jacobi]] and [[Método de Gauss-Seidel]]

## Problem Type

Approximate $x$ in $Ax=b$ by a convergent sequence, especially for large sparse $A$.

## Method Definition

Split $A=M-N$ with $M$ easy to invert. Then

$$
Mx^{(k+1)}=Nx^{(k)}+b
\quad\Leftrightarrow\quad
x^{(k+1)}=T x^{(k)}+c,
$$

where $T=M^{-1}N$ and $c=M^{-1}b$.[^saad]

Common choices:

| Method | $M$ | Notes |
| --- | --- | --- |
| Jacobi | $D=\operatorname{diag}(A)$ | Uses only $x^{(k)}$ |
| Gauss–Seidel | $D+L$ (lower incl. diagonal) | Uses newest components |
| SOR | extrapolated Gauss–Seidel | Successive over-relaxation with parameter $\omega$ |

**Successive over-relaxation (SOR)** (not “seasonal relaxation”):

$$
x_i^{(k+1)}=(1-\omega)x_i^{(k)}+\frac{\omega}{a_{ii}}\left(b_i-\sum_{j<i}a_{ij}x_j^{(k+1)}-\sum_{j>i}a_{ij}x_j^{(k)}\right).
$$

For $\omega=1$ this is Gauss–Seidel; typically $0<\omega<2$.

## Assumptions / Requirements

- $a_{ii}\neq 0$ for Jacobi/GS/SOR component updates
- Convergence requires $\rho(T)<1$ (necessary and sufficient for stationary iterations)
- $\|T\|<1$ for some matrix norm is a convenient **sufficient** condition

## Convergence

- $\rho(T)<1$ $\Leftrightarrow$ $x^{(k)}\to x^*$ for every start
- Strict diagonal dominance of $A$ is a sufficient condition for Jacobi and Gauss–Seidel
- SPD structure helps conjugate-gradient type methods (nonstationary; mentioned only for orientation)

## Error / Accuracy

Stop when $\|x^{(k+1)}-x^{(k)}\|<\varepsilon$ and/or residual $\|b-Ax^{(k)}\|<\varepsilon$.

## Worked Example (fixed-point form)

$$
A=\begin{pmatrix}4&-1\\-1&3\end{pmatrix},\quad b=\begin{pmatrix}2\\5\end{pmatrix}
$$

Jacobi updates:

$$
x_1^{(k+1)}=\frac{1}{4}\big(2+x_2^{(k)}\big),\qquad
x_2^{(k+1)}=\frac{1}{3}\big(5+x_1^{(k)}\big)
$$

so

$$
T_J=\begin{pmatrix}0&1/4\\1/3&0\end{pmatrix},\quad
c=\begin{pmatrix}1/2\\5/3\end{pmatrix}.
$$

Gauss–Seidel uses the new $x_1^{(k+1)}$ immediately in the second equation:

$$
x_2^{(k+1)}=\frac{1}{3}\big(5+x_1^{(k+1)}\big).
$$

Its iteration matrix is **not** $T_J$; do not reuse the Jacobi matrix when claiming Seidel convergence rates.

## Common Failure Modes

- Using Jacobi’s $T$ to conclude Gauss–Seidel convergence without recomputing $T_{GS}$
- $\omega\notin(0,2)$ for SOR
- Ignoring that $\rho(T)<1$ is the sharp criterion, while diagonal dominance is only sufficient

## Connections

- [[Método de Gauss-Jacobi]], [[Método de Gauss-Seidel]]
- [[Teorema Condição Suficiente de Converência do Método de Gauss-Jacobi]]
- [[Resolução de Sistemas Lineares]]

## References

[^saad]: Y. Saad, *Iterative Methods for Sparse Linear Systems*; also Burden & Faires; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
