---
dg-publish: true
aliases:
  - IID Random Variables
  - Independent and Identically Distributed
  - Variaveis Aleatorias IID
---

# IID Random Variables

Compact study note.

## Summary

IID means random variables are independent and share the same distribution. This assumption powers sample means, laws of large numbers, and the central limit theorem.[^mit-prob]

## Prerequisites

- [[Independence|Independence]]
- [[Random Variable|Random Variable]]

## Notation and Assumptions

$X_1,\ldots,X_n$ are IID when they are mutually independent and each $X_i$ has the same distribution.

## Essential Result

For IID variables with finite mean $\mu$ and variance $\sigma^2$, $E[\bar X_n]=\mu$ and $\operatorname{Var}(\bar X_n)=\sigma^2/n$.

## Small Example

Repeated fair die rolls are IID if the die is rolled under identical conditions and previous rolls do not influence later rolls.

## Common Mistakes

- Checking identical distribution but forgetting independence.
- Assuming time-ordered data are IID without checking dependence or drift.

## Connections

- [[Law of Large Numbers|Law of Large Numbers]]
- [[Central Limit Theorem|Central Limit Theorem]]
- [[Binomial Distribution|Binomial Distribution]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
