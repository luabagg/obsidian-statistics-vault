---
dg-publish: true
aliases:
  - Hypothesis Testing
  - Teste de Hipóteses
---

# Hypothesis Testing

## Summary

Hypothesis testing uses sample evidence to decide between a null hypothesis and an alternative hypothesis. A test statistic measures how far the sample result is from the null value; if the statistic falls in a predetermined rejection region, the null is rejected. The structure of the alternative determines whether the test is one-tailed or two-tailed.[^openstax-ht]

## Prerequisites

- [[Inferência Estatística/Estimação Pontual|Point Estimation]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]
- [[Probabilidade/Teorema Central do Limite|Central Limit Theorem]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição Normal|Normal Distribution]]

## Definition / Notation

| Symbol | Meaning |
|---|---|
| $H_0$ | Null hypothesis |
| $H_1$ or $H_a$ | Alternative hypothesis |
| $T$ | Test statistic |
| $R$ | Rejection region |
| $\alpha$ | Significance level, $P(\text{reject }H_0\mid H_0\text{ true})$ |

A test of $H_0:\theta=\theta_0$ against $H_a:\theta\neq\theta_0$ is two-tailed; tests against $H_a:\theta>\theta_0$ or $H_a:\theta<\theta_0$ are one-tailed.

## Parameters / Assumptions

- A fully specified parametric model under $H_0$.
- Independent observations, unless the test is designed for dependence.
- The sampling distribution of the test statistic under $H_0$ is known or approximated.
- The significance level $\alpha$ is fixed before seeing the data.

## Essential Result

For $H_0:\mu=\mu_0$ with known $\sigma$, the test statistic is

$$
Z=\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}\sim N(0,1)\quad\text{under }H_0.
$$

- Two-tailed test ($H_a:\mu\neq\mu_0$): reject if $|Z|>z_{\alpha/2}$.
- One-tailed upper test ($H_a:\mu>\mu_0$): reject if $Z>z_\alpha$.
- One-tailed lower test ($H_a:\mu<\mu_0$): reject if $Z<-z_\alpha$.

There is a duality between two-sided tests and confidence intervals: a two-sided $100(1-\alpha)\%$ confidence interval contains exactly the values of $\mu_0$ that would not be rejected by a two-sided $\alpha$-level test.[^mit-ht]

## Worked Example

Test $H_0:\mu=100$ against $H_a:\mu\neq 100$ with $n=36$, $\bar{x}=104$, $\sigma=12$, and $\alpha=0.05$. The test statistic is

$$
z=\frac{104-100}{12/\sqrt{36}}=2.
$$

Since $|2|>1.96$, reject $H_0$ at the 5% level.

## Common Mistakes

- Confusing statistical significance with practical importance.
- Choosing a one-tailed alternative after seeing the data direction.
- Believing that failing to reject $H_0$ proves $H_0$ is true.
- Applying a test whose distribution assumptions are violated.

## Connections

- [[Inferência Estatística/p-valor|p-values]]
- [[Inferência Estatística/Erros Tipo I e II|Type I and Type II Errors]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]
- [[Inferência Estatística/Máxima Verossimilhança|Maximum Likelihood]]

## References

[^openstax-ht]: OpenStax, *Introductory Statistics*, "Hypothesis Testing", https://openstax.org/details/books/introductory-statistics
[^mit-ht]: MIT OCW, *Introduction to Probability and Statistics*, "Hypothesis Testing", https://ocw.mit.edu/courses/mathematics/
