---
dg-publish: true
dg-show-local-graph: true
tags:
  - probability
  - distributions
  - discrete
aliases:
  - Discrete Distributions
  - Discretas
---

%% Begin Waypoint %%
- **[[Discrete]]**
	- [[Bernoulli Distribution]]
	- [[Binomial Distribution]]
	- [[Geometric Distribution]]
	- [[Hypergeometric Distribution]]
	- [[Negative Binomial Distribution]]
	- [[Poisson Distribution]]
	- [[Uniform Distribution]]
%% End Waypoint %%

# Discrete Distributions

Compact study note.

## Summary

Discrete distributions assign probability mass to finite or countably infinite support points. They model counts, categories encoded as numbers, and repeated Bernoulli-trial mechanisms.[^openstax-discrete]

## Prerequisites

- [[Discrete Random Variable|Discrete Random Variable]]

## Notation and Assumptions

Use $p_X(x)=P(X=x)$ and require $\sum_xp_X(x)=1$ over the support.

## Essential Result

Match the sampling mechanism: Bernoulli for single success/failure trial, binomial for fixed independent trials, geometric for waiting to first success, and Poisson for event counts at fixed rate.

## Small Example

One fair die has a discrete uniform distribution over $\{1,2,3,4,5,6\}$.

## Common Mistakes

- Using a continuous density for count data.
- Leaving support implicit.

## Connections

- [[Bernoulli Distribution|Bernoulli Distribution]]
- [[Binomial Distribution|Binomial Distribution]]
- [[Poisson Distribution|Poisson Distribution]]
- [[Probability/Distributions/Discrete/Uniform Distribution|Discrete Uniform Distribution]]

## References

[^openstax-discrete]: OpenStax, *Introductory Statistics 2e*, "Chapter 4: Discrete Random Variables", https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
