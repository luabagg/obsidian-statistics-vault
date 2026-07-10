---
dg-publish: true
aliases:
  - Covariance and Correlation
  - Covariancia e Correlacao
  - Covariância e Correlação
---

# Covariance and Correlation

Compact study note.

## Summary

Covariance measures linear co-movement between two random variables. Correlation rescales covariance to a unitless number between $-1$ and $1$ when both variances are positive.[^mit-prob]

## Prerequisites

- [[Esperança de uma Variável Aleatória|Expected Value]]
- [[Variância de uma Variável Aleatória|Variance]]

## Notation and Assumptions

Core definitions:

$$\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])].$$

$$\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.$$

## Essential Result

$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$. Independence implies zero covariance when moments exist, but zero covariance does not imply independence in general.

## Small Example

If $Y=2X+1$ and $\operatorname{Var}(X)>0$, then $\rho_{X,Y}=1$ because the relationship is exactly increasing linear.

## Common Mistakes

- Equating zero correlation with independence.
- Forgetting units: covariance has product units; correlation has no units.

## Connections

- [[Independência|Independence]]
- [[Variância de uma Variável Aleatória|Variance]]
- [[Distribuições Conjuntas Marginais e Condicionais|Joint Marginal and Conditional Distributions]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
