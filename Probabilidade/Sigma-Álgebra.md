---
dg-publish: true
aliases:
  - Sigma-Algebra
  - Sigma Algebra
  - Sigma-Álgebra
---

# Sigma-Algebra

Compact study note.

## Summary

One sigma-algebra is the collection of events on which a probability measure is allowed to operate. It is closed under complements and countable unions, so probability rules remain stable under repeated event operations.[^mit-prob]

## Prerequisites

- [[Espaço Amostral e Eventos|Sample Space and Events]]

## Notation and Assumptions

Collection $\mathcal{F}\subseteq\mathcal{P}(\Omega)$ is sigma-algebra when it contains $\Omega$, is closed under complements, and is closed under countable unions:

$$A_1,A_2,\ldots\in\mathcal{F} \implies \bigcup_{n=1}^{\infty}A_n\in\mathcal{F}.$$

## Essential Result

One correct finite example is $\mathcal{F}=\mathcal{P}(\{1,2,3\})$. On $[0,1]$, the collection of all intervals is not one sigma-algebra because countable unions of intervals need not be intervals.

## Small Example

With $\Omega=\{H,T\}$, $\mathcal{F}=\{\emptyset,\{H\},\{T\},\Omega\}$ is a sigma-algebra. Complements and countable unions stay inside the same collection.

## Common Mistakes

- Saying 'all intervals' form one sigma-algebra.
- Forgetting countable closure; finite closure alone defines only an algebra of sets.

## Connections

- [[Sigma-Álgebra De Borel|Borel Sigma-Algebra]]
- [[Espaço de Probabilidade|Probability Space]]
- [[Variável Aleatória|Random Variable]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
