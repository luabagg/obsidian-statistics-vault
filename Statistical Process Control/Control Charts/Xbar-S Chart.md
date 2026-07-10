---
dg-publish: true
aliases:
  - Xbar-S Chart
  - X-bar S Chart
  - Mean and Standard Deviation Chart
---

# Xbar-S Chart

An Xbar-S chart monitors a variable process characteristic with rational subgroups. It uses subgroup means for location and subgroup standard deviations for short-term variation.[^nist-xbar-s]

## Prerequisites

Prerequisites: control chart basics, sample standard deviation, rational subgrouping.

## Process Context

Use Xbar-S when subgroup standard deviations are more appropriate than ranges, especially for larger subgroups. NIST notes that range charts are usually satisfactory for small subgroup sizes, while standard deviations are preferable for larger subgroup sizes.[^nist-xbar-s]

## Definition

For subgroup \(i\), compute \(\bar{x}_i\) and sample standard deviation \(s_i\). The S chart checks whether short-term variation is stable; the Xbar chart checks whether subgroup means are stable.

## Assumptions / Requirements

- Variable measurement data.
- Rational subgroups with a consistent subgroup size for the constants used.
- Independent subgroups over time.
- Approximate within-subgroup normality for standard constants.
- Stable S chart before strong conclusions from Xbar chart.

## Notation

| Symbol | Meaning |
|---|---|
| \(n\) | Subgroup size |
| \(\bar{x}_i\) | Mean of subgroup \(i\) |
| \(s_i\) | Sample standard deviation of subgroup \(i\) |
| \(\bar{\bar{x}}\) | Average of subgroup means |
| \(\bar{s}\) | Average of subgroup standard deviations |
| \(A_3,B_3,B_4\) | Control chart constants based on \(n\) |

## Control Limits / Formula

For equal subgroup size:

$$
\begin{aligned}
UCL_{\bar{X}} &= \bar{\bar{x}} + A_3\bar{s}, &
CL_{\bar{X}} &= \bar{\bar{x}}, &
LCL_{\bar{X}} &= \bar{\bar{x}} - A_3\bar{s}, \\
UCL_S &= B_4\bar{s}, &
CL_S &= \bar{s}, &
LCL_S &= B_3\bar{s}.
\end{aligned}
$$

For \(n=5\), common constants are \(A_3=1.427\), \(B_3=0\), and \(B_4=2.089\).[^montgomery-spc]

## Interpretation Rules

- Read the S chart first.
- Investigate points outside limits and nonrandom patterns.
- A low S chart signal can matter; it may indicate stratification, rounding, or measurement changes.
- Capability calculations wait until both charts support stability.

## Worked Example

Four subgroups of size \(n=5\) have means \(10.02, 9.98, 10.05, 10.00\) and standard deviations \(0.04, 0.05, 0.03, 0.06\). Then \(\bar{\bar{x}}=10.0125\) and \(\bar{s}=0.045\).

$$
UCL_{\bar{X}}=10.0125+1.427(0.045)=10.0767
$$

$$
LCL_{\bar{X}}=10.0125-1.427(0.045)=9.9483
$$

$$
UCL_S=2.089(0.045)=0.0940,\qquad LCL_S=0.
$$

All example values are inside the limits, so the example has no control-limit signal.

## Common Mistakes

- Using Xbar-S only because it sounds more precise when subgroups are very small.
- Interpreting the Xbar chart before checking the S chart.
- Mixing unequal subgroup sizes without recalculating appropriate limits.
- Treating stable charts like proof that specifications are met.

## Connections

| Related note | Use |
|---|---|
| [[Control Charts|Control charts]] | Chart selection |
| [[Xbar-R Chart|Xbar-R chart]] | Alternative using ranges |
| [[Control Limits and Specification Limits]] | Avoid limit confusion |
| [[Process Capability|Process capability]] | Specification comparison after stability |

## References

[^nist-xbar-s]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Shewhart X-bar and R and S Control Charts", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm
[^montgomery-spc]: Douglas C. Montgomery, *Introduction to Statistical Quality Control*, 8th ed., Wiley, ISBN 978-1-119-39930-8.
