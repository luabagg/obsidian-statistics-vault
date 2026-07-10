---
dg-publish: true
aliases:
  - Random Variable
  - Variavel Aleatoria
  - Variável Aleatória
---

# Random Variable

Compact study note.

## Summary

One random variable is a measurable function from outcomes to numerical values. Measurability is what makes events including $\{X\le x\}$ legitimate probability events.[^mit-prob]

## Prerequisites

- [[Probability Space|Probability Space]]
- [[Borel Sigma-Algebra|Borel Sigma-Algebra]]

## Notation and Assumptions

One real-valued random variable is a function $X:\Omega\to\mathbb{R}$ such that $X^{-1}(B)\in\mathcal{F}$ for every $B\in\mathcal{B}(\mathbb{R})$.

## Essential Result

The CDF $F_X(x)=P(X\le x)$ determines the distribution of one real-valued random variable.

## Small Example

For two coin flips, $X=$ number of heads maps $HH\mapsto2$, $HT\mapsto1$, $TH\mapsto1$, $TT\mapsto0$.

## Common Mistakes

- Thinking a random variable is random in its formula; the input outcome is uncertain.
- Ignoring measurability when moving beyond finite spaces.

## Connections

- [[Discrete Random Variable|Discrete Random Variable]]
- [[Continuous Random Variable|Continuous Random Variable]]
- [[Mixed Random Variable|Mixed Random Variable]]
- [[Probability Space Induced by Random Variable|Distribution Induced by a Random Variable]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
