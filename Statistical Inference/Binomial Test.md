---
dg-publish: true
aliases:
  - Binomial Test
  - Teste Binomial
  - Exact binomial test
---

# Binomial Test

## Summary

The binomial test assesses a population proportion \(p\) when each observation is binary (success/failure) and trials are independent. Under the null \(H_0:p=p_0\), the success count \(X\) follows \(\operatorname{Binomial}(n,p_0)\). Exact p-values use the binomial PMF/CDF; for large \(n\), a normal approximation to \(X\) is sometimes used.[^openstax-ht][^r-binom]

## Prerequisites

- [[Statistical Inference/Hypothesis Testing|Hypothesis Testing]]
- [[Statistical Inference/p-value|p-values]]
- [[Probability/Distributions/Discrete/Binomial Distribution|Binomial Distribution]]
- [[Probability/Distributions/Discrete/Bernoulli Distribution|Bernoulli Distribution]]

## Definition / Notation

| Symbol | Meaning |
|---|---|
| \(p\) | True success probability (proportion) |
| \(p_0\) | Hypothesized value under \(H_0\) |
| \(q_0=1-p_0\) | Failure probability under \(H_0\) |
| \(n\) | Number of independent trials |
| \(X\) | Number of successes in \(n\) trials |
| \(\alpha\) | Significance level (fixed before seeing data) |

Hypotheses:

- \(H_0: p = p_0\)
- \(H_1: p \neq p_0\) (two-sided), or \(p < p_0\) (lower), or \(p > p_0\) (upper)

## Parameters / Assumptions

- Each trial has exactly two outcomes (success/failure).
- Trials are independent (or sampling with replacement / large population).
- Success probability is constant across trials under the model.
- \(\alpha\) is chosen before looking at the data.
- \(X\) counts successes in the category of interest (not “whichever class is smaller” by default).

## Essential Result

PMF under \(H_0\):

$$
P(X=x)=\binom{n}{x}p_0^x q_0^{n-x},\qquad
\binom{n}{x}=\frac{n!}{x!(n-x)!}.
$$

Exact lower-tail p-value for observed \(x\) when \(H_1:p<p_0\):

$$
\text{p-value}=P(X\le x\mid H_0)=\sum_{k=0}^{x}\binom{n}{k}p_0^k q_0^{n-k}.
$$

Upper tail uses \(P(X\ge x\mid H_0)\). The two-sided p-value sums probabilities of outcomes at least as extreme as observed (implementation-dependent; R’s `binom.test` documents its rule).

Decision: reject \(H_0\) if p-value \(< \alpha\).

### Large-sample normal approximation

When \(n\) is large (common rule of thumb \(n>30\), and \(np_0\), \(nq_0\) not tiny):

$$
Z=\frac{X-np_0}{\sqrt{np_0 q_0}}\approx N(0,1)\quad\text{under }H_0.
$$

Prefer the exact binomial test when \(n\) is moderate or counts are extreme.

## Worked Example

Test \(H_0:p=0.3\) vs \(H_1:p<0.3\) with \(n=10\), \(x=1\), \(\alpha=0.05\).

$$
\begin{align*}
P(X=0)&=\binom{10}{0}(0.3)^0(0.7)^{10}=0.7^{10},\\
P(X=1)&=\binom{10}{1}(0.3)^1(0.7)^{9},\\
\text{p-value}&=P(X\le 1)=P(X=0)+P(X=1).
\end{align*}
$$

In R: `pbinom(1, 10, 0.3)` and `binom.test(1, 10, 0.3, alternative = "less", conf.level = 0.95)`.

Note: `conf.level` is \(1-\alpha\) (e.g. `0.95` when \(\alpha=0.05\)), not \(\alpha\) itself.

Large-sample illustration: `binom.test(725, 1500, 0.5)` (exact method in R; the \(Z\) formula above is the classical approximation).

## Code

Runnable script:

`~/development/statistics/r/binomial_test/binomial_test.R`

```bash
Rscript r/binomial_test/binomial_test.R
```

## Common Mistakes

- Passing \(\alpha\) as `conf.level` in `binom.test` (use `1 - alpha`).
- Treating “fail to reject \(H_0\)” as proof that \(p=p_0\).
- Using the normal \(Z\) approximation with small \(n\) or tiny \(np_0\) / \(nq_0\).
- Choosing the tail after seeing which way the data went.
- Coding the “success” category inconsistently with \(p_0\).

## Connections

- [[Statistical Inference/Hypothesis Testing|Hypothesis Testing]]
- [[Statistical Inference/p-value|p-values]]
- [[Statistical Inference/Type I and Type II Errors|Type I and Type II Errors]]
- [[Probability/Distributions/Discrete/Binomial Distribution|Binomial Distribution]]
- [[Statistical Process Control/Control Charts/p Chart|p Chart]]

## References

[^openstax-ht]: OpenStax, *Introductory Statistics*, Hypothesis testing for a single population proportion, https://openstax.org/details/books/introductory-statistics
[^r-binom]: R Core Team, `binom.test` help page (`stats::binom.test`), https://stat.ethz.ch/R-manual/R-devel/library/stats/html/binom.test.html
