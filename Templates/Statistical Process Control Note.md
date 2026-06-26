---
dg-publish: false
template: true
tags:
  - template
  - statistical-process-control
aliases: []
---

# {{title}}

## Summary

Explain the SPC concept, tool, chart, or method in 2-4 sentences.

## Process Context

Describe the process, quality characteristic, measurement unit, and objective.

## Definition

Define the SPC concept or chart precisely.

## Data Type

- Variable data: `<continuous measurement>`
- Attribute data: `<count, defect, nonconformity, proportion>`

## Assumptions / Requirements

- Process stability: `<yes/no/condition>`
- Independence: `<condition>`
- Subgrouping: `<rational subgrouping rule>`
- Distributional assumption: `<normal, binomial, Poisson, none, or other>`

## Notation

| Symbol | Meaning |
|---|---|
| `<symbol>` | `<meaning>` |

## Control Limits / Formula

$$
<formula>
$$

## Procedure

1. Collect data using rational subgroups.
2. Estimate the process center and variation.
3. Compute control limits.
4. Plot the statistic over time.
5. Identify signals of special causes.
6. Decide and document the action.

## Interpretation Rules

- Points outside control limits indicate possible special causes.
- Non-random patterns can indicate instability even if points are inside limits.
- Control limits are not the same as specification limits.

## Worked Example

### Problem

State the process and data.

### Solution

Show calculations for center line and limits.

### Interpretation

Explain whether the process appears stable and what action is recommended.

## Common Mistakes

- Confusing control limits with specification limits.
- Adjusting a stable process unnecessarily.
- Ignoring rational subgrouping.
- Calculating capability before checking statistical control.

## Connections

- Related notes: [[Cartas de Controle]], [[Capacidade do Processo]]
- Prerequisites: [[Distribuição Normal]], [[Variância de uma Variável Aleatória]]
- Used in: [[<case-study-note>]]

## References

- `<book, article, standard, lecture note, or URL>`

## Review Checklist

- [ ] Data type is clear.
- [ ] Chart choice matches the data type.
- [ ] Assumptions are stated.
- [ ] Control limits are correct for the chart.
- [ ] Control limits and specification limits are not confused.
- [ ] Interpretation includes an action decision.
- [ ] References are included.
