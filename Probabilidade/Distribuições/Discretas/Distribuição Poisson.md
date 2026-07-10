---
dg-publish: true
aliases:
  - Poisson Distribution
  - Distribuição Poisson
---

# Poisson Distribution

Compact study note.

## Summary

The Poisson distribution models counts of events in a fixed interval when events occur independently at one constant average rate.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória Discreta|Discrete Random Variable]]

## Definition

$X\sim\operatorname{Poisson}(\lambda)$ with rate parameter $\lambda$ equal to the expected count in the interval.

## Notation and Assumptions

The interval is fixed, the average rate is constant, and events do not cluster beyond the model's independence assumptions.

## Parameters

$\lambda>0$.

## Support

$\{0,1,2,\ldots\}$.

## PMF or PDF

$P(X=k)=e^{-\lambda}\lambda^k/k!$ for $k=0,1,2,\ldots$.

## CDF

$F_X(k)=\sum_{j=0}^{\lfloor k\rfloor}e^{-\lambda}\lambda^j/j!$.

## Moments

Moments and MGF:

$$E[X]=\lambda, \qquad \operatorname{Var}(X)=\lambda.$$

$$M_X(t)=\exp(\lambda(\exp(t)-1)).$$

## Essential Result

Poisson counts connect to exponential waiting times in a Poisson process.

## Small Example

If defects average $4$ per hour, $P(X=3)=e^{-4}4^3/3!\approx0.1954$.

## Common Mistakes

- Using Poisson when the rate changes across the interval.
- Forgetting that the variance equals the mean under the basic model.

## Connections

- [[Distribuição Exponencial|Exponential Distribution]]
- [[Distribuição Binomial|Binomial Distribution]]
- [[Distribuições|Distributions]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
