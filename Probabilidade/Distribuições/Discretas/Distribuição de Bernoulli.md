---
dg-publish: true
aliases:
  - Bernoulli Distribution
  - Distribuição de Bernoulli
---

# Bernoulli Distribution

Compact study note.

## Summary

Bernoulli distribution models a success/failure trial coded with $1$ for success and $0$ for failure.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória Discreta|Discrete Random Variable]]

## Definition

$X\sim\operatorname{Bernoulli}(p)$ when $P(X=1)=p$ and $P(X=0)=1-p$.

## Notation and Assumptions

Use single trial only. For multiple independent Bernoulli trials, use binomial model.

## Parameters

$p$ is the success probability with $0\le p\le1$.

## Support

$\{0,1\}$.

## PMF or PDF

$P(X=x)=p^x(1-p)^{1-x}$ for $x\in\{0,1\}$.

## CDF

$F_X(x)=0$ for $x<0$, $1-p$ for $0\le x<1$, and $1$ for $x\ge1$.

## Moments

$E[X]=p$, $\operatorname{Var}(X)=p(1-p)$, and $M_X(t)=1-p+pe^t$.

## Essential Result

One Bernoulli variable is the building block for binomial, geometric, and negative binomial distributions.

## Small Example

For biased coin with $P(H)=0.7$, let $X=1$ for heads. Then

$$P(X=1)=0.7, \qquad E[X]=0.7, \qquad \operatorname{Var}(X)=0.21.$$

## Common Mistakes

- Using two coin flips as Bernoulli variable when $X$ counts heads.
- Writing the MGF as probability generating function without $\exp(t)$.

## Connections

- [[Distribuição Binomial|Binomial Distribution]]
- [[Distribuição Geométrica|Geometric Distribution]]
- [[Esperança a Partir da Função Geradora de Momentos|Expectation from an MGF]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
