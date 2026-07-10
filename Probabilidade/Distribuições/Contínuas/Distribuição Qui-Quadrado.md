---
dg-publish: true
aliases:
  - Chi-Square Distribution
  - Distribuição Qui-Quadrado
---

# Chi-Square Distribution

Compact study note.

## Summary

The chi-square distribution with $\nu$ degrees of freedom is the distribution of a sum of squared independent standard normal variables. It is right-skewed, especially for small $\nu$.[^nist-gallery]

## Prerequisites

- [[Distribuição Normal|Normal Distribution]]
- [[Distribuição Gama|Gamma Distribution]]

## Definition

If $Z_1,\ldots,Z_\nu$ are IID $N(0,1)$, then $X=\sum_{i=1}^{\nu}Z_i^2\sim\chi^2_\nu$.

## Notation and Assumptions

$\nu$ is a positive degree-of-freedom parameter.

## Parameters

$\nu>0$ in the gamma-family form; for the squared-normal construction, $\nu$ is a positive integer.

## Support

$[0,\infty)$.

## PMF or PDF

$f_X(x)=\frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2-1}e^{-x/2}$ for $x>0$.

## CDF

The CDF is the gamma CDF with shape $\nu/2$ and scale $2$.

## Moments

$E[X]=\nu$, $\operatorname{Var}(X)=2\nu$, and $M_X(t)=(1-2t)^{-\nu/2}$ for $t<1/2$.

## Essential Result

$\chi^2_\nu$ is $\operatorname{Gamma}(\nu/2,2)$ in shape-scale notation.

## Small Example

If $Z_1,Z_2,Z_3$ are independent standard normals, then $Z_1^2+Z_2^2+Z_3^2\sim\chi^2_3$.

## Common Mistakes

- Calling chi-square symmetric.
- Defining it through cubes or unsquared normal quantities.

## Connections

- [[Distribuição Normal|Normal Distribution]]
- [[Distribuição Gama|Gamma Distribution]]
- [[Distribuição F (Distribuição de Freira)|F Distribution]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
[^dlmf-gamma]: NIST Digital Library of Mathematical Functions, "Chapter 5: Gamma Function", https://dlmf.nist.gov/5
