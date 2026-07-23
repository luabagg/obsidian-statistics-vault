---
dg-publish: true
dg-show-local-graph: true
tags:
  - spc
  - statistics
  - hub
aliases:
  - Statistical Process Control
  - SPC
  - CEP
---

%% Begin Waypoint %%
- **[[Statistical Process Control]]**
	- **[[Control Charts]]**
	- **[[Quadratic Loss Function]]**
	- **[[Quality Tools]]**
	- [[What is SPC]]
%% End Waypoint %%

# Statistical Process Control

Statistical process control (SPC) uses data over time to decide whether a process is stable, predictable, and worth improving. Its central idea is not "meet the specification every time"; it is "separate routine process noise from evidence that the process changed."[^nist-control]

## Prerequisites

Prerequisites: basic descriptive statistics and sampling.

## Core Ideas

- Process systems combine inputs, equipment, methods, measurements, people, and environment to produce output.
- Common-cause variation is the routine variation built into a stable process.
- Special-cause variation is evidence that a nonroutine source changed the process.
- Control limits are statistical limits estimated from process data.
- Specification limits are engineering, customer, or regulatory requirements.
- Capability is assessed only after the process is statistically stable.

## Typical Workflow

1. Define the quality characteristic, unit, sampling plan, and business decision.
2. Choose the chart from the data type and rational subgrouping.
3. Estimate control limits from stable Phase I data.
4. Investigate special-cause signals instead of adjusting every point.
5. After stability, compare process output to specification limits.
6. Improve centering, variation, measurement, or process design.

## Chart Taxonomy

| Data and sampling | Correct chart family |
|---|---|
| One measurement at a time | Individuals and moving range: I-MR or X-MR |
| Variable data in small rational subgroups | Xbar-R for subgroup mean and range |
| Variable data in larger rational subgroups | Xbar-S for subgroup mean and standard deviation |
| Attribute data: nonconforming proportion | p chart |
| Attribute data: number nonconforming with fixed sample size | np chart |
| Attribute data: nonconformities per constant inspection unit | c chart |
| Attribute data: nonconformities per variable inspection unit | u chart |

## Worked Example

A machining cell records one shaft diameter per hour. Because there is no rational subgroup at each hour, the correct starting chart is I-MR, not Xbar-R. If the chart shows no special-cause signal, capability can then compare the stable diameter distribution with the lower and upper specification limits.

## Common Mistakes

- Treating specification limits as if they were control limits.
- Treating every high or low point like justification for process adjustment.
- Calculating capability before the control chart shows statistical stability.
- Using Xbar-R when the data are individual observations.
- Mixing defective units and defects; those require different attribute charts.

## Connections

| Related note | Use |
|---|---|
| [[What is SPC|What is SPC]] | Plain-language overview |
| [[Common-Cause and Special-Cause Variation]] | Variation taxonomy |
| [[Control Limits and Specification Limits]] | Limit taxonomy |
| [[Control Charts|Control charts]] | Chart selection |
| [[Process Capability|Process capability]] | Stable-process specification comparison |
| [[Quality Tools|Quality tools]] | Diagnostic tools around SPC |

## References

[^nist-control]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Process or Product Monitoring and Control", https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm
