---
dg-publish: true
aliases:
  - Discrete Random Variable
  - Variavel Aleatoria Discreta
  - Variável Aleatória Discreta
---

# Discrete Random Variable

Compact study note.

## Summary

One discrete random variable has countable support and is described by a probability mass function. Its CDF is one step function with jumps at support points.[^openstax-discrete]

## Prerequisites

- [[Variável Aleatória|Random Variable]]

## Notation and Assumptions

Use $p_X(x)=P(X=x)$ for the PMF. The support $S$ is finite or countably infinite, and $\sum_{x\in S}p_X(x)=1$.

## Essential Result

For any Borel set $C\subseteq\mathbb{R}$,

$$P(X\in C)=\sum_{x\in C\cap S}p_X(x).$$

## Small Example

If $X$ counts heads in two fair flips, $p_X(0)=1/4$, $p_X(1)=1/2$, and $p_X(2)=1/4$.

## Common Mistakes

- Calling a PMF one density.
- Forgetting that probabilities over the support must sum to one.

## Connections

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Distribuição Binomial|Binomial Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
