---
dg-publish: true
aliases:
  - F Distribution
  - Fisher-Snedecor F Distribution
  - Distribuição F
---

# F Distribution (Fisher-Snedecor)

Compact study note.

## Summary

The F distribution is the distribution of a ratio of two independent chi-square variables divided by their degrees of freedom. The name refers to Fisher and Snedecor; the old path title is retained only for link stability.[^nist-gallery]

## Prerequisites

- [[Chi-Square Distribution|Chi-Square Distribution]]

## Definition

If $U\sim\chi^2_{d_1}$, $V\sim\chi^2_{d_2}$, and $U,V$ are independent, then $X=(U/d_1)/(V/d_2)\sim F_{d_1,d_2}$.

## Notation and Assumptions

$d_1$ and $d_2$ are numerator and denominator degrees of freedom.

## Parameters

$d_1>0$ and $d_2>0$.

## Support

$(0,\infty)$.

## PMF or PDF

$f_X(x)=\frac{(d_1/d_2)^{d_1/2}x^{d_1/2-1}}{B(d_1/2,d_2/2)(1+d_1x/d_2)^{(d_1+d_2)/2}}$ for $x>0$.

## CDF

The CDF is computed through the regularized beta function.

## Moments

$E[X]=d_2/(d_2-2)$ for $d_2>2$; $\operatorname{Var}(X)=\frac{2d_2^2(d_1+d_2-2)}{d_1(d_2-2)^2(d_2-4)}$ for $d_2>4$.

## Essential Result

The F distribution is right-skewed and has no finite upper endpoint.

## Small Example

If $U\sim\chi^2_5$ and $V\sim\chi^2_{10}$ are independent, then $(U/5)/(V/10)\sim F_{5,10}$.

## Common Mistakes

- Calling the distribution symmetric or bounded above.
- Describing chi-square variables like cubes of normals instead of sums of squared standard normals.

## Connections

- [[Chi-Square Distribution|Chi-Square Distribution]]
- [[Student t Distribution|Student's t Distribution]]
- [[Gamma Function|Gamma Function]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
[^dlmf-beta]: NIST Digital Library of Mathematical Functions, "5.12 Beta Function", https://dlmf.nist.gov/5.12
