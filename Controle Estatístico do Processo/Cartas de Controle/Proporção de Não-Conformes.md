---
dg-publish: true
aliases:
  - p Chart
  - Proportion Nonconforming Chart
---

# p Chart

A p chart monitors sample proportions of nonconforming units.
It charts units classified conforming or nonconforming.[^nist-p-chart]

## Prerequisites

Prerequisites: binomial distribution and control chart basics.

## Process Context

Use p charts when each inspected unit is counted once as conforming or nonconforming.
Sample sizes may vary.

## Definition

For sample \(i\), let \(D_i\) be the number of nonconforming units and \(n_i\) the number inspected. The plotted statistic is:

$$
\hat{p}_i = \frac{D_i}{n_i}.
$$

## Assumptions / Requirements

- Each unit is classified into one of two outcomes.
- Units are independent within and between samples.
- The probability of nonconformance is stable when only common causes are present.
- Sample sizes are large enough for normal-approximation limits to be useful, or exact/binomial methods are considered.

## Notation

| Symbol | Meaning |
|---|---|
| \(D_i\) | Nonconforming units in sample \(i\) |
| \(n_i\) | Inspected units in sample \(i\) |
| \(\hat{p}_i\) | Sample proportion nonconforming |
| \(\bar{p}\) | Pooled estimate of process fraction nonconforming |

## Control Limits / Formula

Estimate:

$$
\bar{p}=\frac{\sum_i D_i}{\sum_i n_i}.
$$

For sample \(i\):

$$
UCL_i=\bar{p}+3\sqrt{\frac{\bar{p}(1-\bar{p})}{n_i}}
$$

$$
CL=\bar{p}
$$

$$
LCL_i=\max\left(0,\bar{p}-3\sqrt{\frac{\bar{p}(1-\bar{p})}{n_i}}\right).
$$

## Interpretation Rules

- Points above the UCL suggest a worse-than-stable nonconforming rate.
- Points below the LCL can signal improvement, inspection changes, or classification changes.
- Variable \(n_i\) means variable limits.
- If \(n_i\) is fixed and counts are easier to communicate, an np chart is equivalent.

## Worked Example

Five samples of 100 units have nonconforming counts \(4,7,5,6,8\). Then \(\bar{p}=30/500=0.06\).

$$
UCL=0.06+3\sqrt{\frac{0.06(0.94)}{100}}=0.1313
$$

$$
LCL=\max(0,0.06-0.0713)=0.
$$

The observed proportions \(0.04,0.07,0.05,0.06,0.08\) are inside the limits.

## Common Mistakes

- Using a p chart for number of defects; use c or u charts for defects.
- Forgetting that changing sample size changes the limits.
- Treating "defective" and "nonconforming" as identical in all contexts.
- Using specification limits as control limits.

## Connections

| Related note | Use |
|---|---|
| [[Número de Não-Conformes|np chart]] | Fixed sample-size count of nonconforming units |
| [[Número de Defeitos|c chart]] | Defect counts, constant opportunity |
| [[Defeitos por Unidade|u chart]] | Defect rates, variable opportunity |
| [[Cartas de Controle|Control charts]] | Attribute chart taxonomy |
| [[Control Limits and Specification Limits]] | Limit distinction |

## References

[^nist-p-chart]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Proportions Control Charts", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm
