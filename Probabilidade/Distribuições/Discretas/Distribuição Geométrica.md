---
dg-publish: true
aliases:
  - Geometric Distribution
  - Distribuição Geométrica
---

# Geometric Distribution

Compact study note.

## Summary

The geometric distribution models the trial number of the first success in independent Bernoulli trials.[^openstax-discrete]

## Prerequisites

- [[Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Independência|Independence]]

## Definition

$X\sim\operatorname{Geometric}(p)$ here means $X$ counts trials until the first success.

## Notation and Assumptions

Trials are independent and each has success probability $p$.

## Parameters

$0<p\le1$.

## Support

$\{1,2,3,\ldots\}$.

## PMF or PDF

$P(X=k)=(1-p)^{k-1}p$ for $k=1,2,\ldots$.

## CDF

$F_X(k)=1-(1-p)^{\lfloor k\rfloor}$ for $k\ge1$.

## Moments

Moments and MGF:

$$E[X]=1/p, \qquad \operatorname{Var}(X)=(1-p)/p^2.$$

$$M_X(t)=\frac{p\exp(t)}{1-(1-p)\exp(t)}, \qquad t<-\log(1-p).$$

## Essential Result

The geometric distribution is memoryless: $P(X>m+n\mid X>m)=P(X>n)$.

## Small Example

With $p=0.25$, $P(X=3)=(0.75)^2(0.25)=0.140625$.

## Common Mistakes

- Mixing the trial-count version with the failure-count version.
- Using memorylessness for non-geometric waiting models.

## Connections

- [[Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Distribuição Binomial Negativa|Negative Binomial Distribution]]
- [[Distribuição Exponencial|Exponential Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
