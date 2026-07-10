---
dg-publish: true
aliases:
  - What is SPC
  - What is CEP
  - SPC overview
---

# What Is Statistical Process Control?

Statistical process control is disciplined monitoring with time-ordered data.
It asks whether current data still look like they came from the same stable process used to set chart limits.[^nist-process-control]

## Prerequisites

Prerequisites: none.

## Definition

SPC combines:

- Control: act on a process only when evidence supports action.
- Statistics: use data, variation, and probability instead of isolated impressions.
- Process thinking: treat output like the result of system causes.

SPC is useful because it prevents two costly errors: ignoring real process changes and overreacting to common-cause variation.

## What SPC Does

- Detects special-cause signals early.
- Supports operator-level monitoring with clear escalation rules.
- Makes improvement work more targeted.
- Provides a stability requirement before process capability studies.
- Helps distinguish process behavior from customer or engineering specifications.

## Implementation Notes

- Start with the few characteristics that matter most to customers or safety.
- Define an out-of-control action plan before collecting chart data.
- Use charts where action is possible; charting without response wastes attention.
- Use Quality Function Deployment only for planning bridges from customer needs to process characteristics, not instead of control charts.

```image-layout-a
![[matriz-de-qualidade.webp]]
![[exemplo-matriz-qualidade.webp]]
```

## Worked Example

A brake rotor producer wants to monitor rotor thickness. SPC starts by defining the measurement method, sampling frequency, and chart type. If one rotor is measured every 30 minutes, use an I-MR chart; if five consecutive rotors are sampled from the same short production run, use Xbar-R.

## Common Mistakes

- Starting with many charts instead of a few actionable characteristics.
- Calling a process "good" because it is stable even when it misses specifications.
- Calling process behavior "bad" because one value is near a specification limit while chart behavior remains stable.
- Adding QFD matrices without connecting them to measurable control characteristics.

## Connections

| Related note | Use |
|---|---|
| [[Statistical Process Control|Statistical Process Control]] | Main hub |
| [[Control Charts|Control charts]] | Monitoring method |
| [[Control Limits and Specification Limits]] | Required distinction |
| [[Common-Cause and Special-Cause Variation]] | Required variation language |
| [[Quality Tools|Quality tools]] | Problem exploration tools |

## References

[^nist-process-control]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What is Process Control?", https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc13.htm
