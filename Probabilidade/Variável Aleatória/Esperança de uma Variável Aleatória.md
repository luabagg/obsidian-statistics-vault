---
dg-publish: true
aliases:
  - Expected Value
  - Expectation
  - Esperança de uma Variável Aleatória
---

# Expected Value

Compact study note.

## Summary

Expected value is the probability-weighted average of a random variable when the required sum or integral is finite. It is linear even when variables are dependent.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória|Random Variable]]

## Notation and Assumptions

Discrete expectation:

$$E[X]=\sum_x xP(X=x).$$

Continuous expectation with density $f_X$:

$$E[X]=\int_{-\infty}^{\infty}x f_X(x)\,dx.$$

Use these formulas when the absolute sum or integral is finite.

## Essential Result

Linearity: $E[aX+bY+c]=aE[X]+bE[Y]+c$ whenever the expectations exist.

## Small Example

If $X$ counts heads in two fair flips, $E[X]=0(1/4)+1(1/2)+2(1/4)=1$.

## Common Mistakes

- Averaging possible values without probability weights.
- Assuming expectation exists for every distribution.

## Connections

- [[Variância de uma Variável Aleatória|Variance]]
- [[Funções Geradoras de Momento|Moment Generating Functions]]
- [[Distribuições|Distributions]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
