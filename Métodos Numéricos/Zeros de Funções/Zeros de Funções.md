---
dg-publish: true
dg-show-local-graph: true
tags:
  - numerical-methods
  - roots
  - hub
aliases:
  - Roots of Functions
---

# Roots of Functions

## Summary

Root-finding algorithms approximate solutions of \(f(x)=0\). Bracket methods need a sign change; open methods need a good initial guess and often a derivative.

## Prerequisites

[[Limites]], [[Derivadas]], continuity concepts.

## Learning Order

1. [[Teorema De Bolzano]] / [[Método Gráfico]] — existence and rough location
2. [[Método da Bisseção]] — guaranteed linear convergence on a bracket
3. [[Método da Falsa Posição]] — bracket with secant-like updates
4. [[Método das Secantes]] — derivative-free open method
5. [[Método de Newton-Raphson]] — locally quadratic for simple roots

## Comparison Snapshot

| Method | Needs | Speed | Guarantee |
|---|---|---|---|
| Bisection | sign change | slow | yes on bracket |
| False position | sign change | often faster than bisection | stays bracketed |
| Secant | two starts | superlinear typical | local |
| Newton | \(f'\) and one start | quadratic near simple root | local |

## Connections

- Hub: [[Métodos Numéricos]]
- Optimization uses roots of derivatives: [[Valores de Máximo e Mínimo]]

## References

Root-finding methods are classical numerical analysis.[^dlmf3]

[^dlmf3]: NIST DLMF, *Chapter 3 Numerical Methods*, https://dlmf.nist.gov/3
