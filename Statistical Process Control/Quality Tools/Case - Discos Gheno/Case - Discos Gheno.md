---
dg-publish: true
dg-show-local-graph: true
tags:
  - spc
  - quality-tools
  - case-study
aliases:
  - Discos Gheno Case
  - GHENOrtrs Case
---

%% Begin Waypoint %%
- **[[Case - Discos Gheno]]**
	- **[[Process Flowchart]]**
%% End Waypoint %%

# Discos Gheno Case

This case maps the process for producing GHENOrtrs downhill bicycle brake rotors and uses quality tools to frame one likely business/process problem. The note is an application index; theory stays in the linked concept notes.[^montgomery-tools-case]

## Prerequisites

Prerequisites: quality tools and SPC basics.

## Process Context

```image-layout-a
![[catálogo-GHENOrtrs.webp]]
![[disco-em-roda-traseira.webp]]
```

The product is a bicycle brake rotor. The case artifacts show product design, material purchase, prototyping, testing, production, marketing, sales, and post-sale feedback.

## Process Map

| Diagram | Purpose |
|---|---|
| [[Process Flowchart.excalidraw]] | Whole process |
| [[Part 1 - Design.excalidraw]] | Design |
| [[Part 2 - Material Purchase.excalidraw]] | Material purchasing |
| [[Part 3 - Prototyping.excalidraw]] | Prototyping |
| [[Part 4 - Prototype Testing.excalidraw]] | Prototype testing |
| [[Part 5 - Production.excalidraw]] | Production |
| [[Part 6 - Marketing Sales and After-sales.excalidraw]] | Market and post-sale loop |

## Cause Investigation

The selected problem is insufficient market pre-validation before committing to production. The cause-and-effect diagram is stored separately:

| Diagram |
|---|
| ![[Cause and Effect Diagram.excalidraw]] |

## Force-Field Summary

| Driving forces | Restraining forces |
|---|---|
| Conduct market research | Technical uncertainty |
| Validate the product with target riders | Design difficulty |
| Study competitors | High prototyping cost |
| Define pricing method | Low market influence |

## SPC Follow-Up

Useful measurable characteristics for future SPC work:

- Rotor thickness or runout as variable measurements.
- Surface defect counts per rotor for c or u chart candidates.
- Final-inspection failure proportion for p chart candidates.
- Customer complaint rate after sale as an attribute or time-series monitoring candidate.

## Common Mistakes

- Duplicating control-chart theory inside a case note.
- Treating diagrams as evidence without measurement data.
- Choosing corrective action from one possible cause without verification.
- Choosing SPC metrics that the team cannot act on.

## Connections

| Related note | Use |
|---|---|
| [[Quality Tools|Quality tools]] | Tool definitions |
| [[Control Charts|Control charts]] | Candidate monitoring charts |
| [[p Chart|p chart]] | Final inspection proportion |
| [[c Chart|c chart]] | Defect counts per constant unit |
| [[Defects per Unit|u chart]] | Defects with variable opportunity |
| [[Control Limits and Specification Limits]] | Keep requirements separate from signals |

## References

[^montgomery-tools-case]: Douglas C. Montgomery, *Introduction to Statistical Quality Control*, 8th ed., Wiley, ISBN 978-1-119-39930-8.
