---
dg-publish: true
aliases:
  - Central Limit Theorem
  - CLT
  - Teorema Central do Limite
---

# Central Limit Theorem

Compact study note.

## Summary

The central limit theorem explains why normalized sums and averages are often approximately normal, even when individual observations are not normal.[^mit-prob]

## Prerequisites

- [[Variáveis Aleatórias IID|IID Random Variables]]
- [[Distribuição Normal|Normal Distribution]]

## Notation and Assumptions

For IID $X_i$ with mean $\mu$ and variance $0<\sigma^2<\infty$, $\frac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n}$ converges in distribution to $N(0,1)$.

## Essential Result

Equivalently, $\bar X_n$ is approximately $N(\mu,\sigma^2/n)$ for large $n$ under the theorem assumptions.

## Small Example

For many independent Bernoulli trials with success probability $p$, the sample proportion is approximately normal with mean $p$ and variance $p(1-p)/n$ when $n$ is large enough.

## Common Mistakes

- Applying the CLT to strongly dependent data without justification.
- Forgetting that the approximation is about normalized sums, not raw observations.

## Connections

- [[Lei dos Grandes Números|Law of Large Numbers]]
- [[Distribuição Normal|Normal Distribution]]
- [[Função Característica|Characteristic Function]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
