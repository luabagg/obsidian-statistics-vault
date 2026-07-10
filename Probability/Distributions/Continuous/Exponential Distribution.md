---
dg-publish: true
aliases:
  - Exponential Distribution
  - Distribuição Exponencial
---

# Exponential Distribution

Compact study note.

## Summary

The exponential distribution models waiting time to the next event in one constant-rate Poisson process. It is right-skewed and memoryless, not symmetric.[^nist-gallery]

## Prerequisites

- [[Poisson Distribution|Poisson Distribution]]
- [[Continuous Random Variable|Continuous Random Variable]]

## Definition

$X\sim\operatorname{Exponential}(\lambda)$ uses the rate parameterization.

## Notation and Assumptions

$\lambda>0$ is a rate per unit of time or space. Support is nonnegative.

## Parameters

$\lambda>0$.

## Support

$[0,\infty)$.

## PMF or PDF

$f_X(x)=\lambda e^{-\lambda x}$ for $x\ge0$, and $0$ otherwise.

## CDF

$F_X(x)=1-e^{-\lambda x}$ for $x\ge0$.

## Moments

$E[X]=1/\lambda$, $\operatorname{Var}(X)=1/\lambda^2$, and $M_X(t)=\lambda/(\lambda-t)$ for $t<\lambda$.

## Essential Result

Memorylessness: $P(X>s+t\mid X>s)=P(X>t)$ for $s,t\ge0$.

## Small Example

If calls arrive at rate $2$ per minute, the chance of waiting more than one minute is $P(X>1)=e^{-2}$.

## Common Mistakes

- Mixing rate $\lambda$ with scale $\theta=1/\lambda$.
- Calling the exponential distribution symmetric.

## Connections

- [[Poisson Distribution|Poisson Distribution]]
- [[Gamma Distribution|Gamma Distribution]]
- [[Weibull Distribution|Weibull Distribution]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
