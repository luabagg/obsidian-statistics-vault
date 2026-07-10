---
dg-publish: true
---

# False Position Method (Regula Falsi)

## Summary

False position keeps a sign-changing bracket like bisection, but places the next sample at the intercept of the secant through $(a,f(a))$ and $(b,f(b))$. It often reduces the residual faster than pure bisection while preserving a bracket.

## Prerequisites

- [[Bolzano's Theorem]]
- [[Bisection Method]] (bracketing idea)

## Problem Type

Solve $f(x)=0$ on a continuous bracket with opposite signs.

## Method Definition

Given continuous $f$ on $[a,b]$ with $f(a)f(b)<0$, set

$$
c = \frac{a\,f(b)-b\,f(a)}{f(b)-f(a)}
$$

and replace the endpoint whose function value has the same sign as $f(c)$.[^burden]

## Assumptions / Requirements

- Continuity on $[a,b]$
- $f(a)f(b)<0$
- $f(b)\neq f(a)$ (secant is defined)

## Algorithm

1. Evaluate $f(a),f(b)$ with opposite signs.
2. Compute $c$ from the formula above.
3. If $|f(c)|$ or $|b-a|$ is small enough, stop.
4. If $f(a)f(c)<0$ then $b\leftarrow c$, else $a\leftarrow c$.
5. Repeat.

## Formula / Iteration Rule

$$
c_k = \frac{a_k f(b_k)-b_k f(a_k)}{f(b_k)-f(a_k)}
$$

Equivalent form:

$$
c_k = a_k - f(a_k)\frac{b_k-a_k}{f(b_k)-f(a_k)}
$$

## Convergence

Typically faster residual reduction than bisection when $f$ is roughly linear near the root. Convergence is still linear in general. One endpoint can stagnate for convex/concave $f$; modified regula falsi variants fix this.

## Error / Accuracy

Common stops: $|f(c)|<\varepsilon$ or $|c_{\text{new}}-c_{\text{old}}|<\varepsilon$. The interval length need not shrink as aggressively as in bisection.

## Worked Example

Again use $f(x)=x^3-2x-5$. Valid bracket: $[2,3]$ because $f(2)=-1$ and $f(3)=16$.

Iteration 1:

$$
c_1 = \frac{2\cdot 16 - 3\cdot(-1)}{16-(-1)} = \frac{32+3}{17}=\frac{35}{17}\approx 2.05882
$$

$$
f(c_1)\approx -0.3908 < 0 \Rightarrow \text{new bracket }[c_1,3]
$$

Iteration 2:

$$
c_2 = \frac{2.05882\cdot 16 - 3\cdot f(c_1)}{16-f(c_1)}\approx 2.08126,\quad f(c_2)\approx -0.1472
$$

Subsequent iterates approach $\approx 2.09455$ from below while the right endpoint stays at $3$ for several steps (classic regula falsi stagnation pattern).

## Common Failure Modes

- Invalid initial bracket
- One endpoint stuck for many iterations
- Near-zero denominator if $f(a)\approx f(b)$ (should not happen under opposite signs unless values are tiny)

## Connections

- [[Secant Method]] drops the bracketing constraint
- [[Bisection Method]] for guaranteed interval halving
- [[Root Finding]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, regula falsi; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
