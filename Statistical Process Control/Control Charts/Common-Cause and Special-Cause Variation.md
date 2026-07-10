---
dg-publish: true
aliases:
  - Common Cause Variation
  - Special Cause Variation
  - Assignable Cause
---

# Common-Cause and Special-Cause Variation

SPC separates common-cause variation from special-cause variation. This distinction decides whether to improve the system or investigate a specific change.[^nist-out-control]

## Prerequisites

Prerequisites: control chart basics.

## Definition

Common-cause variation is the routine variation produced by the current stable system. Special-cause variation is evidence that the current point or pattern likely came from a different source than the stable system used to set the limits.

## Interpretation

| Variation type | Meaning | Proper response |
|---|---|---|
| Common cause | Predictable process noise | Improve the system: method, equipment, material, training, measurement |
| Special cause | Assignable change or unusual event | Investigate, contain, correct, and prevent recurrence |

## Worked Example

One filling-process bottle volume sits slightly above the center line but inside limits.
That is not enough evidence for adjustment.
Later, one point exceeds the UCL after nozzle replacement.
That special-cause signal should trigger the out-of-control action plan.

## Common Mistakes

- Adjusting the process after every common-cause fluctuation.
- Ignoring a point outside limits because the product still meets specification.
- Calling all variation "random" and skipping investigation.
- Treating stable but off-target output like acceptable output.

## Connections

| Related note | Use |
|---|---|
| [[Control Charts|Control charts]] | Signal detection |
| [[Control Limits and Specification Limits]] | Limit distinction |
| [[Quality Tools|Quality tools]] | Cause investigation |
| [[Process Capability|Process capability]] | Stable-process capability |

## References

[^nist-out-control]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What to do if the process is Out of Control?", https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc14.htm
