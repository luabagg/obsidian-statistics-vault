---
dg-publish: true
aliases:
  - Quantiles
  - Quantis
---

# Quantiles

Compact study note.

## Summary

Quantile means value cutting off chosen cumulative probability. Quantiles translate CDFs into thresholds and are used for medians, percentiles, and critical values.[^openstax-continuous]

## Prerequisites

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]

## Notation and Assumptions

For $0<p<1$, one $p$-quantile is any $q_p$ satisfying $F(q_p)\ge p$ and $P(X\ge q_p)\ge1-p$. For continuous strictly increasing CDFs, $q_p=F^{-1}(p)$.

## Essential Result

The median is any $0.5$-quantile.

## Small Example

For $X\sim\operatorname{Uniform}(0,10)$, $F(x)=x/10$ on $[0,10]$, so the $0.9$-quantile is $9$.

## Common Mistakes

- Assuming quantiles are unique for discrete distributions.
- Confusing a percentile rank $p$ with the value $q_p$.

## Connections

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Distribuição Normal|Normal Distribution]]
- [[Distribuição T-Student|Student's t Distribution]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
