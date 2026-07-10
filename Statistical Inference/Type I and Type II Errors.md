---
dg-publish: true
aliases:
  - Type I and Type II Errors
  - Erros Tipo I e II
---

# Type I and Type II Errors

## Summary

Every hypothesis test can make two kinds of errors. A Type I error rejects a true null hypothesis; its probability is $\alpha$. A Type II error fails to reject a false null hypothesis; its probability is $\beta$. Power, defined as $1-\beta$, is the probability of correctly rejecting a false null.[^openstax-errors]

## Prerequisites

- [[Statistical Inference/Hypothesis Testing|Hypothesis Testing]]
- [[Statistical Inference/p-value|p-values]]
- [[Probability/Probability|Probability]]

## Definition / Notation

|  | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject $H_0$ | Type I error ($\alpha$) | Correct decision (power, $1-\beta$) |
| Fail to reject $H_0$ | Correct decision ($1-\alpha$) | Type II error ($\beta$) |

| Symbol | Meaning |
|---|---|
| $\alpha$ | Significance level; probability of Type I error |
| $\beta$ | Probability of Type II error |
| $1-\beta$ | Power of the test |

## Parameters / Assumptions

- The test, sample size $n$, and significance level $\alpha$ are fixed.
- Computing $\beta$ requires a specific alternative parameter value.
- The sampling distributions under both $H_0$ and the chosen alternative are known or approximated.

## Essential Result

For a fixed sample size, $\alpha$ and $\beta$ are inversely related: lowering $\alpha$ raises $\beta$, and vice versa. Increasing $n$ reduces both error probabilities for a fixed alternative. Power increases with larger effect size, larger $\alpha$, smaller variability, and larger sample size.[^mit-power]

## Worked Example

Test $H_0:\mu=100$ against $H_a:\mu=105$ with known $\sigma=10$, $n=25$, and $\alpha=0.05$ for an upper-tailed test. Under $H_0$ the rejection region is

$$
\bar{x}>100+1.645\frac{10}{\sqrt{25}}=103.29.
$$

If $\mu=105$, then $\bar{X}\sim N(105, 4)$. Thus

$$
\beta=P(\bar{X}\le 103.29)=P\left(Z\le \frac{103.29-105}{2}\right)\approx P(Z\le -0.86)\approx 0.195.
$$

The power is $1-\beta\approx 0.805$.

## Common Mistakes

- Thinking $\alpha+\beta=1$.
- Ignoring that $\beta$ depends on the specific alternative value.
- Believing a non-significant result means the effect is exactly zero.
- Choosing sample size without considering the desired power.

## Connections

- [[Statistical Inference/Hypothesis Testing|Hypothesis Testing]]
- [[Statistical Inference/p-value|p-values]]
- [[Statistical Inference/Confidence Intervals|Confidence Intervals]]

## References

[^openstax-errors]: OpenStax, *Introductory Statistics*, "Type I and Type II Errors", https://openstax.org/details/books/introductory-statistics
[^mit-power]: MIT OCW, *Introduction to Probability and Statistics*, "Power of Tests", https://ocw.mit.edu/courses/mathematics/
