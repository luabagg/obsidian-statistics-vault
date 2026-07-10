---
dg-publish: true
aliases:
  - Log-Normal Distribution
  - Distribuição Log-Normal
---

# Log-Normal Distribution

Compact study note.

## Summary

One log-normal random variable is the exponential of a normal random variable. It is positive and right-skewed, with parameters inherited from the normal distribution on the log scale.[^nist-gallery]

## Prerequisites

- [[Normal Distribution|Normal Distribution]]
- [[Functions of Random Variables|Functions of Random Variables]]

## Definition

If $Y\sim N(\mu,\sigma^2)$ and $X=e^Y$, then $X\sim\operatorname{LogNormal}(\mu,\sigma^2)$.

## Notation and Assumptions

$\mu$ is any real number and $\sigma>0$. These are not the mean and standard deviation of $X$.

## Parameters

$\mu\in\mathbb{R}$ and $\sigma>0$.

## Support

$(0,\infty)$.

## PMF or PDF

$f_X(x)=\frac{1}{x\sigma\sqrt{2\pi}}\exp[-(\ln x-\mu)^2/(2\sigma^2)]$ for $x>0$.

## CDF

$F_X(x)=\Phi((\ln x-\mu)/\sigma)$ for $x>0$.

## Moments

Moments:

$$E[X]=\exp(\mu+\sigma^2/2).$$

$$\operatorname{Var}(X)=(\exp(\sigma^2)-1)\exp(2\mu+\sigma^2).$$

The MGF is not finite for any $t>0$.

## Essential Result

The distribution exists for every $\mu\in\mathbb{R}$ and $\sigma>0$; there is no extra condition including $m-r^2<0$.

## Small Example

If $Y\sim N(0,1)$ and $X=\exp(Y)$, then the median of $X$ is $1$ and

$$E[X]=\exp(1/2).$$

## Common Mistakes

- Confusing log-scale parameters with the mean and variance of $X$.
- Claiming an ordinary MGF exists near zero.

## Connections

- [[Normal Distribution|Normal Distribution]]
- [[Functions of Random Variables|Functions of Random Variables]]
- [[Probability Density|Probability Density Function]]

## References

[^nist-gallery]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "1.3.6.6 Gallery of Distributions", https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm
