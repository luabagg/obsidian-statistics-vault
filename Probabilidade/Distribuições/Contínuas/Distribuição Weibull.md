---
dg-publish: true
aliases:
  - Weibull Distribution
  - Distribuição Weibull
---

# Weibull Distribution

Compact study note.

## Summary

The Weibull distribution is a flexible positive distribution often used for lifetimes and reliability. Its shape parameter controls increasing, constant, or decreasing hazard behavior.[^nist-gallery]

## Prerequisites

- [[Variável Aleatória Contínua|Continuous Random Variable]]
- [[Função Gama|Gamma Function]]

## Definition

$X\sim\operatorname{Weibull}(k,\lambda)$ with shape $k$ and scale $\lambda$.

## Notation and Assumptions

$k>0$ and $\lambda>0$. This note uses $\lambda$ like scale, not rate.

## Parameters

$k>0$ and $\lambda>0$.

## Support

$[0,\infty)$.

## PMF or PDF

$f_X(x)=(k/\lambda)(x/\lambda)^{k-1}e^{-(x/\lambda)^k}$ for $x\ge0$.

## CDF

$F_X(x)=1-e^{-(x/\lambda)^k}$ for $x\ge0$.

## Moments

$E[X]=\lambda\Gamma(1+1/k)$ and $\operatorname{Var}(X)=\lambda^2[\Gamma(1+2/k)-\Gamma(1+1/k)^2]$.

## Essential Result

When $k=1$, Weibull$(1,\lambda)$ is exponential with rate $1/\lambda$.

## Small Example

If $k=1$ and $\lambda=5$, then $E[X]=5$, matching an exponential distribution with rate $0.2$.

## Common Mistakes

- Mixing Weibull scale with exponential rate.
- Assuming all Weibull models are memoryless; only $k=1$ is.

## Connections

- [[Distribuição Exponencial|Exponential Distribution]]
- [[Função Gama|Gamma Function]]
- [[Distribuição Gama|Gamma Distribution]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
[^dlmf-gamma]: NIST Digital Library of Mathematical Functions, "Chapter 5: Gamma Function", https://dlmf.nist.gov/5
