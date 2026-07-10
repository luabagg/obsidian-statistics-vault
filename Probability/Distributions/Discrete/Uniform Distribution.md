---
dg-publish: true
aliases:
  - Discrete Uniform Distribution
  - Distribuição Uniforme Discreta
---

# Discrete Uniform Distribution

Compact study note.

## Summary

One discrete uniform distribution assigns equal probability to each value in a finite set.[^openstax-discrete]

## Prerequisites

- [[Discrete Random Variable|Discrete Random Variable]]

## Definition

$X$ is discrete uniform on $\{x_1,\ldots,x_n\}$ when each support point has probability $1/n$.

## Notation and Assumptions

The support is finite and all listed outcomes are equally likely.

## Parameters

$n\in\{1,2,\ldots\}$.

## Support

$\{x_1,\ldots,x_n\}$.

## PMF or PDF

$P(X=x_i)=1/n$ for $i=1,\ldots,n$.

## CDF

$F_X(x)=n^{-1}\#\{i:x_i\le x\}$.

## Moments

For support $\{1,\ldots,n\}$, $E[X]=(n+1)/2$ and $\operatorname{Var}(X)=(n^2-1)/12$.

## Essential Result

Use this model only when equal likelihood is part of the experiment design or assumption.

## Small Example

One fair six-sided die has $P(X=k)=1/6$ for $k=1,\ldots,6$.

## Common Mistakes

- Assuming all finite outcomes are equally likely without justification.
- Confusing discrete uniform with continuous uniform.

## Connections

- [[Binomial Distribution|Binomial Distribution]]
- [[Probability/Distributions/Continuous/Uniform Distribution|Continuous Uniform Distribution]]
- [[Discrete|Discrete Distributions]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
