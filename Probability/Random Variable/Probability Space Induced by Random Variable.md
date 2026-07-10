---
dg-publish: true
aliases:
  - Distribution Induced by a Random Variable
  - Pushforward Distribution
  - Espaço de Probabilidade Produzido por Variável Aleatória
---

# Distribution Induced by a Random Variable

Compact study note.

## Summary

One random variable transfers probability from the original sample space to the real line. The resulting pushforward measure is the distribution of the random variable.[^mit-prob]

## Prerequisites

- [[Random Variable|Random Variable]]
- [[Borel Sigma-Algebra|Borel Sigma-Algebra]]

## Notation and Assumptions

For $X:\Omega\to\mathbb{R}$, define $P_X(B)=P(X^{-1}(B))$ for every $B\in\mathcal{B}(\mathbb{R})$.

## Essential Result

The induced distribution is a probability measure on the real Borel space. For intervals,

$$P_X((l,u])=F_X(u)-F_X(l).$$

## Small Example

If $X$ counts heads in two fair flips, then $P_X(\{1\})=P(\{HT,TH\})=1/2$.

## Common Mistakes

- Confusing the original probability measure $P$ with the induced distribution $P_X$.
- Using $P_X(B)$ before checking $B$ is Borel.

## Connections

- [[Random Variable|Random Variable]]
- [[Cumulative Distribution Function|Cumulative Distribution Function]]
- [[Distributions|Distributions]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
