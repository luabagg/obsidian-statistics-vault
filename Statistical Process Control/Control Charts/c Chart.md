---
dg-publish: true
aliases:
  - c Chart
  - Count of Nonconformities Chart
---

# c Chart

A c chart monitors nonconformity counts, often called defects, in constant inspection units.
It is an attribute chart based on a Poisson count model.[^nist-c-chart]

## Prerequisites

Prerequisites: Poisson distribution and control chart basics.

## Process Context

Use a c chart when the opportunity for defects is essentially constant from sample to sample: same area, same length, same form, same number of units, or same inspection effort.

## Definition

The plotted value \(c_i\) is the count of nonconformities in inspection unit \(i\). A unit can have more than one nonconformity.

## Assumptions / Requirements

- Constant inspection unit size.
- Defects are countable events.
- Events are approximately independent and rare over many opportunities.
- The stable defect rate is constant unless a special cause occurs.

## Notation

| Symbol | Meaning |
|---|---|
| \(c_i\) | Defects in inspection unit \(i\) |
| \(\bar{c}\) | Average defect count per inspection unit |

## Control Limits / Formula

$$
UCL_c=\bar{c}+3\sqrt{\bar{c}}
$$

$$
CL_c=\bar{c}
$$

$$
LCL_c=\max(0,\bar{c}-3\sqrt{\bar{c}}).
$$

## Interpretation Rules

- A high point means more defects than expected from stable Poisson variation.
- Low points can indicate improvement or changed inspection methods.
- If inspection unit size changes, use a u chart.

## Worked Example

Five equal-area panels have defect counts \(3,5,2,4,6\). Then \(\bar{c}=4\).

$$
UCL=4+3\sqrt{4}=10
$$

$$
LCL=\max(0,4-6)=0.
$$

All five counts are inside the limits.

## Common Mistakes

- Using a c chart for defective units instead of defects.
- Using a c chart when inspection area or opportunity changes.
- Treating each defect as equally severe without checking whether stratification is needed.
- Forgetting that the LCL is zero when the formula is negative.

## Connections

| Related note | Use |
|---|---|
| [[Defects per Unit|u chart]] | Variable inspection unit size |
| [[p Chart|p chart]] | Nonconforming proportions |
| [[np Chart|np chart]] | Nonconforming counts |
| [[Control Charts|Control charts]] | Attribute chart taxonomy |

## References

[^nist-c-chart]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Counts Control Charts", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc331.htm
