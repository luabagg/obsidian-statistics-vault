---
dg-publish: false
title: Notes Adjustment Guide
tags:
  - audit
  - maintenance
  - statistics
---

# Notes Adjustment Guide

Use this file as a checklist while rewriting the vault in English, re-studying each topic, and applying the new templates from [[Templates/Template Index|Template Index]].

## Goal

Make the vault trustworthy for review by ensuring that each note is:

- Mathematically correct.
- Written with standard terminology.
- Explicit about notation and assumptions.
- Supported by reliable references.
- Consistent with related notes.
- Easy to review later.

## General Workflow

1. Pick one note.
2. Choose the matching template from [[Templates/Template Index|Template Index]].
3. Rewrite the note in English.
4. Re-study the concept using a reliable source.
5. Correct formulas, assumptions, notation, and examples.
6. Add references.
7. Mark the review checklist inside the template.
8. Link related notes.

## Priority 0: Critical Corrections

Fix these first because they contain factual or mathematical errors.

### Probability and Measure Theory

- [x] [[Probability/Sigma-Algebra|Sigma-Álgebra]]: the example saying that all open and closed subintervals of $[0,1]$ form a sigma-algebra is incorrect. Intervals are not closed under countable unions. Replace with the Borel sigma-algebra or the power set in a finite case.
- [x] [[Probability/Borel Sigma-Algebra|Sigma-Álgebra De Borel]]: the claim that every Borel set can be written as the difference between a closed set and an open set is incorrect. Replace with the correct generated-sigma-algebra definition and examples.
- [x] [[Probability/Borel Sigma-Algebra|Sigma-Álgebra De Borel]]: replace "reta irracional" with standard terminology such as "set of irrational numbers".

### Random Variables and Moments

- [x] [[Probability/Random Variable/Variance of a Random Variable|Variância de uma Variável Aleatória]]: correct the variance transformation formula. The correct identity is:

$$
\operatorname{Var}(a + bX) = b^2\operatorname{Var}(X)
$$

- [x] [[Probability/Random Variable/Moment Generating Functions|Funções Geradoras de Momento]]: remove nonstandard concepts currently called CGF and AGF. Use standard concepts: moment generating function and cumulant generating function.
- [x] [[Probability/Distributions/Expectation from the MGF|Esperança a Partir da Função Geradora de Momentos]]: keep this as the reliable basis for MGF derivations, then link it from distribution notes.

### Continuous Distributions

- [x] [[Probability/Distributions/Continuous/Exponential Distribution|Distribuição Exponencial]]: remove the claim that the exponential distribution is symmetric. It is right-skewed.
- [x] [[Probability/Distributions/Continuous/Chi-Square Distribution|Distribuição Qui-Quadrado]]: remove the claim that the chi-square distribution is symmetric. It is right-skewed, especially for small degrees of freedom.
- [x] [[Probability/Distributions/Continuous/F Distribution|Distribuição F]]: rename the note. "Freira" is wrong; the distribution is named after Fisher and is often called the Fisher-Snedecor F distribution.
- [x] [[Probability/Distributions/Continuous/F Distribution|Distribuição F]]: correct the definition. A chi-square random variable is a sum of squared independent standard normal variables, not a cube.
- [x] [[Probability/Distributions/Continuous/F Distribution|Distribuição F]]: remove the claims that the F distribution is symmetric and has finite limits. It is right-skewed and has support $(0, \infty)$.
- [x] [[Probability/Distributions/Continuous/Student t Distribution|Distribuição T-Student]]: define the t-distribution as a distribution, not only as a test statistic. It has one parameter: degrees of freedom.
- [x] [[Probability/Distributions/Continuous/Gamma Distribution|Distribuição Gama]]: correct the MGF parameterization. For shape $k$ and scale $\theta$:

$$
M_X(t) = (1 - \theta t)^{-k}, \quad t < \frac{1}{\theta}
$$

- [x] [[Probability/Distributions/Continuous/Gamma Distribution|Distribuição Gama]]: correct the moment derivation. For shape $k$ and scale $\theta$:

