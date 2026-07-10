---
dg-publish: true
dg-show-local-graph: true
---

# Solving Linear Systems

## Summary

This path solves linear algebraic systems $Ax=b$ with $A\in\mathbb{R}^{n\times n}$. Direct methods factor or triangularize $A$; iterative methods build a sequence $x^{(k)}\to x$.

## Prerequisites

- Matrix–vector products and elementary row operations
- Norms and the idea of residual $r=b-Ax$

## Linear Maps (Not Affine Lines)

A map $T$ is **linear** when

$$
T(u+v)=T(u)+T(v),\qquad T(cu)=c\,T(u)
$$

for all vectors $u,v$ and scalars $c$.[^lax]

In particular, $T(x)=ax+b$ with $b\neq 0$ is **affine**, not linear, because $T(0)=b\neq 0$. Linear systems in this path are of the form $Ax=b$, where the unknown enters linearly through the matrix $A$. (The system is still called linear when $b\neq 0$.)

## Learning Order

1. [[Direct Methods - Triangular System]] — forward/back substitution
2. [[Gaussian Elimination]] — triangularization + back substitution
3. [[LU Factorization]] — $A=LU$ or $PA=LU$
4. [[Iterative Methods]] — fixed-point form $x^{(k+1)}=Tx^{(k)}+c$
5. [[Gauss-Jacobi Method]]
6. [[Gauss-Seidel Method]]
7. [[Sufficient Convergence Condition for Gauss-Jacobi]]

## Topic Map

%% Begin Waypoint %%

- [[Numerical Methods/Linear Systems/Solving Linear Systems]]
	- [[LU Factorization]]
	- [[Gaussian Elimination]]
	- [[Gauss-Jacobi Method]]
	- [[Gauss-Seidel Method]]
	- [[Direct Methods - Triangular System]]
	- [[Iterative Methods]]
	- [[Sufficient Convergence Condition for Gauss-Jacobi]]

%% End Waypoint %%

## Direct vs Iterative

| Family | Idea | Typical use |
| --- | --- | --- |
| Direct | Finite arithmetic factorization / elimination | Dense moderate $n$, many $b$ after one factorization |
| Iterative | Split $A=M-N$, iterate $Mx^{(k+1)}=Nx^{(k)}+b$ | Large sparse systems, good initial guesses |

Always check the residual $\|b-Ax\|$ after computing $x$.

## Connections

- Roots of nonlinear systems often linearize to $J\Delta x=-F$
- Least squares solves normal equations $A^\top A\hat a=A^\top y$ (prefer QR in practice)
- Theory: [[Linear Algebra]]

## References

[^lax]: Definition of linear maps; standard linear algebra. Numerical methods overview: NIST DLMF Ch. 3, https://dlmf.nist.gov/3
