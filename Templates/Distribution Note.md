---
dg-publish: false
template: true
tags:
  - template
  - probability
  - distribution
aliases: []
---

# {{title}}

## Summary

Describe what this distribution models and when it is useful.

## Definition

State the distribution and its notation.

Example:

$$
X \sim <Distribution>(<parameters>)
$$

## Parameters

| Parameter | Meaning | Valid Values |
|---|---|---|
| `<parameter>` | `<meaning>` | `<domain>` |

## Support

State the possible values of $X$.

$$
\operatorname{supp}(X) = <support>
$$

## Probability Function

Use one of the following, depending on the distribution.

### PMF

For discrete distributions:

$$
p_X(x) = P(X = x) = <formula>
$$

### PDF

For continuous distributions:

$$
f_X(x) = <formula>
$$

## CDF

$$
F_X(x) = P(X \leq x) = <formula>
$$

## Moments

| Quantity | Formula |
|---|---|
| Mean | $E[X] = <formula>$ |
| Variance | $\operatorname{Var}(X) = <formula>$ |
| Standard deviation | $\sigma_X = <formula>$ |

## Generating Functions

Include only if useful and correct.

### Moment Generating Function

$$
M_X(t) = E[e^{tX}] = <formula>
$$

State the values of $t$ where it exists.

### Characteristic Function

$$
\varphi_X(t) = E[e^{itX}] = <formula>
$$

## Relationships With Other Distributions

- `<relationship>`

## Assumptions / Modeling Conditions

- `<assumption>`

## Worked Example

### Problem

State the problem.

### Solution

Show parameter identification, formula choice, substitution, and result.

### Interpretation

Explain the probability or statistic in context.

## Common Mistakes

- Confusing PMF and PDF.
- Forgetting the support.
- Mixing parameterizations without stating them.
- Claiming symmetry without checking the shape.

## Connections

- Related notes: [[<related-note>]]
- Prerequisites: [[Função de Distribuição Acumulada]], [[Densidade de Probabilidade]]
- Used in: [[<application-note>]]

## References

- `<book, article, lecture note, or URL>`

## Review Checklist

- [ ] Parameters and support are explicit.
- [ ] PMF/PDF integrates or sums to 1.
- [ ] Mean and variance match a reliable source.
- [ ] MGF uses the same parameterization as the PDF/PMF.
- [ ] Symmetry/skewness claims are correct.
- [ ] Worked example checks assumptions and units.
- [ ] References are included.
