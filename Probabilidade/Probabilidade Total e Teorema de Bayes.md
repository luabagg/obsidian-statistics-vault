---
dg-publish: true
aliases:
  - Total Probability and Bayes Theorem
  - Bayes' Theorem
  - Probabilidade Total e Teorema de Bayes
---

# Total Probability and Bayes' Theorem

Compact study note.

## Summary

The law of total probability decomposes events across partitions. Bayes' theorem reverses conditional probability by combining likelihood with prior probabilities.[^openstax-prob]

## Prerequisites

- [[Probabilidade Condicional|Conditional Probability]]

## Notation and Assumptions

Let $B_1,\ldots,B_n$ be disjoint events with positive probability and union $\Omega$. Then

$$P(A)=\sum_i P(A\mid B_i)P(B_i).$$

## Essential Result

Bayes' theorem, whenever $P(A)>0$:

$$P(B_j\mid A)=\frac{P(A\mid B_j)P(B_j)}{\sum_i P(A\mid B_i)P(B_i)}.$$

## Small Example

If a test is positive with probability $0.9$ for disease and $0.05$ without disease, and prevalence is $0.01$, then $P(D\mid +)=0.009/(0.009+0.0495)\approx0.154$.

## Common Mistakes

- Ignoring base rates.
- Using Bayes' theorem when conditioning events do not form partition.

## Connections

- [[Probabilidade Condicional|Conditional Probability]]
- [[Independência|Independence]]
- [[Distribuições Conjuntas Marginais e Condicionais|Joint Marginal and Conditional Distributions]]

## References

[^openstax-prob]: OpenStax, *Introductory Statistics 2e*, "Chapter 3: Probability Topics", https://openstax.org/books/introductory-statistics-2e/pages/3-introduction
