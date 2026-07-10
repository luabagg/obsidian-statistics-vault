---
dg-publish: true
aliases:
  - Conditional Probability
  - Probabilidade Condicional
---

# Conditional Probability

Compact study note.

## Summary

Conditional probability updates the probability of an event after restricting attention to another event that occurred. It is the basis for Bayes' theorem and conditional distributions.[^openstax-prob]

## Prerequisites

- [[Espaço de Probabilidade|Probability Space]]

## Notation and Assumptions

For events $A,B\in\mathcal{F}$ with $P(B)>0$:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$

## Essential Result

Conditioning changes the denominator from the whole sample space to the event being conditioned on.

## Small Example

In a fair die roll, condition on result being at least $4$. The even outcomes inside that condition are $4$ and $6$, so

$$P(\text{even}\mid \text{at least }4)=\frac{2/6}{3/6}=2/3.$$

## Common Mistakes

- Conditioning on an event with probability zero without additional theory.
- Assuming reversed conditional probabilities are equal.

## Connections

- [[Probabilidade Total e Teorema de Bayes|Total Probability and Bayes' Theorem]]
- [[Independência|Independence]]
- [[Distribuições Conjuntas Marginais e Condicionais|Joint Marginal and Conditional Distributions]]

## References

[^openstax-prob]: OpenStax, *Introductory Statistics 2e*, "Chapter 3: Probability Topics", https://openstax.org/books/introductory-statistics-2e/pages/3-introduction
