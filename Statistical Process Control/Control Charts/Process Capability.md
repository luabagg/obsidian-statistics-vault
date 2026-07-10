---
dg-publish: true
aliases:
  - Process Capability
  - Cp
  - Cpk
---

# Process Capability

Process capability compares stable process variation with specification limits.
It is not a control chart.
Use it only after statistical stability is established.[^nist-capability]

## Prerequisites

Prerequisites: control charts, sample mean, sample standard deviation.

## Process Context

Use capability indices when a process is in control and the question is whether output fits customer, engineering, or regulatory requirements.

## Definition

For a two-sided specification with lower specification limit \(LSL\), upper specification limit \(USL\), process mean \(\mu\), and process standard deviation \(\sigma\):

$$
C_p=\frac{USL-LSL}{6\sigma}
$$

$$
C_{pk}=\min\left(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\right).
$$

\(C_p\) measures potential capability if centered. \(C_{pk}\) includes off-centering.

## Assumptions / Requirements

- The process is stable.
- Observations are independent enough for the estimate used.
- The distribution model is appropriate; the classical formulas assume approximate normality.
- Specification limits are real requirements, not control limits.

## Notation

| Symbol | Meaning |
|---|---|
| \(USL\) | Upper specification limit |
| \(LSL\) | Lower specification limit |
| \(T\) | Target value |
| \(\mu,\sigma\) | Process mean and standard deviation |
| \(\bar{x},s\) | Sample estimates |

## Procedure

1. Verify control-chart stability.
2. Estimate \(\bar{x}\) and \(s\) from representative data.
3. Check distribution shape and measurement system adequacy.
4. Calculate capability.
5. Improve centering or variation if capability is insufficient.

## Worked Example

A shaft has \(LSL=9.90\), \(USL=10.10\), \(\bar{x}=10.03\), and \(s=0.025\).

$$
\hat{C}_p=\frac{10.10-9.90}{6(0.025)}=1.33
$$

$$
\hat{C}_{pk}=\min\left(\frac{10.10-10.03}{3(0.025)},\frac{10.03-9.90}{3(0.025)}\right)=0.93.
$$

The spread could be adequate if centered, but the process mean is too close to the USL.

## Common Mistakes

- Calculating capability from unstable data.
- Reporting only \(C_p\) when the process is off-center.
- Confusing LSL/USL with LCL/UCL.
- Assuming normal capability formulas are valid for strongly nonnormal data.

## Connections

| Related note | Use |
|---|---|
| [[Control Limits and Specification Limits]] | Required distinction |
| [[Control Charts|Control charts]] | Stability prerequisite |
| [[Quadratic Loss Function|Quadratic loss function]] | Target-centered quality |
| [[Common-Cause and Special-Cause Variation]] | Stability interpretation |

## References

[^nist-capability]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What is Process Capability?", https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm
