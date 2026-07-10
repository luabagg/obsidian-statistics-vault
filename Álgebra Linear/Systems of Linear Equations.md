---
dg-publish: true
tags:
  - linear-algebra
  - systems
aliases:
  - Linear Systems
  - Simultaneous Equations
---

# Systems of Linear Equations

## Summary

A linear system asks for all vectors $\mathbf{x}$ satisfying $A\mathbf{x}=\mathbf{b}$. The solution set is empty, a single point, or an affine subspace. Matrix form and geometry of intersecting hyperplanes organize the theory.

## Prerequisites

High-school systems of equations; [[Vectors and Dot Product]] helpful. Hub: [[Álgebra Linear]].

## Definition / Statement

A **linear equation** in unknowns $x_1,\ldots,x_n$ has the form

$$
a_1 x_1 + \cdots + a_n x_n = b.
$$

A **system** of $m$ linear equations is

$$
\begin{aligned}
a_{11}x_1 + \cdots + a_{1n}x_n &= b_1, \\
&\vdots \\
a_{m1}x_1 + \cdots + a_{mn}x_n &= b_m.
\end{aligned}
$$

In matrix form, with $A=(a_{ij})\in\mathbb{R}^{m\times n}$, $\mathbf{x}\in\mathbb{R}^n$, $\mathbf{b}\in\mathbb{R}^m$,

$$
A\mathbf{x} = \mathbf{b}.
$$

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $A$ | coefficient matrix | $m \times n$ |
| $\mathbf{x}$ | unknown vector | $n \times 1$ |
| $\mathbf{b}$ | right-hand side | $m \times 1$ |
| $[A\mid\mathbf{b}]$ | augmented matrix | $m \times (n+1)$ |

## Notation

| Symbol | Meaning |
|---|---|
| $A\mathbf{x}=\mathbf{b}$ | matrix form of the system |
| consistent | at least one solution |
| inconsistent | no solution |
| free variable | variable not forced by a pivot |

## Conditions / Assumptions

- Entries real unless stated otherwise.
- **Linear** means no products of unknowns, no powers other than $1$, and no nonlinear functions of unknowns. The equation $A\mathbf{x}+\mathbf{c}=\mathbf{b}$ is still linear in $\mathbf{x}$ after moving $\mathbf{c}$; the map $\mathbf{x}\mapsto A\mathbf{x}+\mathbf{c}$ is affine, not linear, if $\mathbf{c}\neq\mathbf{0}$.

## Matrix / Vector Form

Equivalent views of $A\mathbf{x}=\mathbf{b}$:

1. **Row view**: each equation is a hyperplane (dot product of a row of $A$ with $\mathbf{x}$ equals $b_i$).
2. **Column view**: $\mathbf{b}$ is a linear combination of the columns of $A$ with coefficients $x_j$.

## Geometric Interpretation

- $n=2$: lines in the plane; solutions are empty, a point, or a line.
- $n=3$: planes in space; solutions are empty, a point, a line, or a plane.

If $\mathbf{b}=\mathbf{0}$ (**homogeneous system**), $\mathbf{x}=\mathbf{0}$ is always a solution; extra solutions form a subspace (the null space of $A$).

## Procedure

1. Form the augmented matrix $[A\mid\mathbf{b}]$.
2. Row-reduce (see [[Matrices and Row Reduction]]) to row echelon or reduced row echelon form.
3. Read pivot variables and free variables; parametrize the solution set.
4. Declare inconsistency if a row $[0\ \cdots\ 0\mid c]$ with $c\neq 0$ appears.

## Worked Example

$$
\begin{cases}
x + y = 3, \\
2x + 2y = 6.
\end{cases}
$$

The second equation is twice the first, so the system is consistent with infinitely many solutions: $y = 3 - x$, free variable $x=t$, so $\mathbf{x} = \langle t,\, 3-t\rangle$.

If the second right-hand side were $7$, the system would be inconsistent.

## Common Mistakes

- Calling $y = mx + b$ a linear map in $x$ without rewriting; as a function of one variable with intercept, it is affine.
- Forgetting free variables when rank $A < n$.
- Concluding uniqueness from $m=n$ without checking invertibility/rank.

## Connections

- Related: [[Matrices and Row Reduction]], [[Determinants]], [[Vector Spaces and Bases]]
- Next: [[Matrices and Row Reduction]]
- Geometry: [[Lines and Planes]]

## References

Linear systems and solution geometry follow MIT 18.06 and standard introductory linear algebra.[^mit-systems]

[^mit-systems]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
