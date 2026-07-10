---
dg-publish: true
tags:
  - numerical-methods
  - interpolation
  - hub
aliases:
  - Polynomial Interpolation
---

# Polynomial Interpolation

## Summary

Polynomial interpolation constructs a polynomial that passes through given data points. For distinct nodes, the polynomial of degree at most \(n\) through \(n+1\) points is unique.

## Prerequisites

[[Polynomials and Rational Functions]], [[Systems of Linear Equations]]

## Learning Order

1. [[Teorema de Existência e Unicidade do Polinômio de Interpolação]]
2. [[Interpolação Polinimial pela Definição]] (Vandermonde)
3. [[Polinômio de Lagrange]]
4. [[Polinômio de Newton]]

## Limitations

High-degree equispaced interpolation can oscillate (Runge phenomenon). Piecewise polynomials/splines are often preferable for large data sets (not covered in this hub’s child notes yet).

## Connections

- Contrast with approximate fitting: [[Ajuste de Curvas]]
- Hub: [[Métodos Numéricos]]

## References

Existence/uniqueness and classical forms are standard numerical analysis.[^dlmf-interp]

[^dlmf-interp]: NIST DLMF, *§3.3 Interpolation*, https://dlmf.nist.gov/3.3
