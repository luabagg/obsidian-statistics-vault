---
dg-publish: true
aliases:
  - Confidence Intervals
  - Intervalos de Confiança
---

# Confidence Intervals

## Summary

A confidence interval gives a range of plausible values for a population parameter based on sample data. Before sampling, the endpoints are random and the interval has a known probability of covering the true parameter. After sampling, the realized interval either contains the parameter or it does not.[^openstax-ci]

## Prerequisites

- [[Statistical Inference/Point Estimation|Point Estimation]]
- [[Probability/Central Limit Theorem|Central Limit Theorem]]
- [[Probability/Distributions/Continuous/Normal Distribution|Normal Distribution]]
- [[Probability/Distributions/Continuous/Student t Distribution|t-Distribution]]

## Definition / Notation

A $100(1-\alpha)\%$ confidence interval for a parameter $\theta$ is a random interval $(L(X),U(X))$ such that

$$
P(L(X)\le \theta \le U(X))=1-\alpha.
$$

| Symbol | Meaning |
|---|---|
| $1-\alpha$ | Confidence level |
| $z_{\alpha/2}$ | Upper $\alpha/2$ quantile of $N(0,1)$ |
| $t_{\alpha/2,\nu}$ | Upper $\alpha/2$ quantile of $t_\nu$ |
| $\chi^2_{\alpha/2,\nu}$ | Upper $\alpha/2$ quantile of $\chi^2_\nu$ |
| $s$ | Sample standard deviation |

## Parameters / Assumptions

- Random sample $X_1,\dots,X_n$.
- For the mean with known $\sigma$: normal population or $n$ large enough for the Central Limit Theorem.
- For the mean with unknown $\sigma$: approximately normal population or $n$ large.
- For a proportion: $n\hat{p}$ and $n(1-\hat{p})$ are large enough for the normal approximation.
- For a variance ratio: independent normal samples.

## Essential Result

| Parameter | Assumptions | Confidence Interval |
|---|---|---|
| Mean $\mu$ | $\sigma$ known | $\bar{x}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$ |
| Mean $\mu$ | $\sigma$ unknown | $\bar{x}\pm t_{\alpha/2,n-1}\frac{s}{\sqrt{n}}$ |
| Proportion $p$ | Large sample | $\hat{p}\pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ |
| Variance ratio $\sigma_1^2/\sigma_2^2$ | Independent normal samples | $\left(\frac{s_1^2}{s_2^2}\frac{1}{F_{\alpha/2,n_1-1,n_2-1}},\ \frac{s_1^2}{s_2^2}F_{\alpha/2,n_2-1,n_1-1}\right)$ |

The correct interpretation is that $100(1-\alpha)\%$ of intervals constructed by this procedure will cover $\theta$.[^nist-ci]

## Worked Example

A sample of size $n=25$ has mean $\bar{x}=50$ and standard deviation $s=10$. A 95% confidence interval for $\mu$ uses $t_{0.025,24}\approx 2.064$:

$$
50\pm 2.064\frac{10}{\sqrt{25}} = 50\pm 4.128.
$$

The interval is $(45.87,\,54.13)$.

## Common Mistakes

- Saying "the probability that $\theta$ is in this interval is 0.95" after the data are observed.
- Using the normal quantile when $\sigma$ is unknown and $n$ is small.
- Forgetting the $\sqrt{n}$ in the standard error.
- Treating a confidence interval as a prediction interval for future observations.

## Connections

- [[Statistical Inference/Hypothesis Testing|Hypothesis Testing]]
- [[Statistical Inference/Maximum Likelihood|Maximum Likelihood]]
- [[Probability/Distributions/Continuous/Normal Distribution|Normal Distribution]]

## References

[^openstax-ci]: OpenStax, *Introductory Statistics*, "Confidence Intervals", https://openstax.org/details/books/introductory-statistics
[^nist-ci]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Confidence Limits", https://www.itl.nist.gov/div898/handbook/
