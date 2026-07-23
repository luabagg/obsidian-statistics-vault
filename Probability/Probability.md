---
dg-publish: true
dg-show-local-graph: true
tags:
  - probability
  - hub
aliases:
  - Probability
  - Probabilidade
---

%% Begin Waypoint %%
- **[[Probability]]**
	- **[[Distributions]]**
	- **[[Random Variable]]**
	- [[Borel Sigma-Algebra]]
	- [[Central Limit Theorem]]
	- [[Conditional Probability]]
	- [[Covariance and Correlation]]
	- [[De Morgan Laws]]
	- [[IID Random Variables]]
	- [[Independence]]
	- [[Joint Marginal and Conditional Distributions]]
	- [[Law of Large Numbers]]
	- [[Probability Space]]
	- [[Quantiles]]
	- [[Sample Space and Events]]
	- [[Sigma-Algebra]]
	- [[Total Probability and Bayes Theorem]]
%% End Waypoint %%

# Probability

Compact study note.

## Summary

Probability assigns coherent numerical weights to uncertain events. Modern probability starts with sample space, event sigma-algebra, and probability measure.[^mit-prob]

## Prerequisites

- Prerequisites: None

## Notation and Assumptions

Use $(\Omega, \mathcal{F}, P)$ for probability space notation: outcomes live in $\Omega$, events live in $\mathcal{F}$, and $P$ maps events to numbers in $[0,1]$.

## Essential Result

The core workflow is: define outcomes, choose measurable events, assign probabilities, then study random variables and distributions derived from those events.

## Small Example

For fair die roll, $\Omega=\{1,2,3,4,5,6\}$ and $P(\{2,4,6\})=3/6=1/2$ for event 'even result'.

## Common Mistakes

- Treating outcome $3$ and event $\{3\}$ as identical objects.
- Using formulas before checking the event belongs to the chosen sigma-algebra.

## Connections

- [[Sample Space and Events|Sample Space and Events]]
- [[Probability Space|Probability Space]]
- [[Conditional Probability|Conditional Probability]]
- [[Distributions|Distributions]]
- [[Random Variable|Random Variables]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
