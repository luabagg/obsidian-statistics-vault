---
dg-publish: true
aliases:
  - Control Charts
  - Shewhart Charts
---

# Control Charts

Control charts plot time-ordered statistics with center lines and statistical control limits.
They monitor whether process behavior remains stable or shows evidence of special-cause variation.[^nist-control-charts]

## Prerequisites

Prerequisites: SPC overview and basic descriptive statistics.

## Definition

Most Shewhart charts use center lines for in-control process levels.
Upper and lower control limits surround those center lines.
Points outside limits, or nonrandom patterns inside limits, signal assignable-cause investigation.

## Control Limits vs Specification Limits

Control limits come from process behavior. Specification limits come from design, customer, regulation, or engineering requirements. A process can be in control and still unacceptable when its stable output does not fit specifications.[^nist-unacceptable]

## Selection Guide

| Data | Sampling condition | Chart |
|---|---|---|
| Variable measurement | Individual observations | [[Valores Individuais e Amplitude Móvel|I-MR / X-MR]] |
| Variable measurement | Rational subgroups, usually size 2-10 | [[Média e Amplitude|Xbar-R]] |
| Variable measurement | Rational subgroups, usually larger than 10 | [[Média e Desvio Padrão|Xbar-S]] |
| Attribute: fraction nonconforming | Variable or fixed inspected sample size | [[Proporção de Não-Conformes|p chart]] |
| Attribute: number nonconforming | Fixed inspected sample size | [[Número de Não-Conformes|np chart]] |
| Attribute: defect count | Constant inspection unit | [[Número de Defeitos|c chart]] |
| Attribute: defects per unit | Variable inspection unit size | [[Defeitos por Unidade|u chart]] |

## Assumptions / Requirements

- Data are ordered by production or observation time.
- Sampling is defined before interpretation.
- Subgroups, when used, are rational: variation within a subgroup should represent short-term common-cause variation.
- Control limits are estimated from stable Phase I data or a justified standard value.
- Special-cause signals trigger investigation, not automatic tampering.

## Worked Example

Daily complaint counts are tracked in one call center.
When handled-call volume is roughly constant, a c chart may be reasonable.
When call volume changes by day, use a u chart or model the rate because complaint opportunity changes.

## Common Mistakes

- Choosing a chart by habit instead of data type.
- Using Xbar-R for individual observations.
- Using a p chart for defect counts per unit.
- Recomputing limits after every signal without investigating the cause.
- Treating points inside limits as proof that the process is acceptable to customers.

## Connections

| Related note | Use |
|---|---|
| [[Common-Cause and Special-Cause Variation]] | Signal interpretation |
| [[Control Limits and Specification Limits]] | Limits distinction |
| [[Valores Individuais e Amplitude Móvel|I-MR / X-MR chart]] | Individuals data |
| [[Média e Amplitude|Xbar-R chart]] | Mean and range |
| [[Média e Desvio Padrão|Xbar-S chart]] | Mean and standard deviation |
| [[Para Dados Autocorrelacionados|Autocorrelated data]] | When independence fails |
| [[Capacidade do Processo|Process capability]] | After stability |

## References

[^nist-control-charts]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What are Control Charts?", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm
[^nist-unacceptable]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "What to do if In Control but Unacceptable?", https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc15.htm
