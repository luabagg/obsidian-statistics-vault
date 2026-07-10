---
dg-publish: true
aliases:
  - u Chart
  - Defects per Unit Chart
---

# u Chart

A u chart monitors nonconformities per unit when the number of inspected units or the opportunity for defects changes by sample. It is the rate-scale companion to the c chart.[^montgomery-u]

## Prerequisites

Prerequisites: Poisson distribution, c chart logic.

## Process Context

Use a u chart when defect counts are collected over samples with different sizes, areas, lengths, forms, or exposure.

## Definition

For sample \(i\), let \(c_i\) be the number of defects and \(n_i\) the number of inspection units. Plot:

$$
u_i=\frac{c_i}{n_i}.
$$

## Assumptions / Requirements

- Defects are countable events.
- Inspection unit size \(n_i\) is known for each sample.
- Defects follow an approximately Poisson count model under stable conditions.
- Differences in opportunity are represented by \(n_i\).

## Notation

| Symbol | Meaning |
|---|---|
| \(c_i\) | Defects in sample \(i\) |
| \(n_i\) | Inspection units in sample \(i\) |
| \(u_i\) | Defects per unit in sample \(i\) |
| \(\bar{u}\) | Pooled defects per unit |

## Control Limits / Formula

$$
\bar{u}=\frac{\sum_i c_i}{\sum_i n_i}
$$

For sample \(i\):

$$
UCL_i=\bar{u}+3\sqrt{\frac{\bar{u}}{n_i}}
$$

$$
CL=\bar{u}
$$

$$
LCL_i=\max\left(0,\bar{u}-3\sqrt{\frac{\bar{u}}{n_i}}\right).
$$

## Interpretation Rules

- Larger \(n_i\) gives narrower limits because the rate is estimated more precisely.
- High points signal unusual defect rates, not high raw counts.
- If \(n_i\) is constant, a c chart may communicate more simply.

## Worked Example

Three lots inspect \(5,4,6\) units and find \(4,5,3\) defects. Then \(\bar{u}=12/15=0.8\). For the first lot:

$$
UCL_1=0.8+3\sqrt{\frac{0.8}{5}}=2.0
$$

$$
LCL_1=\max(0,0.8-1.2)=0.
$$

The first plotted value is \(u_1=4/5=0.8\), exactly on the center line.

## Common Mistakes

- Plotting raw defect counts when opportunity changes.
- Using a u chart for nonconforming units instead of defects.
- Forgetting that limits differ by sample size.
- Ignoring changes in inspection intensity or defect definition.

## Connections

| Related note | Use |
|---|---|
| [[Número de Defeitos|c chart]] | Constant inspection unit |
| [[Proporção de Não-Conformes|p chart]] | Nonconforming proportions |
| [[Número de Não-Conformes|np chart]] | Nonconforming counts |
| [[Cartas de Controle|Control charts]] | Attribute chart taxonomy |

## References

[^montgomery-u]: Douglas C. Montgomery, *Introduction to Statistical Quality Control*, 8th ed., Wiley, ISBN 978-1-119-39930-8.
