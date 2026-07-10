---
dg-publish: true
aliases:
  - Borel Sigma-Algebra
  - Borel sigma algebra
  - Sigma-Álgebra de Borel
---

# Borel Sigma-Algebra

Compact study note.

## Summary

The Borel sigma-algebra on the real line is the smallest sigma-algebra containing all open subsets of $\mathbb{R}$. It is the standard measurable-event structure for real-valued random variables.[^mit-prob]

## Prerequisites

- [[Sigma-Álgebra|Sigma-Algebra]]

## Notation and Assumptions

$\mathcal{B}(\mathbb{R})=\sigma(\{G\subseteq\mathbb{R}:G\text{ is open}\})$. It also contains closed intervals, half-open intervals, countable sets including $\mathbb{Q}$, and the set of irrational numbers $\mathbb{R}\setminus\mathbb{Q}$.

## Essential Result

One real-valued random variable $X$ is measurable when $X^{-1}(B)\in\mathcal{F}$ for every $B\in\mathcal{B}(\mathbb{R})$. Not every Borel set is simply 'closed minus open'; the correct definition is generation by open sets.

## Small Example

Closed intervals are Borel. For example,

$$[l,u]=\mathbb{R}\setminus((-\infty,l)\cup(u,\infty)).$$

## Common Mistakes

- Claiming every Borel set has one simple closed-minus-open form.
- Using nonstandard phrases including 'irrational line' instead of 'set of irrational numbers'.

## Connections

- [[Sigma-Álgebra|Sigma-Algebra]]
- [[Variável Aleatória|Random Variable]]
- [[Espaço de Probabilidade Produzido por Variável Aleatória|Distribution Induced by a Random Variable]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
