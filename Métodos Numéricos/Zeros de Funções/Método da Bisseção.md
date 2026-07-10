---
dg-publish: true
---

# Bisection Method

## Summary

Bisection finds a root of a continuous function on a bracket $[a,b]$ with $f(a)f(b)<0$ by repeatedly cutting the interval in half. It is slow but reliable.

## Prerequisites

- [[Teorema De Bolzano]]
- Ability to evaluate $f$

## Problem Type

Solve $f(x)=0$ when a valid sign-changing interval is known.

## Method Definition

Given continuous $f$ on $[a,b]$ with $f(a)f(b)<0$, set $c=(a+b)/2$. Replace $[a,b]$ by the half that still has a sign change. Repeat until the half-width is below a tolerance.[^burden]

## Assumptions / Requirements

- $f$ continuous on $[a,b]$
- $f(a)f(b)<0$
- The method may return any root if several lie in the bracket

## Algorithm

1. Input $a,b,\varepsilon,\texttt{max\_iter}$ with $f(a)f(b)<0$.
2. For $k=1,2,\ldots$:
   - $c \leftarrow (a+b)/2$
   - If $|f(c)|<\varepsilon$ or $(b-a)/2 < \varepsilon$, return $c$
   - If $f(a)f(c)<0$ then $b\leftarrow c$, else $a\leftarrow c$
3. Stop with failure if the iteration budget is exceeded

## Formula / Iteration Rule

$$
c_k = \frac{a_k+b_k}{2},\qquad
\text{error bound:}\quad |c_k - r| \le \frac{b_0-a_0}{2^k}
$$

for some root $r\in[a_k,b_k]$.

## Convergence

Linear (interval length halves each step). Convergence is guaranteed under the assumptions above.

## Error / Accuracy

Stopping options:

- Absolute interval: $(b-a)/2 < \varepsilon$
- Residual: $|f(c)|<\varepsilon$

Iteration count to guarantee half-width $\le\varepsilon$:

$$
n \ge \log_2\left(\frac{b_0-a_0}{\varepsilon}\right)
$$

## Worked Example

Use $f(x)=x^3-2x-5$. Then $f(1)=-6$, $f(2)=-1$, $f(3)=16$. A valid bracket is $[2,3]$, not $[1,2]$.[^burden]

With $\varepsilon=10^{-3}$:

$$
n \ge \log_2\left(\frac{1}{0.001}\right) \approx 9.97 \Rightarrow n=10
$$

First steps:

| $k$ | $a$ | $b$ | $c$ | $f(c)$ | new interval |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 2.5 | 4.875 | $[2,2.5]$ |
| 2 | 2 | 2.5 | 2.25 | 1.546875 | $[2,2.25]$ |
| 3 | 2 | 2.25 | 2.125 | 0.18164… | $[2,2.125]$ |

The unique real root is near $2.09455$.

## Pseudocode

```
function bisection(f, a, b, tol, max_iter):
    require f(a)*f(b) < 0
    for k = 1 to max_iter:
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a)/2 < tol:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2   # not converged
```

## Common Failure Modes

- Invalid bracket (no sign change)
- Multiple roots in $[a,b]$ (any one may be returned)
- Extremely flat $f$ near the root (residual criterion may mislead)

## Connections

- [[Método da Falsa Posição]] keeps a bracket but uses a secant intercept
- [[Método de Newton-Raphson]] is faster locally but not globally guaranteed
- [[Zeros de Funções]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, bisection method; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
