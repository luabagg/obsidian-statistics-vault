---
dg-publish: true
aliases:
  - Gamma Distribution
  - Distribuição Gama
---

# Gamma Distribution

Compact study note.

## Summary

The gamma distribution models positive continuous quantities, especially sums of exponential waiting times. This note uses shape-scale parameters.[^nist-gallery]

## Prerequisites

- [[Função Gama|Gamma Function]]
- [[Distribuição Exponencial|Exponential Distribution]]

## Definition

$X\sim\operatorname{Gamma}(k,\theta)$ with shape $k$ and scale $\theta$.

## Notation and Assumptions

$k>0$ and $\theta>0$. The rate form uses $\lambda=1/\theta$ and must not be mixed with this scale form.

## Parameters

$k>0$; $\theta>0$.

## Support

$(0,\infty)$.

## PMF or PDF

$f_X(x)=x^{k-1}e^{-x/\theta}/(\Gamma(k)\theta^k)$ for $x>0$.

## CDF

The CDF uses the lower incomplete gamma function: $F_X(x)=\gamma(k,x/\theta)/\Gamma(k)$.

## Moments

$E[X]=k\theta$, $\operatorname{Var}(X)=k\theta^2$, and $M_X(t)=(1-\theta t)^{-k}$ for $t<1/\theta$.

## Essential Result

If $k$ is a positive integer, $X$ is the sum of $k$ IID exponential variables with common scale $\theta$.

## Small Example

For $k=3$ and $\theta=2$, $E[X]=6$ and $\operatorname{Var}(X)=12$.

## Common Mistakes

- Writing the MGF with the rate formula while calling the parameter a scale.
- Forgetting the support is positive.

## Connections

- [[Função Gama|Gamma Function]]
- [[Distribuição Exponencial|Exponential Distribution]]
- [[Distribuição Qui-Quadrado|Chi-Square Distribution]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
[^dlmf-gamma]: NIST Digital Library of Mathematical Functions, "Chapter 5: Gamma Function", https://dlmf.nist.gov/5
