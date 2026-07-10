---
dg-publish: true
aliases:
  - Moment Generating Functions
  - MGF
  - Funções Geradoras de Momento
---

# Moment Generating Functions

Compact study note.

## Summary

Moment generating functions package moments through expectations of exponentials when they exist near zero.[^mit-prob]

$$M_X(t)=E[\exp(tX)], \qquad K_X(t)=\log M_X(t).$$

## Prerequisites

- [[Esperança de uma Variável Aleatória|Expected Value]]

## Notation and Assumptions

Use $M_X(t)$ for the MGF and $K_X(t)$ for the cumulant generating function. Do not use nonstandard 'central MGF' or 'asymmetric MGF' like separate standard objects.

## Essential Result

If $M_X$ exists near $0$, then $E[X^n]=M_X^{(n)}(0)$. If independent $X,Y$ have MGFs near $0$, then $M_{X+Y}(t)=M_X(t)M_Y(t)$.

## Small Example

For $X\sim\operatorname{Bernoulli}(p)$, $M_X(t)=(1-p)+pe^t$ and $M_X'(0)=p$.

## Common Mistakes

- Assuming every distribution has an MGF near zero; log-normal does not.
- Confusing an MGF with one characteristic function, which always exists.

## Connections

- [[Esperança a Partir da Função Geradora de Momentos|Expectation from an MGF]]
- [[Função Característica|Characteristic Function]]
- [[Distribuição de Bernoulli|Bernoulli Distribution]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
