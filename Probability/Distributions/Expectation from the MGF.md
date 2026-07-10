---
dg-publish: true
aliases:
  - Expectation from an MGF
  - Esperança a Partir da Função Geradora de Momentos
---

# Expectation from a Moment Generating Function

Compact study note.

## Summary

When an MGF exists near zero, derivatives at zero recover raw moments. This is a compact way to derive means and variances for many standard distributions.[^mit-prob]

## Prerequisites

- [[Moment Generating Functions|Moment Generating Functions]]

## Notation and Assumptions

MGF definition:

$$M_X(t)=E[\exp(tX)].$$

If differentiation under the expectation is justified near $0$, then

$$M_X'(0)=E[X], \qquad M_X''(0)=E[X^2].$$

## Essential Result

$\operatorname{Var}(X)=M_X''(0)-[M_X'(0)]^2$.

## Small Example

For Bernoulli $X$, $M_X(t)=1-p+pe^t$. Then $M_X'(0)=p$, $M_X''(0)=p$, and $\operatorname{Var}(X)=p(1-p)$.

## Common Mistakes

- Differentiating an expression outside its domain of convergence.
- Using this method for a distribution whose MGF does not exist near zero.

## Connections

- [[Moment Generating Functions|Moment Generating Functions]]
- [[Expectation of a Random Variable|Expected Value]]
- [[Variance of a Random Variable|Variance]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
