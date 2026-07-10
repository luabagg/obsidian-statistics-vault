---
dg-publish: true
aliases:
  - One-Way ANOVA
  - ANOVA
  - Analysis of Variance
---

# One-Way ANOVA

## Summary

One-way analysis of variance compares the means of several groups defined by a single categorical factor. It partitions total variation into variation between groups and variation within groups, then tests whether the between-group variation is large relative to the within-group variation using an F-statistic. Significant results are usually followed by post-hoc comparisons to identify which means differ.[^openstax-anova]

## Prerequisites

- [[Inferência Estatística/Regressão Linear|Simple Linear Regression]]
- [[Probabilidade/Variável Aleatória/Esperança de uma Variável Aleatória|Expectation]]
- [[Probabilidade/Variável Aleatória/Variância de uma Variável Aleatória|Variance]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição F (Distribuição de Freira)|F-Distribution]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição Qui-Quadrado|Chi-Square Distribution]]

## Definition / Notation

The model for group $i=1,\dots,k$ and observation $j=1,\dots,n_i$ is

$$
Y_{ij}=\mu+\alpha_i+\varepsilon_{ij},
$$

with the constraint $\sum_{i=1}^k n_i\alpha_i=0$.

| Symbol | Meaning |
|---|---|
| $Y_{ij}$ | Observation $j$ in group $i$ |
| $\mu$ | Overall mean |
| $\alpha_i$ | Effect of group $i$ |
| $\bar{Y}_{i.}$ | Mean of group $i$ |
| $\bar{Y}_{..}$ | Grand mean |
| $SST$ | Total sum of squares |
| $SSB$ | Between-group sum of squares |
| $SSE$ | Within-group (error) sum of squares |
| $N$ | Total sample size, $\sum_i n_i$ |

The sums of squares are

$$
SST=\sum_{i=1}^k\sum_{j=1}^{n_i}(Y_{ij}-\bar{Y}_{..})^2,
$$

$$
SSB=\sum_{i=1}^k n_i(\bar{Y}_{i.}-\bar{Y}_{..})^2,
$$

$$
SSE=\sum_{i=1}^k\sum_{j=1}^{n_i}(Y_{ij}-\bar{Y}_{i.})^2.
$$

They satisfy $SST=SSB+SSE$.

## Parameters / Assumptions

- Independent random samples from $k$ populations.
- Each population is approximately normal.
- The populations share a common variance $\sigma^2$ (homoscedasticity).
- Observations are independent within and across groups.

## Essential Result

The hypotheses are

$$
H_0:\mu_1=\mu_2=\dots=\mu_k
$$

against

$$
H_a:\text{at least two means differ}.
$$

The test statistic is

$$
F=\frac{MSB}{MSE}=\frac{SSB/(k-1)}{SSE/(N-k)}\sim F_{k-1,N-k}\quad\text{under }H_0.
$$

Reject $H_0$ if $F>F_{\alpha,k-1,N-k}$. When $H_0$ is rejected, post-hoc procedures such as Tukey's HSD or Bonferroni corrections control the family-wise error rate for pairwise comparisons.[^nist-anova]

## Worked Example

Three teaching methods produce scores:

- Method A: 78, 82, 85
- Method B: 88, 90, 92
- Method C: 80, 84, 86

Group means are $81.67$, $90$, and $83.33$; the grand mean is $85$. The sums of squares are

$$
SSB\approx 116.67,\qquad SSE\approx 51.33,\qquad SST\approx 168.00.
$$

With $k=3$ and $N=9$, $MSB=58.33$ and $MSE=8.56$, giving

$$
F=\frac{58.33}{8.56}\approx 6.82.
$$

Since $F_{0.05,2,6}\approx 5.14$, we reject $H_0$ and conclude that at least one method mean differs.

## Common Mistakes

- Running many pairwise t-tests instead of ANOVA, which inflates the Type I error rate.
- Ignoring the equal-variance assumption.
- Concluding that all groups differ when only some do.
- Using ANOVA when the response is not continuous or the groups are not independent.

## Connections

- [[Inferência Estatística/Regressão Linear|Simple Linear Regression]]
- [[Inferência Estatística/Teste de Hipóteses|Hypothesis Testing]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição F (Distribuição de Freira)|F-Distribution]]
- [[Inferência Estatística/Erros Tipo I e II|Type I and Type II Errors]]

## References

[^openstax-anova]: OpenStax, *Introductory Statistics*, "One-Way ANOVA", https://openstax.org/details/books/introductory-statistics
[^nist-anova]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Analysis of Variance", https://www.itl.nist.gov/div898/handbook/
