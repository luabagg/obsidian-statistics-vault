---
dg-publish: true
dg-show-local-graph: true
tags:
  - numerical-methods
  - hub
aliases:
  - Numerical Methods
---

# Numerical Methods

## Summary

Numerical methods approximate mathematical problems that are hard or impossible to solve in closed form: roots, linear systems, interpolation, integrals, and data fitting.

## Prerequisites

[[Cálculo]], [[Álgebra Linear]], basic programming literacy for algorithms.

## Learning Order

1. [[Zeros de Funções]] — bracket and open root finders
2. [[Resolução de Sistemas Lineares]] — direct and iterative solvers
3. [[Interpolação Polinimial]] — Lagrange / Newton
4. Integration: [[Regra do Ponto Médio]], [[Regra dos Trapézios]], [[Regra de Simpson (um terço)]], [[Regra de Simpson (três oitavos)]]
5. [[Ajuste de Curvas]] / [[Mínimos Quadrados]]

## Design Principles

- State assumptions (continuity, smoothness, nonsingularity).
- Separate mathematical convergence guarantees from implementation heuristics.
- Always define a stopping criterion and an error measure.
- Prefer stable algorithms (pivoting, QR) when conditioning matters.

## Connections

- Theory: [[Cálculo]], [[Álgebra Linear]]
- Full path list: [[LEARNING_PATHS]]

## References

NIST DLMF Chapter 3 is a compact reference for numerical linear algebra, interpolation, and quadrature.[^dlmf3]

[^dlmf3]: NIST DLMF, *Chapter 3 Numerical Methods*, https://dlmf.nist.gov/3
