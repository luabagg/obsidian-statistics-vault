---
dg-publish: true
tags:
  - linear-algebra
  - matrices
  - row-reduction
aliases:
  - Gaussian Elimination
  - Row Echelon Form
  - Matrix Algebra
---

# Matrices and Row Reduction

## Summary

Matrices represent linear maps and store coefficients of linear systems. Elementary row operations implement Gaussian elimination, producing row echelon forms that reveal rank, invertibility, and solution structure.

## Prerequisites

[[Systems of Linear Equations]]. Hub: [[Linear Algebra]].

## Definition / Statement

An $m\times n$ **matrix** $A$ is a rectangular array of scalars $a_{ij}$. Matrix–vector multiplication $A\mathbf{x}$ defines a map $\mathbb{R}^n\to\mathbb{R}^m$ that is linear:

$$
A(\mathbf{u}+\mathbf{v}) = A\mathbf{u}+A\mathbf{v}, \qquad A(c\mathbf{u}) = c\,A\mathbf{u}.
$$

**Elementary row operations** on a matrix:

1. Swap two rows.
2. Multiply a row by a nonzero scalar.
3. Add a scalar multiple of one row to another row.

These operations do not change the solution set of $A\mathbf{x}=\mathbf{b}$ when applied to the augmented matrix.

## Objects and Dimensions

| Object | Meaning | Dimensions |
|---|---|---|
| $A$ | matrix | $m\times n$ |
| $A\mathbf{x}$ | linear map applied to $\mathbf{x}$ | $m\times 1$ |
| $AB$ | product (columns of $B$ mapped by $A$) | $m\times p$ if $B$ is $n\times p$ |
| $I_n$ | identity | $n\times n$ |
| $\operatorname{rank}(A)$ | number of pivots / dimension of column space | integer |

## Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{REF}$ | row echelon form |
| $\mathrm{RREF}$ | reduced row echelon form |
| pivot | first nonzero entry in a row of REF/RREF |
| $A^{-1}$ | inverse matrix (square, when it exists) |

## Conditions / Assumptions

- Matrix product $AB$ requires the number of columns of $A$ to equal the number of rows of $B$.
- $A$ is invertible if and only if $A$ is square and $\operatorname{rank}(A)=n$ (full pivots), equivalently $A\mathbf{x}=\mathbf{b}$ has a unique solution for every $\mathbf{b}$.
- Row reduction assumes exact arithmetic in theory; numerical practice needs pivoting strategies (see numerical methods notes).

## Matrix / Vector Form

**Identity and inverse** (for invertible $A\in\mathbb{R}^{n\times n}$):

$$
A A^{-1} = A^{-1} A = I_n.
$$

**Solving via inverse** (when $A$ is invertible): $\mathbf{x} = A^{-1}\mathbf{b}$. Prefer row reduction in hand computation.

**Rank**: $\operatorname{rank}(A)$ equals the number of pivot positions after row reduction, and equals the dimension of the column space (and of the row space).

## Procedure

Gaussian elimination to REF:

1. Find the leftmost nonzero column; swap a nonzero entry into the pivot row if needed.
2. Scale (optional) and eliminate entries below the pivot.
3. Repeat on the submatrix below and to the right of the pivot.
4. For RREF, eliminate above pivots and scale pivots to $1$.

To invert $A$, row-reduce $[A\mid I]$ to $[I\mid A^{-1}]$ when possible.

## Worked Example

$$
A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 0 \\ 3 & 6 & 1 \end{pmatrix}.
$$

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:

$$
\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & -2 \\ 0 & 0 & -2 \end{pmatrix}.
$$

$R_3 \leftarrow R_3 - R_2$, then scale $R_2$: pivots in columns 1 and 3, so $\operatorname{rank}(A)=2$. The middle column is a free-direction indicator for null-space structure when solving $A\mathbf{x}=\mathbf{b}$.

## Common Mistakes

- Multiplying matrices entrywise instead of using row–column products.
- Assuming $AB=BA$.
- Scaling a row by zero (destroys information; not an elementary operation).
- Calling $f(\mathbf{x})=A\mathbf{x}+\mathbf{b}$ linear when $\mathbf{b}\neq\mathbf{0}$.

## Connections

- Related: [[Systems of Linear Equations]], [[Determinants]], [[Vector Spaces and Bases]]
- Next: [[Determinants]] or [[Vector Spaces and Bases]]
- Numerical: LU factorization and elimination methods under [[Numerical Methods]]

## References

Matrix algebra and elimination follow MIT 18.06 (Strang).[^mit-matrices]

[^mit-matrices]: MIT OpenCourseWare, *18.06 Linear Algebra*, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
