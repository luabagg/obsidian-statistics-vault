---
dg-publish: true
aliases:
  - Normal Distribution
  - Gaussian Distribution
  - Distribuição Normal
---

# Normal Distribution

Compact study note.

## Summary

The normal distribution is a symmetric continuous distribution central to measurement error, approximation theory, and the central limit theorem.[^openstax-normal]

## Prerequisites

- [[Variável Aleatória Contínua|Continuous Random Variable]]

## Definition

$X\sim N(\mu,\sigma^2)$ with mean parameter $\mu$ and variance parameter $\sigma^2$.

## Notation and Assumptions

$\sigma>0$. The standard normal is $Z\sim N(0,1)$.

## Parameters

$\mu\in\mathbb{R}$ and $\sigma>0$.

## Support

$\mathbb{R}$.

## PMF or PDF

$f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp[-(x-\mu)^2/(2\sigma^2)]$.

## CDF

$F_X(x)=\Phi((x-\mu)/\sigma)$, where $\Phi$ is the standard normal CDF.

## Moments

$E[X]=\mu$, $\operatorname{Var}(X)=\sigma^2$, and $M_X(t)=\exp(\mu t+\sigma^2t^2/2)$.

## Essential Result

Standardization converts $X$ to $Z=(X-\mu)/\sigma\sim N(0,1)$.

## Small Example

If $X\sim N(70,15^2)$, then $P(X\le85)=\Phi(1)\approx0.8413$.

## Common Mistakes

- Writing $N(\mu,\sigma)$ when the convention is $N(\mu,\sigma^2)$ without saying so.
- Using normal approximations without checking scale and support.

## Connections

- [[Teorema Central do Limite|Central Limit Theorem]]
- [[Distribuição Log-Normal|Log-Normal Distribution]]
- [[Distribuição Qui-Quadrado|Chi-Square Distribution]]

## References

[^openstax-normal]: OpenStax, *Introductory Statistics 2e*, "Chapter 6: The Normal Distribution", https://openstax.org/books/introductory-statistics-2e/pages/6-introduction
[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
