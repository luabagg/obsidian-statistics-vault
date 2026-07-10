---
dg-publish: true
aliases:
  - Probability Density Function
  - PDF
  - Densidade de Probabilidade
---

# Probability Density Function

Compact study note.

## Summary

One probability density function describes how probability is distributed across a continuum. Probabilities are integrals of the density over intervals.[^openstax-continuous]

## Prerequisites

- [[Variável Aleatória Contínua|Continuous Random Variable]]

## Notation and Assumptions

Density assumptions:

$$f_X(x)\ge0, \qquad \int_{-\infty}^{\infty}f_X(x)\,dx=1.$$

For measurable event set $C$,

$$P(X\in C)=\int_C f_X(x)\,dx.$$

## Essential Result

Density values may exceed $1$; only integrated area is probability.

## Small Example

For $X\sim\operatorname{Uniform}(0,0.5)$, $f_X(x)=2$ on $(0,0.5)$, but $P(0<X<0.25)=2(0.25)=0.5$.

## Common Mistakes

- Calling $f_X(3)$ the probability that $X=3$.
- Forgetting to verify total area equals one.

## Connections

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Variável Aleatória Contínua|Continuous Random Variable]]
- [[Distribuição Uniforme|Continuous Uniform Distribution]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
