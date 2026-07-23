---
dg-publish: true
dg-show-local-graph: true
tags:
  - linear-algebra
  - hub
aliases:
  - Linear Algebra
  - LA
---

%% Begin Waypoint %%
- **[[Linear Algebra]]**
	- [[Determinants]]
	- [[Eigenvalues and Eigenvectors]]
	- [[Least Squares and QR]]
	- [[Matrices and Row Reduction]]
	- [[Orthogonality and Projections]]
	- [[Systems of Linear Equations]]
	- [[Vector Spaces and Bases]]
%% End Waypoint %%

# Linear Algebra

## Summary

Linear algebra studies linear equations, matrices, vector spaces, and linear maps. It underpins least squares, spectral methods, numerical linear algebra, and much of statistics and machine learning.

## Prerequisites

[[Functions]]; coordinate geometry from [[Analytic Geometry]] (especially [[Vectors and Dot Product]]). Comfortable algebra with systems of equations.

## Learning order

1. [[Systems of Linear Equations]] — solution sets, geometry of intersections
2. [[Matrices and Row Reduction]] — matrix algebra, Gaussian elimination, rank
3. [[Determinants]] — volume scaling, invertibility test
4. [[Vector Spaces and Bases]] — span, independence, dimension, coordinates
5. [[Eigenvalues and Eigenvectors]] — spectral picture of square matrices
6. [[Orthogonality and Projections]] — orthonormal bases, projections
7. [[Least Squares and QR]] — inconsistent systems, QR factorization

## Key distinction

A map $f(\mathbf{x}) = A\mathbf{x}$ (matrix–vector product) is **linear**. An affine map $f(\mathbf{x}) = A\mathbf{x} + \mathbf{b}$ with $\mathbf{b}\neq\mathbf{0}$ is **not** linear, though it is affine.

## Next steps

- Numerical methods for systems: topics under [[Numerical Methods]] (e.g. Gaussian elimination notes in that tree when present)
- Analytic geometry support: [[Lines and Planes]], [[Vectors and Dot Product]]
- Applications: least squares links to regression and [[Least Squares]] when available

## Connections

- Foundations: [[Functions]] and [[Analytic Geometry]]
- Numerical methods: [[Numerical Methods]]
- Statistical applications: [[Probability]]

## References

Core linear algebra structure follows MIT OCW 18.06 and standard matrix-theory curricula.[^mit-1806][^openstax-calc3-la]

[^mit-1806]: MIT OpenCourseWare, *18.06 Linear Algebra* (Strang), https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
[^openstax-calc3-la]: OpenStax, *Calculus Volume 3* (vectors, matrices overview), https://openstax.org/details/books/calculus-volume-3
