---
dg-publish: true
aliases:
  - Xbar-R Chart
  - X-bar R Chart
  - Mean and Range Chart
---

# Xbar-R Chart

An Xbar-R chart monitors a variable process characteristic using rational subgroups. The Xbar chart monitors subgroup means, and the R chart monitors subgroup ranges.[^nist-xbar-r]

## Prerequisites

Prerequisites: control chart basics and rational subgrouping.

## Process Context

Use Xbar-R when each plotted point summarizes a small subgroup, commonly 2 to 10 observations, collected close enough in time that within-subgroup variation represents short-term common-cause variation.

## Definition

For subgroup \(i\) with size \(n\), the subgroup mean is \(\bar{x}_i\) and the subgroup range is \(R_i = x_{i,\max} - x_{i,\min}\). The chart pair is interpreted together: first check the R chart for stable short-term variation, then interpret the Xbar chart.

## Assumptions / Requirements

- Variable measurement data.
- Same subgroup size for the constants shown below.
- Independent subgroups in time.
- Approximate normality is most important for small-sample probability interpretation.
- Rational subgrouping is defensible.

## Notation

| Symbol | Meaning |
|---|---|
| \(n\) | Subgroup size |
| \(\bar{x}_i\) | Mean of subgroup \(i\) |
| \(R_i\) | Range of subgroup \(i\) |
| \(\bar{\bar{x}}\) | Average of subgroup means |
| \(\bar{R}\) | Average of subgroup ranges |
| \(A_2,D_3,D_4\) | Control chart constants based on \(n\) |

## Control Limits / Formula

For equal subgroup size:

$$
\begin{aligned}
UCL_{\bar{X}} &= \bar{\bar{x}} + A_2\bar{R}, &
CL_{\bar{X}} &= \bar{\bar{x}}, &
LCL_{\bar{X}} &= \bar{\bar{x}} - A_2\bar{R}, \\
UCL_R &= D_4\bar{R}, &
CL_R &= \bar{R}, &
LCL_R &= D_3\bar{R}.
\end{aligned}
$$

For \(n=5\), common constants are \(A_2=0.577\), \(D_3=0\), and \(D_4=2.115\).[^nist-xbar-r]

## Interpretation Rules

- Investigate any point outside control limits.
- Investigate nonrandom patterns, especially runs, trends, or cycles.
- If the R chart is unstable, never interpret Xbar shifts like stable mean behavior.
- Do not compare points to specification limits on the control chart.

## Worked Example

Four subgroups of size \(n=5\) have means \(10.02, 9.98, 10.05, 10.00\) and ranges \(0.12, 0.15, 0.10, 0.13\). Then \(\bar{\bar{x}}=10.0125\) and \(\bar{R}=0.125\).

$$
UCL_{\bar{X}}=10.0125+0.577(0.125)=10.0846
$$

$$
LCL_{\bar{X}}=10.0125-0.577(0.125)=9.9404
$$

$$
UCL_R=2.115(0.125)=0.2644,\qquad LCL_R=0.
$$

All listed subgroup means and ranges are inside these limits, so this small example shows no control-limit signal.

## Common Mistakes

- Using Xbar-R for one observation at a time.
- Ignoring the R chart and interpreting only the Xbar chart.
- Forming subgroups from mixed machines, shifts, or materials when the goal is short-term variation.
- Using specification limits as the Xbar chart limits.

## Connections

| Related note | Use |
|---|---|
| [[Cartas de Controle|Control charts]] | Chart selection |
| [[Média e Desvio Padrão|Xbar-S chart]] | Alternative using subgroup standard deviations |
| [[Valores Individuais e Amplitude Móvel|I-MR / X-MR chart]] | Individual observations |
| [[Control Limits and Specification Limits]] | Avoid limit confusion |
| [[Capacidade do Processo|Process capability]] | After stable control |

## References

[^nist-xbar-r]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Shewhart X-bar and R and S Control Charts", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm
