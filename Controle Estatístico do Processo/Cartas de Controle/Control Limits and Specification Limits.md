---
dg-publish: true
aliases:
  - Control Limits vs Specification Limits
  - Specification Limits
  - Control Limits
---

# Control Limits and Specification Limits

Control limits and specification limits answer different questions. Control limits ask whether the process changed; specification limits ask whether output satisfies requirements.[^nist-control-limits]

## Prerequisites

Prerequisites: control chart basics.

## Definition

Control limits are statistical boundaries computed from the process data or from an approved standard process parameter. Specification limits are external requirements such as lower specification limit (LSL), upper specification limit (USL), target value, tolerance, or acceptance criterion.

## Key Distinction

| Limit type | Source | Used for | Should change when |
|---|---|---|---|
| Control limits | Process behavior | Detecting special causes | The stable process changes or Phase I analysis is revised |
| Specification limits | Customer, design, regulation, engineering | Judging conformance and capability | Requirements change |

## Worked Example

A stable process has \(\bar{x}=10.00\), \(\hat{\sigma}=0.10\), so approximate individuals control limits are \(9.70\) and \(10.30\). The drawing specification is \(9.90\) to \(10.10\). The process can be statistically stable while producing too many parts outside specification; stability does not imply capability.

## Common Mistakes

- Drawing specification limits on a control chart and calling them UCL/LCL.
- Widening control limits to reduce alarms.
- Narrowing control limits to match customer tolerance.
- Running capability studies before stability is established.

## Connections

| Related note | Use |
|---|---|
| [[Cartas de Controle|Control charts]] | Where control limits are used |
| [[Capacidade do Processo|Process capability]] | Where specification limits are used |
| [[Common-Cause and Special-Cause Variation]] | Signal interpretation |
| [[Controle Estatístico do Processo|Statistical Process Control]] | Main hub |

## References

[^nist-control-limits]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What are Control Charts?" and "What is Process Capability?", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm
