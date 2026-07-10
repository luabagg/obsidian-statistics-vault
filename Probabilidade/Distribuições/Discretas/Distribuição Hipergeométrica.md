---
dg-publish: true
aliases:
  - Hypergeometric Distribution
  - Distribuição Hipergeométrica
---

# Hypergeometric Distribution

Compact study note.

## Summary

The hypergeometric distribution counts successes in fixed-size samples drawn without replacement from finite populations.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória Discreta|Discrete Random Variable]]

## Definition

$X\sim\operatorname{Hypergeometric}(N,K,n)$ when one population of $N$ items has $K$ successes and $n$ items are sampled without replacement.

## Notation and Assumptions

Population size and number of successes are fixed. Sampling is without replacement.

## Parameters

$N\in\{1,2,\ldots\}$, $0\le K\le N$, and $0\le n\le N$.

## Support

$\max(0,n-(N-K))\le k\le\min(n,K)$.

## PMF or PDF

$P(X=k)=\frac{\binom Kk\binom{N-K}{n-k}}{\binom Nn}$ on the valid support.

## CDF

Usually evaluated by summing the PMF over valid integers.

## Moments

$E[X]=nK/N$ and $\operatorname{Var}(X)=n(K/N)(1-K/N)(N-n)/(N-1)$ for $N>1$.

## Essential Result

Hypergeometric is the without-replacement analogue of binomial sampling.

## Small Example

From 50 items with 20 successes, sample 10. Then $P(X=4)=\binom{20}{4}\binom{30}{6}/\binom{50}{10}$.

## Common Mistakes

- Using a binomial model when draws are without replacement and the population is not large.
- Allowing impossible $k$ values outside the support.

## Connections

- [[Distribuição Binomial|Binomial Distribution]]
- [[Probabilidade/Distribuições/Discretas/Distribuição Uniforme|Discrete Uniform Distribution]]
- [[Distribuições|Distributions]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
