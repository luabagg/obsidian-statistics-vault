---
dg-publish: true
aliases:
  - Mixed Random Variable
  - Variavel Aleatoria Mista
  - Variável Aleatória Mista
---

# Mixed Random Variable

Compact study note.

## Summary

Mixed random variable has both point masses and continuous component. Its distribution is not described completely by only PMF or only PDF.[^mit-prob]

## Prerequisites

- [[Variável Aleatória|Random Variable]]
- [[Variável Aleatória Discreta|Discrete Random Variable]]
- [[Variável Aleatória Contínua|Continuous Random Variable]]

## Notation and Assumptions

A CDF $F_X$ is mixed when it has jumps at some points and continuous growth over intervals. Jump size at point $c$ equals $P(X=c)$.

## Essential Result

Compute probabilities by adding point masses and integrating the density over the continuous part.

## Small Example

Let $P(X=0)=0.3$ and, conditional on not being zero, $X$ be uniform on $(0,1)$ with weight $0.7$. Then $P(X\le0.5)=0.3+0.7(0.5)=0.65$.

## Common Mistakes

- Representing the continuous component with an impossible atom at infinity.
- Dropping the point mass when computing expectations.

## Connections

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Esperança de uma Variável Aleatória|Expected Value]]
- [[Densidade de Probabilidade|Probability Density Function]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
