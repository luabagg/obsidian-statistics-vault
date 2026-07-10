---
dg-publish: true
aliases:
  - p-value
  - p-values
  - p-valor
---

# p-values

## Summary

The p-value is the probability, computed under the assumption that the null hypothesis is true, of obtaining a test statistic at least as extreme as the one observed. It measures the compatibility between the data and the null hypothesis, not the probability that the null is true.[^openstax-pvalue]

## Prerequisites

- [[Inferência Estatística/Teste de Hipóteses|Hypothesis Testing]]
- [[Inferência Estatística/Estimação Pontual|Point Estimation]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição Normal|Normal Distribution]]

## Definition / Notation

For an observed test statistic $t_{\text{obs}}$:

$$
\text{p-value}=P(T\ge t_{\text{obs}}\mid H_0\text{ true})
$$

for an upper-tailed test, with the inequality reversed for a lower-tailed test and a two-tailed version for $H_a:\theta\neq\theta_0$.

| Symbol | Meaning |
|---|---|
| $\alpha$ | Significance level chosen before the test |
| $t_{\text{obs}}$ | Observed value of the test statistic |
| $T$ | Test statistic under $H_0$ |

## Parameters / Assumptions

- The null hypothesis is fully specified, or nuisance parameters are handled.
- The sampling distribution of the test statistic under $H_0$ is known.
- The test and the form of the alternative are selected before seeing the data.

## Essential Result

Decision rule:

- If p-value $< \alpha$, reject $H_0$ at level $\alpha$.
- If p-value $\ge \alpha$, do not reject $H_0$ at level $\alpha$.

A small p-value indicates that the observed result is unusual under $H_0$; it does not measure the size of an effect or the posterior probability of $H_0$.[^nist-pvalue]

## Worked Example

Continuing the normal example with $z=2$ for a two-tailed test:

$$
\text{p-value}=2P(Z>2)\approx 2(0.0228)=0.0456.
$$

Since $0.0456<0.05$, we would reject $H_0$ at the 5% significance level.

## Common Mistakes

- Saying "$H_0$ is true with probability p".
- Treating p-value as an effect-size measure.
- Comparing p-values across different studies or sample sizes directly.
- Treating 0.05 as an absolute boundary between truth and falsehood.

## Connections

- [[Inferência Estatística/Teste de Hipóteses|Hypothesis Testing]]
- [[Inferência Estatística/Erros Tipo I e II|Type I and Type II Errors]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]

## References

[^openstax-pvalue]: OpenStax, *Introductory Statistics*, "p-value", https://openstax.org/details/books/introductory-statistics
[^nist-pvalue]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "p-value", https://www.itl.nist.gov/div898/handbook/
