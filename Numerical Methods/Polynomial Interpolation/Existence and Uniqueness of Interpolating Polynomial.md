---
dg-publish: true
tags:
  - numerical-methods
  - interpolation
aliases:
  - Uniqueness of Interpolating Polynomial
---

# Existence and Uniqueness of the Interpolating Polynomial

## Summary

Through \(n+1\) points with distinct abscissae there exists exactly one polynomial of degree at most \(n\) that interpolates them.

## Prerequisites

[[Polynomials and Rational Functions]]

## Statement

Let \((x_0,y_0),\ldots,(x_n,y_n)\) with \(x_i\neq x_j\) for \(i\neq j\). There exists a unique \(P\in\mathbb{R}[x]\) with \(\deg P\le n\) such that \(P(x_i)=y_i\) for all \(i\).

## Proof Sketch

**Uniqueness.** If \(P\) and \(Q\) both interpolate, then \(R=P-Q\) has degree \(\le n\) and \(n+1\) roots, so \(R\equiv 0\).

**Existence.** The Lagrange formula

\[
P(x)=\sum_{i=0}^n y_i\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}
\]

is a polynomial of degree \(\le n\) that hits every node.

## Connections

- Constructions: [[Lagrange Polynomial]], [[Newton Polynomial]]

## References

This theorem is foundational numerical analysis.[^dlmf-interp]

[^dlmf-interp]: NIST DLMF, *§3.3 Interpolation*, https://dlmf.nist.gov/3.3
