---
dg-publish: true
tags:
  - numerical-methods
  - interpolation
aliases:
  - Interpolation by Definition
---

# Polynomial Interpolation by Definition

## Summary

The interpolating polynomial can be written in the monomial basis and found by solving a Vandermonde system. Existence and uniqueness for distinct nodes guarantee a single solution of degree at most $n$.

## Prerequisites

[[Existence and Uniqueness of Interpolating Polynomial]], [[Systems of Linear Equations]]

## Method Definition

Seek $P(x)=c_0+c_1x+\cdots+c_n x^n$ such that $P(x_i)=y_i$ for distinct $x_0,\ldots,x_n$. In matrix form,

$$
\begin{pmatrix}
1&x_0&\cdots&x_0^n\\
\vdots&\vdots&\ddots&\vdots\\
1&x_n&\cdots&x_n^n
\end{pmatrix}
\begin{pmatrix}c_0\\\vdots\\c_n\end{pmatrix}
=
\begin{pmatrix}y_0\\\vdots\\y_n\end{pmatrix}.
$$

## Worked Example

Nodes $(0,2),(1,3)$: solve $c_0=2$, $c_0+c_1=3$ → $P(x)=2+x$.

## Common Failure Modes

- Repeated nodes make the Vandermonde matrix singular.
- High $n$ yields ill-conditioned Vandermonde systems; prefer Newton form in practice.

## Connections

- Related: [[Lagrange Polynomial]], [[Newton Polynomial]]

## References

Vandermonde interpolation is the monomial-basis form of the unique interpolant.[^dlmf-interp]

[^dlmf-interp]: NIST DLMF, *§3.3 Interpolation*, https://dlmf.nist.gov/3.3
