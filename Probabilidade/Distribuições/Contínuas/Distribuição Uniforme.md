---
dg-publish: true
aliases:
  - Continuous Uniform Distribution
  - Distribuição Uniforme Contínua
---

# Continuous Uniform Distribution

Compact study note.

## Summary

The continuous uniform distribution gives constant density over a finite interval. It models an ideal measurement equally likely across that interval.[^openstax-continuous]

## Prerequisites

- [[Variável Aleatória Contínua|Continuous Random Variable]]

## Definition

Distribution notation:

$$X\sim\operatorname{Uniform}(l,u), \qquad l<u.$$

## Notation and Assumptions

Every subinterval probability is proportional to its length.

## Parameters

$$l,u\in\mathbb{R}, \qquad l<u.$$

## Support

$[a,b]$; endpoint choice does not change probabilities.

## PMF or PDF

$$f_X(x)=1/(u-l), \qquad l\le x\le u,$$

and $0$ otherwise.

## CDF

$$F_X(x)=0, \quad x<l.$$

$$F_X(x)=\frac{x-l}{u-l}, \quad l\le x\le u.$$

$$F_X(x)=1, \quad x>u.$$

## Moments

$$E[X]=(l+u)/2.$$

$$\operatorname{Var}(X)=(u-l)^2/12.$$

$$M_X(t)=\frac{\exp(tu)-\exp(tl)}{t(u-l)}, \qquad t\ne0.$$

## Essential Result

Probabilities are interval lengths divided by total length.

## Small Example

If $X\sim\operatorname{Uniform}(0,30)$, then $P(5<X<15)=10/30=1/3$.

## Common Mistakes

- Saying each individual real value is equally probable with positive probability.
- Forgetting the density changes when interval length changes.

## Connections

- [[Densidade de Probabilidade|Probability Density Function]]
- [[Quantis|Quantiles]]
- [[Probabilidade/Distribuições/Discretas/Distribuição Uniforme|Discrete Uniform Distribution]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
