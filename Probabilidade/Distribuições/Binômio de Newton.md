---
dg-publish: true
aliases:
  - Binomial Theorem
  - Binômio de Newton
---

# Binomial Theorem

Compact study note.

## Summary

The binomial theorem expands powers of a sum and supplies the combinatorial coefficients used in the binomial distribution.[^openstax-discrete]

## Prerequisites

- Prerequisites: None

## Notation and Assumptions

For integer $n\ge0$, $\binom{n}{k}=n!/[k!(n-k)!]$ counts $k$-subsets of an $n$-element set.

## Essential Result

Expansion formula:

$$(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k.$$

## Small Example

$(x+y)^3=x^3+3x^2y+3xy^2+y^3$.

## Common Mistakes

- Using the theorem for noninteger exponents without the infinite-series version.
- Forgetting that $k$ runs from $0$ to $n$.

## Connections

- [[Distribuição Binomial|Binomial Distribution]]
- [[Distribuição Binomial Negativa|Negative Binomial Distribution]]
- [[Distribuições|Distributions]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
