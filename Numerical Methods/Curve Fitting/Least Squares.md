---
dg-publish: true
---

# Least Squares

## Summary

Linear least squares chooses parameters of a model that is linear in those parameters by minimizing the sum of squared residuals. For a straight line, the normal equations give a unique solution when the $x_i$ are not all equal.

## Prerequisites

- Summation notation and $2\times 2$ linear systems
- [[Curve Fitting]]
- Optional: matrix form $A^\top A\hat a=A^\top y$

## Problem Type

Given data $(x_i,y_i)_{i=1}^n$, fit $f(x)=a+bx$ (or a polynomial linear in coefficients) by minimizing

$$
E(a,b)=\sum_{i=1}^{n}\big(y_i-(a+bx_i)\big)^2.
$$

## Method Definition

Set $\partial E/\partial a=0$ and $\partial E/\partial b=0$ to obtain the **normal equations**:[^burden]

$$
\begin{cases}
n a + b\sum x_i = \sum y_i\\
a\sum x_i + b\sum x_i^2 = \sum x_i y_i
\end{cases}
$$

Matrix form: with design matrix

$$
A=\begin{pmatrix}1&x_1\\ \vdots&\vdots\\ 1&x_n\end{pmatrix},\quad
\hat a=\begin{pmatrix}a\\ b\end{pmatrix},\quad
y=\begin{pmatrix}y_1\\ \vdots\\ y_n\end{pmatrix},
$$

$$
A^\top A\,\hat a = A^\top y.
$$

Prefer solving $\min\|A\hat a-y\|_2$ via QR rather than forming $A^\top A$ when $n$ is large or columns are poorly scaled.

## Assumptions / Requirements

- Model linear in parameters
- $A$ full column rank (for a unique minimizer)
- Squared error criterion (sensitive to outliers)

## Algorithm

1. Compute sums $n$, $\sum x$, $\sum y$, $\sum x^2$, $\sum xy$.
2. Solve the $2\times 2$ normal system for $(a,b)$.
3. Report residuals $r_i=y_i-(a+bx_i)$ and $E=\sum r_i^2$.

## Worked Example 1 — three points

Data: $(1,2)$, $(2,3)$, $(3,5)$.

$$
n=3,\ \sum x=6,\ \sum y=10,\ \sum x^2=14,\ \sum xy=23.
$$

$$
\begin{cases}
3a+6b=10\\
6a+14b=23
\end{cases}
$$

Multiply the first equation by 2: $6a+12b=20$. Subtract from the second: $2b=3\Rightarrow b=3/2$. Then $3a+6\cdot(3/2)=10\Rightarrow 3a+9=10\Rightarrow a=1/3$.

Fitted line:

$$
f(x)=\frac13 + \frac32 x.
$$

(Intercept $1/3$, slope $1.5$ — **not** intercept $0.5$.)

## Worked Example 2 — four points

Data: $(1,2)$, $(2,3)$, $(3,5)$, $(4,4)$.

$$
n=4,\ \sum x=10,\ \sum y=14,\ \sum x^2=30,\ \sum xy=39.
$$

$$
\begin{cases}
4a+10b=14\\
10a+30b=39
\end{cases}
$$

From the first equation, $2a+5b=7$, so $a=(7-5b)/2$. Substitute into the second:

$$
10\cdot\frac{7-5b}{2}+30b=39 \Rightarrow 5(7-5b)+30b=39 \Rightarrow 35+5b=39 \Rightarrow b=0.8.
$$

Then $4a+8=14\Rightarrow a=1.5$. Fitted line: $f(x)=1.5+0.8x$.

## Error / Accuracy

Minimizing $E$ does not imply every residual is small. Always inspect residuals and, for inference, model assumptions.

## Common Failure Modes

- Swapping slope and intercept in the normal system
- Using $\sum xy=20$ for the three-point example (correct value is $23$)
- Solving overdetermined systems as if they were square interpolants

## Connections

- [[Curve Fitting]]
- [[Numerical Methods/Linear Systems/Solving Linear Systems]]
- [[Polynomial Interpolation]] (exact fit when $m=n+1$ and degree $n$)

## References

[^burden]: Burden & Faires, *Numerical Analysis*, least squares; Golub & Van Loan, *Matrix Computations*; NIST/SEMATECH e-Handbook, https://www.itl.nist.gov/div898/handbook/
