---
dg-publish: true
aliases:
  - Maximum Likelihood Estimation
  - Máxima Verossimilhança
---

# Maximum Likelihood Estimation

## Summary

Maximum likelihood estimation chooses the parameter value that makes the observed data most probable under the assumed model. The likelihood function has the same functional form as the joint density or mass function, but is viewed as a function of the parameter. Maximizing the log-likelihood is usually easier and gives the same estimate.[^openstax-mle]

## Prerequisites

- [[Inferência Estatística/Estimação Pontual|Point Estimation]]
- [[Probabilidade/Probabilidade|Probability]]
- [[Probabilidade/Distribuições/Discretas/Distribuição de Bernoulli|Bernoulli Distribution]]
- [[Probabilidade/Distribuições/Contínuas/Distribuição Normal|Normal Distribution]]

## Definition / Notation

For a random sample $X_1,\dots,X_n$ with density or mass function $f(x;\theta)$:

| Symbol | Meaning |
|---|---|
| $L(\theta; x_1,\dots,x_n)$ | Likelihood function, $\prod_{i=1}^n f(x_i;\theta)$ |
| $\ell(\theta)$ | Log-likelihood, $\ln L(\theta; x_1,\dots,x_n)$ |
| $\hat{\theta}_{\mathrm{MLE}}$ | Maximum likelihood estimator |
| $U(\theta)$ | Score function, $\ell'(\theta)$ |
| $I(\theta)$ | Fisher information |

The MLE is

$$
\hat{\theta}_{\mathrm{MLE}}=\arg\max_{\theta} L(\theta; x_1,\dots,x_n).
$$

## Parameters / Assumptions

- The data are i.i.d. from a parametric family $f(x;\theta)$.
- The parameter space is identifiable.
- The support of $f$ does not depend on $\theta$ in the regular case, and the log-likelihood is differentiable at the maximum.
- Boundary maxima must be checked separately.

## Essential Result

- For $X_i\sim\operatorname{Bernoulli}(p)$, $\ell(p)=\sum_i [x_i\ln p+(1-x_i)\ln(1-p)]$. Solving $U(p)=0$ gives $\hat{p}=\bar{x}$.
- For $X_i\sim N(\mu,\sigma^2)$, the MLEs are $\hat{\mu}=\bar{x}$ and $\hat{\sigma}^2=\frac{1}{n}\sum_{i=1}^n(x_i-\bar{x})^2$.
- Under regularity conditions, the MLE is consistent and asymptotically normal:

$$
\sqrt{n}(\hat{\theta}_{\mathrm{MLE}}-\theta)\xrightarrow{d} N(0, I(\theta)^{-1}).
$$

This justifies approximate confidence intervals and tests.[^mit-mle]

## Worked Example

A coin is tossed 20 times and shows 7 heads. Model the outcomes as $\operatorname{Bernoulli}(p)$. The log-likelihood is

$$
\ell(p)=7\ln p+13\ln(1-p).
$$

Setting $\ell'(p)=7/p-13/(1-p)=0$ yields $\hat{p}=7/20=0.35$. The second derivative is negative, confirming a maximum.

## Common Mistakes

- Treating the likelihood as a probability distribution over the parameter.
- Using $n-1$ instead of $n$ in the normal variance MLE.
- Ignoring the boundary of the parameter space.
- Trusting the asymptotic normal approximation in very small samples.

## Connections

- [[Inferência Estatística/Estimação Pontual|Point Estimation]]
- [[Inferência Estatística/Intervalos de Confiança|Confidence Intervals]]
- [[Probabilidade/Teorema Central do Limite|Central Limit Theorem]]

## References

[^openstax-mle]: OpenStax, *Introductory Statistics*, "Maximum Likelihood Estimation", https://openstax.org/details/books/introductory-statistics
[^mit-mle]: MIT OCW, *Statistics for Applications*, "Maximum Likelihood Estimation", https://ocw.mit.edu/courses/mathematics/
