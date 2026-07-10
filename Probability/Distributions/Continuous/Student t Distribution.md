---
dg-publish: true
aliases:
  - Student's t Distribution
  - Student t Distribution
  - Distribuição T-Student
---

# Student's t Distribution

Compact study note.

## Summary

Student's t distribution is a continuous distribution with heavier tails than the standard normal. Its single parameter is degrees of freedom.[^nist-gallery]

## Prerequisites

- [[Normal Distribution|Normal Distribution]]
- [[Chi-Square Distribution|Chi-Square Distribution]]

## Definition

If $Z\sim N(0,1)$, $V\sim\chi^2_\nu$, and $Z$ is independent of $V$, then $T=Z/\sqrt{V/\nu}\sim t_\nu$.

## Notation and Assumptions

$\nu>0$ controls tail thickness. Larger $\nu$ makes the distribution closer to $N(0,1)$.

## Parameters

$\nu>0$.

## Support

$\mathbb{R}$.

## PMF or PDF

$f_T(t)=\frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\Gamma(\nu/2)}\left(1+t^2/\nu\right)^{-(\nu+1)/2}$.

## CDF

No elementary closed-form CDF; it is evaluated numerically.

## Moments

$E[T]=0$ for $\nu>1$; $\operatorname{Var}(T)=\nu/(\nu-2)$ for $\nu>2$. The ordinary MGF does not exist for nonzero $t$.

## Essential Result

The one-sample t statistic has one $t_{n-1}$ distribution under normal sampling with unknown variance.

## Small Example

With $n=10$ normal observations and unknown variance, the usual one-sample statistic uses $\nu=9$ degrees of freedom.

## Common Mistakes

- Defining the distribution only through test-statistic usage.
- Listing two parameters when standard Student's t has one degree-of-freedom parameter.

## Connections

- [[Normal Distribution|Normal Distribution]]
- [[Chi-Square Distribution|Chi-Square Distribution]]
- [[F Distribution|F Distribution]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
[^dlmf-gamma]: NIST Digital Library of Mathematical Functions, "Chapter 5: Gamma Function", https://dlmf.nist.gov/5
