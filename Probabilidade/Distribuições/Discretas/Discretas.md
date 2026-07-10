---
dg-publish: true
aliases:
  - Discrete Distributions
  - Discretas
---

# Discrete Distributions

Compact study note.

## Summary

Discrete distributions assign probability mass to finite or countably infinite support points. They model counts, categories encoded as numbers, and repeated Bernoulli-trial mechanisms.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória Discreta|Discrete Random Variable]]

## Notation and Assumptions

Use $p_X(x)=P(X=x)$ and require $\sum_xp_X(x)=1$ over the support.

## Essential Result

Match the sampling mechanism: Bernoulli for single success/failure trial, binomial for fixed independent trials, geometric for waiting to first success, and Poisson for event counts at fixed rate.

## Small Example

One fair die has a discrete uniform distribution over $\{1,2,3,4,5,6\}$.

## Common Mistakes

- Using a continuous density for count data.
- Leaving support implicit.

## Connections

- [[Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Distribuição Binomial|Binomial Distribution]]
- [[Distribuição Poisson|Poisson Distribution]]
- [[Probabilidade/Distribuições/Discretas/Distribuição Uniforme|Discrete Uniform Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
