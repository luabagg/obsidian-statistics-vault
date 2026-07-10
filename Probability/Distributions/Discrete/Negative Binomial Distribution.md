---
dg-publish: true
aliases:
  - Negative Binomial Distribution
  - Distribuição Binomial Negativa
---

# Negative Binomial Distribution

Compact study note.

## Summary

The negative binomial distribution models the number of failures before a fixed number of successes in independent Bernoulli trials.[^openstax-discrete]

## Prerequisites

- [[Geometric Distribution|Geometric Distribution]]

## Definition

$X\sim\operatorname{NegBin}(r,p)$ here means $X$ counts failures before the $r$th success.

## Notation and Assumptions

Trials are independent, success probability is constant, and $r$ is fixed in advance.

## Parameters

$r\in\{1,2,\ldots\}$ and $0<p\le1$.

## Support

$\{0,1,2,\ldots\}$.

## PMF or PDF

$P(X=k)=\binom{k+r-1}{k}p^r(1-p)^k$ for $k=0,1,2,\ldots$.

## CDF

Usually evaluated by summing the PMF; closed forms use special functions.

## Moments

$E[X]=r(1-p)/p$ and $\operatorname{Var}(X)=r(1-p)/p^2$.

## Essential Result

For $r=1$, this is the failure-count version of the geometric distribution.

## Small Example

For $r=3$, $p=0.5$, $P(X=2)=\binom42(0.5)^3(0.5)^2=6/32=0.1875$.

## Common Mistakes

- Not stating whether $X$ counts failures or total trials.
- Replacing 'fixed successes' with 'fixed trials', which is binomial.

## Connections

- [[Geometric Distribution|Geometric Distribution]]
- [[Binomial Distribution|Binomial Distribution]]
- [[Bernoulli Distribution|Bernoulli Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
