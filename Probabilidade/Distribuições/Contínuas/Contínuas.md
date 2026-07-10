---
dg-publish: true
aliases:
  - Continuous Distributions
  - Contínuas
---

# Continuous Distributions

Compact study note.

## Summary

Continuous distributions assign probability through areas under density curves. They model measurements, waiting times, positive quantities, and sampling distributions.[^openstax-continuous]

## Prerequisites

- [[Variável Aleatória Contínua|Continuous Random Variable]]

## Notation and Assumptions

Use $f_X(x)$ for PDF and $F_X(x)$ for CDF. Total density must satisfy

$$\int_{-\infty}^{\infty}f_X(x)\,dx=1.$$

## Essential Result

Support and parameterization are part of the definition; the same distribution name can have rate or scale forms.

## Small Example

An exponential waiting time with rate $\lambda$ has support $[0,\infty)$ and density $\lambda e^{-\lambda x}$.

## Common Mistakes

- Treating density height like probability.
- Forgetting support restrictions including $x>0$ for gamma, log-normal, chi-square, and F distributions.

## Connections

- [[Densidade de Probabilidade|Probability Density Function]]
- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Distribuição Normal|Normal Distribution]]
- [[Distribuição Exponencial|Exponential Distribution]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
