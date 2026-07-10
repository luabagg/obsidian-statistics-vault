---
dg-publish: true
aliases:
  - Gamma Function
  - Função Gama
---

# Gamma Function

Compact study note.

## Summary

The gamma function extends factorials from positive integers to positive real and complex arguments. It normalizes gamma, chi-square, t, and F densities.[^dlmf-gamma]

## Prerequisites

- Prerequisites: None

## Notation and Assumptions

For $x>0$, $\Gamma(x)=\int_0^{\infty}t^{x-1}e^{-t}\,dt$.

## Essential Result

$\Gamma(x+1)=x\Gamma(x)$ and $\Gamma(n)=(n-1)!$ for positive integers $n$.

## Small Example

$\Gamma(3)=2\Gamma(2)=2\cdot1\Gamma(1)=2!$.

## Common Mistakes

- Using $\Gamma(n)=n!$ instead of $\Gamma(n)=(n-1)!$ for positive integers.
- Forgetting that distribution formulas often require positive shape parameters.

## Connections

- [[Distribuição Gama|Gamma Distribution]]
- [[Distribuição Qui-Quadrado|Chi-Square Distribution]]
- [[Distribuição T-Student|Student's t Distribution]]

## References

[^dlmf-gamma]: NIST Digital Library of Mathematical Functions, "Chapter 5: Gamma Function", https://dlmf.nist.gov/5