$$
E[X] = k\theta, \qquad \operatorname{Var}(X) = k\theta^2
$$

- [x] [[Probability/Distributions/Continuous/Log-Normal Distribution|Distribuição Log-Normal]]: remove the false existence condition $m-r^2<0$. A log-normal distribution exists for $m \in \mathbb{R}$ and $r>0$.
- [x] [[Probability/Distributions/Continuous/Log-Normal Distribution|Distribuição Log-Normal]]: make parameter notation consistent. Do not mix $m$, $r$, $\mu$, and $\sigma$ unless each is defined clearly.

### Discrete Distributions

- [x] [[Probability/Distributions/Discrete/Bernoulli Distribution|Distribuição de Bernoulli]]: fix the example section. The expected value of a Bernoulli random variable is $p$. If two coin flips are used, the random variable is binomial, not Bernoulli.

## Priority 1: Standardization

Apply these corrections while rewriting notes.

### Notation

- [x] Use $E[X]$ or $\mathbb{E}[X]$ consistently.
- [x] Use $\operatorname{Var}(X)$ consistently.
- [x] Use $p_X(x)$ or $P(X=x)$ for discrete PMFs.
- [x] Use $f_X(x)$ for continuous PDFs.
- [x] Use $F_X(x)$ for CDFs.
- [x] State the support of every distribution.
- [x] State parameter domains, such as $p \in [0,1]$, $\lambda>0$, $\sigma>0$.

### Language

- [x] Use standard English names for concepts and distributions.
- [x] Avoid literal translations that are not mathematical terms.
- [x] Keep one main term per concept and add aliases only when useful.

### Distribution Notes

Every distribution note should include:

- [x] Definition and notation.
- [x] Parameters and valid values.
- [x] Support.
- [x] PMF or PDF.
- [x] CDF when useful.
- [x] Mean and variance.
- [x] MGF or characteristic function only when correct and useful.
- [x] Relationship with other distributions.
- [x] Modeling assumptions.
- [x] Worked example.
- [x] Common mistakes.
- [x] References.

## Priority 2: Structural Improvements

- [x] Add a note defining a probability space $(\Omega, \mathcal{F}, P)$.
- [x] Add or rewrite a central note for random variables using measurable functions.
- [x] Add a note for independence.
- [x] Add a note for conditional probability.
- [ ] Add a note for expectation as an integral with respect to a probability measure, if studying measure-theoretic probability.
- [x] Add a note for the Central Limit Theorem.
- [x] Add notes for statistical inference: estimation, likelihood, confidence intervals, hypothesis testing, p-values, Type I and Type II errors.
- [x] Add notes for regression and ANOVA if they are part of the review scope.

## Suggested Rewrite Order

1. [[Probability/Sigma-Algebra|Sigma-Álgebra]]
2. Probability space note: create if missing.
3. [[Probability/Random Variable/Random Variable|Variável Aleatória]]
4. [[Probability/Distributions/Continuous/Probability Density|Densidade de Probabilidade]]
5. [[Probability/Distributions/Continuous/Cumulative Distribution Function|Função de Distribuição Acumulada]]
6. [[Probability/Random Variable/Expectation of a Random Variable|Esperança de uma Variável Aleatória]]
7. [[Probability/Random Variable/Variance of a Random Variable|Variância de uma Variável Aleatória]]
8. [[Probability/Random Variable/Moment Generating Functions|Funções Geradoras de Momento]]
9. Discrete distributions.
10. Continuous distributions.
11. Statistical inference topics.
12. Statistical process control topics.

## Reliable Source Standard

Use at least one reliable source per rewritten note.

Good options:

- A course textbook.
- A professor's lecture notes.
- A peer-reviewed reference.
- A standard mathematical statistics textbook.
- Official documentation for computational methods.

Avoid using only AI-generated explanations as the source of truth.

## Final Review Question

Before considering a note trustworthy, answer:

> If I reviewed this note before an exam or project, would it prevent mistakes or accidentally teach me a wrong shortcut?

If the answer is not clearly yes, keep revising.
