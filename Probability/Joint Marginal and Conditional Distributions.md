---
dg-publish: true
aliases:
  - Joint Marginal and Conditional Distributions
  - Distribuições Conjuntas Marginais e Condicionais
---

# Joint, Marginal, and Conditional Distributions

Compact study note.

## Summary

One joint distribution describes random variables together. Marginal distributions summarize one variable; conditional distributions describe one variable after another value or event is known.[^mit-prob]

## Prerequisites

- [[Random Variable|Random Variable]]
- [[Conditional Probability|Conditional Probability]]

## Notation and Assumptions

For discrete variables, use $p_{X,Y}(x,y)=P(X=x,Y=y)$. Marginals are $p_X(x)=\sum_y p_{X,Y}(x,y)$ and $p_Y(y)=\sum_x p_{X,Y}(x,y)$.

## Essential Result

When $p_Y(y)>0$, $p_{X\mid Y}(x\mid y)=p_{X,Y}(x,y)/p_Y(y)$. Continuous versions replace sums by integrals and PMFs by densities.

## Small Example

If $p_{X,Y}(0,0)=0.2$, $p_{X,Y}(1,0)=0.3$, $p_{X,Y}(0,1)=0.1$, $p_{X,Y}(1,1)=0.4$, then $p_X(1)=0.7$.

## Common Mistakes

- Confusing joint probability with conditional probability.
- For continuous variables, treating $f_{X,Y}(x,y)$ as point probability.

## Connections

- [[Conditional Probability|Conditional Probability]]
- [[Independence|Independence]]
- [[Covariance and Correlation|Covariance and Correlation]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
