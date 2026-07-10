---
dg-publish: true
aliases:
  - Probability Space
  - Espaco de Probabilidade
---

# Probability Space

Compact study note.

## Summary

Probability space is the complete mathematical model for random experiment structure. It combines possible outcomes, measurable events, and probability measure.[^mit-prob]

## Prerequisites

- [[Sample Space and Events|Sample Space and Events]]
- [[Sigma-Algebra|Sigma-Algebra]]

## Notation and Assumptions

Probability space notation:

$$(\Omega,\mathcal{F},P).$$

It consists of sample space $\Omega$, event sigma-algebra $\mathcal{F}$, and probability measure $P:\mathcal{F}\to[0,1]$ with $P(\Omega)=1$ and countable additivity over disjoint events.

## Essential Result

All probability statements are statements about events in $\mathcal{F}$. Random variables are measurable functions defined on this space.

## Small Example

For a fair coin, $\Omega=\{H,T\}$, $\mathcal{F}=\mathcal{P}(\Omega)$, and $P(\{H\})=P(\{T\})=1/2$.

## Common Mistakes

- Writing probabilities for sets outside $\mathcal{F}$.
- Leaving $\mathcal{F}$ implicit in measure-theoretic arguments.

## Connections

- [[Probability|Probability]]
- [[Conditional Probability|Conditional Probability]]
- [[Random Variable|Random Variable]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
