---
dg-publish: true
aliases:
  - Binomial Distribution
  - Distribuição Binomial
---

# Binomial Distribution

Compact study note.

## Summary

The binomial distribution counts successes in a fixed number of independent Bernoulli trials with common success probability.[^openstax-discrete]

## Prerequisites

- [[Bernoulli Distribution|Bernoulli Distribution]]
- [[Newton Binomial|Binomial Theorem]]

## Definition

$X\sim\operatorname{Binomial}(n,p)$ when $X=\sum_{i=1}^{n}X_i$ for IID $X_i\sim\operatorname{Bernoulli}(p)$.

## Notation and Assumptions

Trials are independent, $n$ is fixed before observing data, and $p$ is constant across trials.

## Parameters

$n\in\{0,1,2,\ldots\}$ and $0\le p\le1$.

## Support

$\{0,1,\ldots,n\}$.

## PMF or PDF

$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ for $k=0,\ldots,n$.

## CDF

$F_X(k)=\sum_{j=0}^{\lfloor k\rfloor}\binom{n}{j}p^j(1-p)^{n-j}$.

## Moments

$E[X]=np$, $\operatorname{Var}(X)=np(1-p)$, and $M_X(t)=(1-p+pe^t)^n$.

## Essential Result

The binomial model fixes the number of trials and randomizes the number of successes.

## Small Example

For five fair coin flips, $P(X=3)=\binom53(0.5)^3(0.5)^2=0.3125$.

## Common Mistakes

- Using binomial sampling for draws without replacement from a small population.
- Forgetting the independence and constant-$p$ assumptions.

## Connections

- [[Bernoulli Distribution|Bernoulli Distribution]]
- [[Hypergeometric Distribution|Hypergeometric Distribution]]
- [[Negative Binomial Distribution|Negative Binomial Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
