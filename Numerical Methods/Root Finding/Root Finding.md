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

[[Limits]], [[Derivatives]], continuity concepts.

## Learning Order

1. [[Bolzano's Theorem]] / [[Graphical Method]] — existence and rough location
2. [[Bisection Method]] — guaranteed linear convergence on a bracket
3. [[False Position Method]] — bracket with secant-like updates
4. [[Secant Method]] — derivative-free open method
5. [[Newton-Raphson Method]] — locally quadratic for simple roots

## Comparison Snapshot

| Method | Needs | Speed | Guarantee |
|---|---|---|---|
| Bisection | sign change | slow | yes on bracket |
| False position | sign change | often faster than bisection | stays bracketed |
| Secant | two starts | superlinear typical | local |
| Newton | \(f'\) and one start | quadratic near simple root | local |

## Connections

- Hub: [[Numerical Methods]]
- Optimization uses roots of derivatives: [[Maxima and Minima]]

## References

Root-finding methods are classical numerical analysis.[^dlmf3]

[^dlmf3]: NIST DLMF, *Chapter 3 Numerical Methods*, https://dlmf.nist.gov/3
