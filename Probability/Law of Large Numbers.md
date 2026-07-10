---
dg-publish: true
aliases:
  - Law of Large Numbers
  - LLN
  - Lei dos Grandes Números
---

# Law of Large Numbers

Compact study note.

## Summary

The law of large numbers says sample averages stabilize near the population mean under standard independence and finite-mean assumptions.[^mit-prob]

## Prerequisites

- [[IID Random Variables|IID Random Variables]]
- [[Expectation of a Random Variable|Expected Value]]

## Notation and Assumptions

For IID $X_1,X_2,\ldots$ with $E[X_i]=\mu$ and finite variance, the sample mean $\bar X_n=n^{-1}\sum_{i=1}^nX_i$ converges to $\mu$ in probability.

## Essential Result

For every $\varepsilon>0$, $P(|\bar X_n-\mu|>\varepsilon)\to0$ like $n\to\infty$.

## Small Example

The average number of heads per flip in many independent fair coin flips tends toward $0.5$.

## Common Mistakes

- Reading the theorem as guaranteeing short-sample accuracy.
- Thinking convergence removes all randomness at finite $n$.

## Connections

- [[IID Random Variables|IID Random Variables]]
- [[Central Limit Theorem|Central Limit Theorem]]
- [[Bernoulli Distribution|Bernoulli Distribution]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
