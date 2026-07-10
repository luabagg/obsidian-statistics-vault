---
dg-publish: true
aliases:
  - Functions of Random Variables
  - Funções de Variáveis Aleatórias
---

# Functions of Random Variables

Compact study note.

## Summary

Applying one measurable function to a random variable creates another random variable. Its distribution is found by pushing probability through the transformation.[^mit-prob]

## Prerequisites

- [[Variável Aleatória|Random Variable]]
- [[Espaço de Probabilidade Produzido por Variável Aleatória|Distribution Induced by a Random Variable]]

## Notation and Assumptions

If $Y=g(X)$ and $g$ is Borel-measurable, then $Y$ is a random variable and $P(Y\in B)=P(X\in g^{-1}(B))$.

## Essential Result

For an injective differentiable transform $Y=g(X)$ with inverse $x=g^{-1}(y)$, $f_Y(y)=f_X(x)|dx/dy|$ on the transformed support.

## Small Example

If $X\sim\operatorname{Uniform}(0,1)$ and $Y=X^2$, then $F_Y(y)=P(X\le\sqrt{y})=\sqrt{y}$ for $0\le y\le1$.

## Common Mistakes

- Forgetting to transform the support.
- Applying the derivative formula to non-injective transformations without splitting branches.

## Connections

- [[Função de Distribuição Acumulada|Cumulative Distribution Function]]
- [[Densidade de Probabilidade|Probability Density Function]]
- [[Distribuição Log-Normal|Log-Normal Distribution]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
