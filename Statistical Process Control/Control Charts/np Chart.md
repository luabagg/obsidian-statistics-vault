---
dg-publish: true
aliases:
  - np Chart
  - Number Nonconforming Chart
---

# np Chart

An np chart monitors the number of nonconforming units in samples of constant size. It is the count-scale companion to the p chart.[^montgomery-np]

## Prerequisites

Prerequisites: binomial distribution and p chart logic.

## Process Context

Use an np chart when each sample has the same inspected size $n$ and the audience should see counts rather than proportions.

## Definition

For sample $i$, plot $D_i$, the number of nonconforming units. Under stable conditions, $D_i$ is modeled as binomial with parameters $n$ and $p$.

## Assumptions / Requirements

- Fixed sample size $n$.
- Each unit has two possible classifications.
- Unit classifications are independent.
- The probability $p$ is stable when only common causes are present.

## Notation

| Symbol | Meaning |
|---|---|
| $D_i$ | Nonconforming units in sample $i$ |
| $n$ | Fixed inspected sample size |
| $\bar{p}$ | Pooled estimate of fraction nonconforming |

## Control Limits / Formula

$$
CL_{np}=n\bar{p}
$$

$$
UCL_{np}=n\bar{p}+3\sqrt{n\bar{p}(1-\bar{p})}
$$

$$
LCL_{np}=\max\left(0,n\bar{p}-3\sqrt{n\bar{p}(1-\bar{p})}\right).
$$

## Interpretation Rules

- A high point signals more nonconforming units than expected from stable variation.
- Low points can signal improvement or changed inspection/classification.
- If sample size varies, use a p chart instead.

## Worked Example

Five samples of $n=100$ units have nonconforming counts $4,7,5,6,8$. The pooled estimate is $\bar{p}=0.06$, so $CL=6$.

$$
UCL=6+3\sqrt{100(0.06)(0.94)}=13.13
$$

$$
LCL=\max(0,6-7.13)=0.
$$

All five counts are within the chart limits.

## Common Mistakes

- Using an np chart when sample sizes vary.
- Plotting defects instead of nonconforming units.
- Forgetting that one nonconforming unit may contain many defects.
- Replacing control limits with accept/reject specifications.

## Connections

| Related note | Use |
|---|---|
| [[p Chart|p chart]] | Variable sample size or proportion scale |
| [[c Chart|c chart]] | Defect counts |
| [[Defects per Unit|u chart]] | Defects per unit |
| [[Control Charts|Control charts]] | Chart taxonomy |

## References

[^montgomery-np]: Douglas C. Montgomery, *Introduction to Statistical Quality Control*, 8th ed., Wiley, ISBN 978-1-119-39930-8.
