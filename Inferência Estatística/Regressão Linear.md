---
dg-publish: true
aliases:
  - Simple Linear Regression
  - Linear Regression
  - Regressão Linear
---

# Simple Linear Regression

## Summary

Simple linear regression models the mean response of a continuous outcome $Y$ as a linear function of a single predictor $x$. The coefficients are usually estimated by ordinary least squares, which minimizes the sum of squared residuals. Under standard assumptions, these estimators are the best linear unbiased estimators, and normal-theory inference applies to the slopes.[^openstax-regression]

## Prerequisites

- [[Álgebra Linear/Least Squares and QR|Least Squares]]
- [[Probabilidade/Covariância e Correlação|Covariance and Correlation]]
- [[Probabilidade/Variável Aleatória/Esperança de uma Variável Aleatória|Expectation]]
- [[Probabilidade/Variável Aleatória/Variância de uma Variável Aleatória|Variance]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição Normal|Normal Distribution]]

## Definition / Notation

The model is

$$
Y_i=\beta_0+\beta_1 x_i+\varepsilon_i,\qquad i=1,\dots,n.
$$

| Symbol | Meaning |
|---|---|
| $Y_i$ | Response variable |
| $x_i$ | Predictor, treated as fixed or conditioned upon |
| $\beta_0,\beta_1$ | Intercept and slope parameters |
| $\varepsilon_i$ | Random error |
| $\hat{Y}_i$ | Fitted value, $\hat{\beta}_0+\hat{\beta}_1 x_i$ |
| $e_i$ | Residual, $Y_i-\hat{Y}_i$ |
| $R^2$ | Coefficient of determination |

The least-squares estimates are

$$
\hat{\beta}_1=\frac{\sum_{i=1}^n(x_i-\bar{x})(Y_i-\bar{Y})}{\sum_{i=1}^n(x_i-\bar{x})^2},\qquad
\hat{\beta}_0=\bar{Y}-\hat{\beta}_1\bar{x}.
$$

## Parameters / Assumptions

- The predictor values $x_i$ are fixed or conditioned upon.
- Errors have mean zero, constant variance $\sigma^2$, and are uncorrelated (Gauss-Markov assumptions).
- For inference on slopes, errors are additionally assumed i.i.d. normal.
- The predictor is not constant, so $\sum(x_i-\bar{x})^2>0$.

## Essential Result

The Gauss-Markov theorem states that, under the assumptions above, the least-squares estimators are the best linear unbiased estimators (BLUE). Under normality,

$$
\hat{\beta}_1\sim N\left(\beta_1,\frac{\sigma^2}{S_{xx}}\right),
$$

where $S_{xx}=\sum_{i=1}^n(x_i-\bar{x})^2$. In practice $\sigma^2$ is estimated by $s^2=\frac{\sum e_i^2}{n-2}$, and

$$
t=\frac{\hat{\beta}_1-\beta_{1,0}}{s/\sqrt{S_{xx}}}\sim t_{n-2}
$$

under $H_0:\beta_1=\beta_{1,0}$. The coefficient of determination is

$$
R^2=1-\frac{\sum e_i^2}{\sum(Y_i-\bar{Y})^2}.
$$

## Worked Example

For data $x=(1,2,3,4)$ and $y=(2,4,5,7)$:

$$
\bar{x}=2.5,\quad \bar{y}=4.5,\quad S_{xx}=5,\quad S_{xy}=7.
$$

Thus

$$
\hat{\beta}_1=\frac{7}{5}=1.4,\qquad \hat{\beta}_0=4.5-1.4(2.5)=1.0.
$$

The fitted line is $\hat{y}=1.0+1.4x$.[^mit-regression]

## Common Mistakes

- Confusing correlation with causation.
- Extrapolating beyond the observed range of $x$.
- Ignoring non-constant variance, outliers, or influential points.
- Assuming a statistically significant slope implies a large practical effect.

## Connections

- [[Álgebra Linear/Least Squares and QR|Least Squares]]
- [[Inferência Estatística/ANOVA|ANOVA]]
- [[Probabilidade/Covariância e Correlação|Covariance and Correlation]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]

## References

[^openstax-regression]: OpenStax, *Introductory Statistics*, "Linear Regression", https://openstax.org/details/books/introductory-statistics
[^mit-regression]: MIT OCW, *Introduction to Probability and Statistics*, "Simple Linear Regression", https://ocw.mit.edu/courses/mathematics/
