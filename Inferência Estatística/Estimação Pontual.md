---
dg-publish: true
aliases:
  - Point Estimation
  - Estimação Pontual
---

# Point Estimation

## Summary

Point estimation uses a sample statistic to infer the value of an unknown population parameter. An estimator is the rule viewed as a random variable before data are collected; an estimate is the numerical value obtained after sampling. Key properties are unbiasedness, consistency, and efficiency, and common construction methods include the method of moments and maximum likelihood.[^openstax-point-est]

## Prerequisites

- [[Probabilidade/Probabilidade|Probability]]
- [[Probabilidade/Variável Aleatória/Variável Aleatória|Random Variable]]
- [[Probabilidade/Variável Aleatória/Esperança de uma Variável Aleatória|Expectation]]
- [[Probabilidade/Variável Aleatória/Variância de uma Variável Aleatória|Variance]]
- [[Probabilidade/Lei dos Grandes Números|Law of Large Numbers]]

## Definition / Notation

Let $X_1,\dots,X_n$ be a random sample from a distribution that depends on an unknown parameter $\theta$.

| Symbol | Meaning |
|---|---|
| $\theta$ | Unknown population parameter |
| $\hat{\theta}_n$ | Estimator of $\theta$, a statistic $T(X_1,\dots,X_n)$ |
| $\hat{\theta}_{n,\text{obs}}$ | Estimate, the observed value of the estimator |
| $\operatorname{Bias}(\hat{\theta}_n)$ | $E[\hat{\theta}_n]-\theta$ |
| $\operatorname{MSE}(\hat{\theta}_n)$ | $E[(\hat{\theta}_n-\theta)^2]$ |

The mean squared error decomposes as:

$$
\operatorname{MSE}(\hat{\theta}_n)=\operatorname{Var}(\hat{\theta}_n)+\operatorname{Bias}(\hat{\theta}_n)^2
$$

## Parameters / Assumptions

- The sample $X_1,\dots,X_n$ is independent and identically distributed (i.i.d.).
- The parameter space is known and the model is identifiable.
- The estimator has finite first and second moments.

## Essential Result

A good estimator should satisfy one or more of the following:

- **Unbiasedness**: $E[\hat{\theta}_n]=\theta$.
- **Consistency**: $\hat{\theta}_n \xrightarrow{P}\theta$ as $n\to\infty$.
- **Efficiency**: among unbiased estimators, $\hat{\theta}_n$ has the smallest possible variance; under regularity conditions the variance attains the Cramér–Rao lower bound.
- **Method of moments**: equate sample moments to population moments and solve for the parameters.
- **Maximum likelihood**: choose the parameter value that maximizes the likelihood of the observed sample.[^mit-estimation]

## Worked Example

Suppose $X_1,\dots,X_n\sim\operatorname{Bernoulli}(p)$ and we use $\hat{p}=\bar{X}$. Then

$$
E[\hat{p}]=p,\qquad \operatorname{Var}(\hat{p})=\frac{p(1-p)}{n}.
$$

Thus $\hat{p}$ is unbiased. By Chebyshev's inequality,

$$
P(|\bar{X}-p|\ge \varepsilon)\le \frac{p(1-p)}{n\varepsilon^2}\to 0,
$$

so $\hat{p}$ is also consistent.

## Common Mistakes

- Calling an observed number an estimator; it is an estimate.
- Thinking that unbiasedness alone guarantees a small error; variance matters too.
- Forgetting that consistency is a property of a sequence of estimators as $n$ grows.
- Applying the method of moments when the required moments do not exist.

## Connections

- [[Inferência Estatística/Máxima Verossimilhança|Maximum Likelihood]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]
- [[Probabilidade/Teorema Central do Limite|Central Limit Theorem]]
- [[Probabilidade/Lei dos Grandes Números|Law of Large Numbers]]

## References

[^openstax-point-est]: OpenStax, *Introductory Statistics*, "Point Estimation", https://openstax.org/details/books/introductory-statistics
[^mit-estimation]: MIT OCW, *Introduction to Probability and Statistics*, "Estimation", https://ocw.mit.edu/courses/mathematics/
