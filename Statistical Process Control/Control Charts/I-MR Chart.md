---
dg-publish: true
aliases:
  - I-MR Chart
  - X-MR Chart
  - Individuals and Moving Range Chart
---

# I-MR / X-MR Chart

An I-MR chart monitors individual measurements and their moving ranges. It is the correct Shewhart chart when each time point has one observation rather than a rational subgroup.[^nist-imr]

## Prerequisites

Prerequisites: control chart basics and ordered observations.

## Process Context

Use I-MR for low-volume production, destructive tests, long cycle times, administrative processes, or any setting where subgrouping is not meaningful.

## Definition

The individuals chart plots \(x_i\). The moving range chart plots the absolute difference between consecutive observations:

$$
MR_i = |x_i - x_{i-1}|.
$$

## Assumptions / Requirements

- One observation per time point.
- Consecutive observations are meaningful for estimating short-term variation.
- The process is not strongly autocorrelated.
- Measurement resolution is adequate.
- Phase I data are screened for special causes before final limits are used.

## Notation

| Symbol | Meaning |
|---|---|
| \(x_i\) | Individual observation at time \(i\) |
| \(\bar{x}\) | Average of individual observations |
| \(MR_i\) | Moving range between \(x_i\) and \(x_{i-1}\) |
| \(\overline{MR}\) | Average moving range |
| \(d_2\) | Range constant, \(1.128\) for moving ranges of length 2 |

## Control Limits / Formula

For the individuals chart:

$$
UCL_X = \bar{x} + 3\frac{\overline{MR}}{1.128}
      = \bar{x} + 2.66\overline{MR}
$$

$$
CL_X = \bar{x}
$$

$$
LCL_X = \bar{x} - 2.66\overline{MR}.
$$

For the moving range chart with range length 2:

$$
UCL_{MR}=3.267\overline{MR},\qquad CL_{MR}=\overline{MR},\qquad LCL_{MR}=0.
$$

## Interpretation Rules

- Check the moving range chart for unstable short-term variation.
- Investigate individual points outside limits and nonrandom patterns.
- If autocorrelation is visible, use a time-series or residual approach instead of naive I-MR limits.
- Never use specification limits like chart limits.

## Worked Example

Five individual measurements are \(10.1, 9.9, 10.3, 10.2, 10.0\). Then \(\bar{x}=10.10\), moving ranges are \(0.2, 0.4, 0.1, 0.2\), and \(\overline{MR}=0.225\).

$$
UCL_X=10.10+2.66(0.225)=10.6985
$$

$$
LCL_X=10.10-2.66(0.225)=9.5015
$$

$$
UCL_{MR}=3.267(0.225)=0.7351.
$$

No listed point or moving range exceeds these limits.

## Common Mistakes

- Calling an individuals chart an Xbar chart.
- Creating artificial subgroups after the fact.
- Ignoring autocorrelation from automated or continuous processes.
- Using a moving range when consecutive observations are not comparable.

## Connections

| Related note | Use |
|---|---|
| [[Control Charts|Control charts]] | Chart selection |
| [[Xbar-R Chart|Xbar-R chart]] | True subgroup chart |
| [[Autocorrelated Data|Autocorrelated data]] | When I-MR assumptions fail |
| [[Control Limits and Specification Limits]] | Avoid limit confusion |

## References

[^nist-imr]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Individuals Control Charts", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm
