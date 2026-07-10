---
dg-publish: true
aliases:
  - Continuous Random Variable
  - Variavel Aleatoria Continua
  - Variável Aleatória Contínua
---

# Continuous Random Variable

Compact study note.

## Summary

One continuous random variable is commonly represented by a probability density function. Probabilities come from areas under the density, not from density values at points.[^openstax-continuous]

## Prerequisites

- [[Random Variable|Random Variable]]
- [[Probability Density|Probability Density Function]]

## Notation and Assumptions

One continuous random variable with density $f_X$ has $F_X(x)=\int_{-\infty}^{x}f_X(u)\,du$ and $f_X(u)\ge0$ with total integral $1$.

## Essential Result

For interval endpoints $l<u$,

$$P(l\le X\le u)=\int_l^u f_X(x)\,dx.$$

Also $P(X=c)=0$ for every single point $c$.

## Small Example

If $X\sim\operatorname{Uniform}(0,1)$, then $P(0.2<X<0.5)=\int_{0.2}^{0.5}1\,dx=0.3$.

## Common Mistakes

- Interpreting $f_X(x)$ itself as point probability.
- Expecting endpoint inclusions to matter for continuous distributions.

## Connections

- [[Probability Density|Probability Density Function]]
- [[Cumulative Distribution Function|Cumulative Distribution Function]]
- [[Normal Distribution|Normal Distribution]]

## References

[^openstax-continuous]: OpenStax, *Introductory Statistics 2e*, "Chapter 5: Continuous Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/5-introduction
