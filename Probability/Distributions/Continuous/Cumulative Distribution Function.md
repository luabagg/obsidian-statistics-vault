---
dg-publish: true
aliases:
  - Cumulative Distribution Function
  - CDF
  - Função de Distribuição Acumulada
---

# Cumulative Distribution Function

Compact study note.

## Summary

The cumulative distribution function gives probability that random variable values are at or below chosen thresholds. Every real-valued random variable has a CDF.[^openstax-continuous]

## Prerequisites

- [[Random Variable|Random Variable]]

## Notation and Assumptions

$F_X(x)=P(X\le x)$ for all real $x$. CDFs are nondecreasing, right-continuous, and have limits $0$ at $-\infty$ and $1$ at $+\infty$.

## Essential Result

For continuous variables, interval probability is CDF difference:

$$P(l<X\le u)=F_X(u)-F_X(l).$$

For discrete variables, jump sizes give point probabilities.

## Small Example

If $X$ is uniform on $[0,1]$, then $F_X(0.3)=0.3$.

## Common Mistakes

- Assuming every CDF is continuous; discrete CDFs jump.
- Using $F_X(b)-F_X(a)$ with wrong endpoint conventions for atoms.

## Connections

- [[Quantiles|Quantiles]]
- [[Probability Density|Probability Density Function]]
- [[Discrete Random Variable|Discrete Random Variable]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
