---
dg-publish: true
aliases:
  - Quadratic Loss Function
  - Taguchi Loss Function
---

# Quadratic Loss Function

The quadratic loss function models quality loss increasing with squared distance from the target.
Loss can exist even when an item is inside specification limits.
This supports the SPC goal of reducing target variation, not merely sorting good from bad at tolerance boundaries.[^taguchi-loss]

## Prerequisites

Prerequisites: target value, specification limits, process variation.

## Definition

For measured value \(y\), target \(T\), and proportionality constant \(k\):

$$
L(y)=k(y-T)^2.
$$

The constant \(k\) converts squared deviation into money, warranty cost, performance loss, or another loss scale.

## Assumptions / Requirements

- The target value is meaningful.
- Loss increases symmetrically when \(y\) moves away from \(T\), unless asymmetric loss is justified.
- The cost at a known deviation can be used to estimate \(k\).
- Specification limits remain requirements; the loss function does not replace conformance decisions.

## Notation

| Symbol | Meaning |
|---|---|
| \(y\) | Observed quality characteristic |
| \(T\) | Target or nominal value |
| \(L(y)\) | Loss at value \(y\) |
| \(k\) | Loss constant |

## Worked Example

Rotor thickness target is \(T=2.00\) mm.
Deviation of \(0.10\) mm is estimated to cost 20 monetary units, so:

$$
k=\frac{20}{0.10^2}=2000.
$$

If one rotor measures \(2.04\) mm:

$$
L(2.04)=2000(2.04-2.00)^2=3.2.
$$

The part may still be inside specification, but it is not loss-free.

## Interpretation

- Lower variation around the target reduces expected loss.
- Centering matters even when capability spread looks acceptable.
- The function supports continuous improvement rather than threshold-only thinking.

## Common Mistakes

- Treating all in-spec values as equally good.
- Using Taguchi loss without defining \(k\).
- Ignoring asymmetric customer loss when one side of the target is more costly.
- Confusing target value with control-chart center line.

## Connections

| Related note | Use |
|---|---|
| [[Process Capability|Process capability]] | Capability and target centering |
| [[Control Limits and Specification Limits]] | Specification distinction |
| [[Statistical Process Control|Statistical Process Control]] | Variation reduction context |
| [[Common-Cause and Special-Cause Variation]] | Process improvement logic |

## References

[^taguchi-loss]: Genichi Taguchi, Elsayed A. Elsayed, and Thomas Hsiang, *Quality Engineering in Production Systems*, McGraw-Hill, ISBN 978-0-07-062830-2.
