---
dg-publish: true
---

# Lagrange Interpolating Polynomial

## Summary

Lagrange form writes the unique interpolant as a weighted sum of cardinal basis polynomials $L_i$ that satisfy $L_i(x_k)=\delta_{ik}$.

## Prerequisites

- [[Existence and Uniqueness of Interpolating Polynomial]]
- Product notation for polynomials

## Problem Type

Given distinct nodes $x_0,\ldots,x_n$ and values $y_i$, construct $P$ with $P(x_i)=y_i$.

## Method Definition

$$
P(x)=\sum_{i=0}^{n} y_i L_i(x),\qquad
L_i(x)=\prod_{\substack{j=0\\ j\neq i}}^{n}\frac{x-x_j}{x_i-x_j}.
$$

Each $L_i$ has degree $n$, $L_i(x_i)=1$, and $L_i(x_j)=0$ for $j\neq i$. The product is over $j\neq i$ only.[^burden]

## Assumptions / Requirements

- Distinct $x_i$
- Exact arithmetic ignores cancellation; numerically, barycentric Lagrange is preferred for evaluation

## Algorithm

1. For each $i$, form $L_i(x)$ as the product over $j\neq i$.
2. Sum $y_i L_i(x)$.
3. Optionally expand into monomial form for inspection.

## Error / Accuracy

If $y_i=f(x_i)$ with $f\in C^{n+1}$, then for some $\xi$ between the nodes and $x$,

$$
f(x)-P(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x-x_i).
$$

If $|f^{(n+1)}|\le M$ on the interval of interest,

$$
|f(x)-P(x)|\le \frac{M}{(n+1)!}\left|\prod_{i=0}^{n}(x-x_i)\right|.
$$

## Worked Example

Nodes $(0,2)$, $(1,3)$, $(2,5)$.

$$
\begin{aligned}
L_0(x)&=\frac{(x-1)(x-2)}{(0-1)(0-2)}=\frac{(x-1)(x-2)}{2}=\frac12(x^2-3x+2),\\
L_1(x)&=\frac{(x-0)(x-2)}{(1-0)(1-2)}=\frac{x(x-2)}{-1}= -x^2+2x,\\
L_2(x)&=\frac{(x-0)(x-1)}{(2-0)(2-1)}=\frac{x(x-1)}{2}=\frac12(x^2-x).
\end{aligned}
$$

$$
\begin{aligned}
P(x)&=2L_0(x)+3L_1(x)+5L_2(x)\\
&=2\cdot\tfrac12(x^2-3x+2)+3(-x^2+2x)+5\cdot\tfrac12(x^2-x)\\
&=(x^2-3x+2)+(-3x^2+6x)+\bigl(\tfrac52 x^2-\tfrac52 x\bigr)\\
&=\Bigl(1-3+\tfrac52\Bigr)x^2+\Bigl(-3+6-\tfrac52\Bigr)x+2\\
&=\tfrac12 x^2+\tfrac12 x+2.
\end{aligned}
$$

Checks: $P(0)=2$, $P(1)=1/2+1/2+2=3$, $P(2)=2+1+2=5$.

## Common Failure Modes

- Writing $\prod_j$ without excluding $j=i$
- Dropping the weights $y_i$
- High $n$ with equal spacing (Runge oscillations)

## Connections

- [[Newton Polynomial]] (same $P$, different basis)
- [[Polynomial Interpolation by Definition]]
- [[Polynomial Interpolation]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Lagrange interpolation; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
