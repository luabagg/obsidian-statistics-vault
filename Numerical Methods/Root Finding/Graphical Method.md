---
dg-publish: true
---

# Graphical Method for Locating Roots

## Summary

The graphical method plots $y=f(x)$ (or $y=g(x)$ and $y=h(x)$ when solving $g(x)=h(x)$) to find approximate intervals where roots occur. It is a scouting tool, not a high-precision solver.

## Prerequisites

- Plotting functions / evaluating sample points
- [[Bolzano's Theorem]] to certify brackets after visual inspection

## Problem Type

Estimate how many roots exist and where to start numerical methods.

## Method Definition

1. Sample $f$ on a search window.
2. Mark sign changes or axis crossings.
3. Optionally plot $g$ and $h$ when solving $g(x)=h(x)$ via $f=g-h$.
4. Hand off each promising interval to bisection/Newton/secant.

## Assumptions / Requirements

- $f$ can be evaluated on a dense enough grid
- Visual resolution limits accuracy; graphics alone do not prove uniqueness

## Algorithm

1. Choose a window $[A,B]$ and sample points $x_i$.
2. Compute $f(x_i)$ and look for sign changes or near-zeros.
3. For each sign change on $[x_i,x_{i+1}]$, record a candidate bracket.
4. Refine with a numerical method.

## Convergence

Not iterative in the algorithmic sense. Finer sampling reduces the chance of missing roots but never replaces a rigorous method.

## Error / Accuracy

Graphical estimates are typically accurate only to a fraction of the sample spacing. Always refine numerically.

## Worked Example

Let $f(x)=x^3-4x+1$ on $[-2,2]$.

| $x$ | $f(x)$ |
| --- | --- |
| −2 | 1 |
| −1 | 4 |
| 0 | 1 |
| 1 | −2 |
| 2 | 1 |

Sign changes on $[-2,-1]?$ No ($1$ and $4$). On $[0,1]$: $+$ to $-$. On $[1,2]$: $-$ to $+$. Also $f(-2)=1>0$ and $f\to-\infty$ as $x\to-\infty$, so another root lies left of $-2$ if the window is extended.

Thus there are **three real roots** (cubic), not a unique root on $[-2,2]$. The graph suggests brackets near $(-2.2,-2)$, $(0,1)$, and $(1,2)$. Do not claim uniqueness from a partial plot.

Intersection form: solving $g(x)=h(x)$ is the same problem for $f=g-h$. Example $g(x)=x^3-2x+1$, $h(x)=x^2-1$ gives $f(x)=x^3-x^2-2x+2$ with a root at $x=1$ since $f(1)=0$.

## Common Failure Modes

- Missing roots between coarse samples
- Claiming uniqueness when multiple crossings exist
- Treating a tangency ($f=f'=0$) as a simple crossing
- Extrapolating far outside the plotted window

## Connections

- [[Bolzano's Theorem]], [[Bisection Method]]
- [[Root Finding]]

## References

Graphical scouting is standard preparation for classical root algorithms.[^burden]

[^burden]: Burden & Faires, *Numerical Analysis*; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
