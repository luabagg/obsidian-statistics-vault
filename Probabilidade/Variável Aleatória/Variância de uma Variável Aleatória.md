---
dg-publish: true
aliases:
  - Variance
  - Variância de uma Variável Aleatória
---

# Variance

Compact study note.

## Summary

Variance measures mean squared deviation from the expected value. It is nonnegative and has squared units.[^openstax-discrete]

## Prerequisites

- [[Esperança de uma Variável Aleatória|Expected Value]]

## Notation and Assumptions

Variance identity:

$$\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-(E[X])^2.$$

Use it when $E[X^2]$ is finite.

## Essential Result

For constants $c,d$,

$$\operatorname{Var}(c+dX)=d^2\operatorname{Var}(X).$$

If $X$ and $Y$ are independent,

$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).$$

## Small Example

If $X\sim\operatorname{Bernoulli}(p)$, then $E[X^2]=p$ and $\operatorname{Var}(X)=p-p^2=p(1-p)$.

## Common Mistakes

- Squaring the added constant instead of the coefficient multiplying $X$.
- Adding variances without independence or zero covariance.

## Connections

- [[Covariância e Correlação|Covariance and Correlation]]
- [[Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Distribuição Binomial|Binomial Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
