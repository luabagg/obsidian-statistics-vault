---
dg-publish: true
---

# Secant Method

## Summary

The secant method approximates Newton’s step by replacing $f'(x_n)$ with a finite difference built from the last two iterates. It needs two starts and no derivative evaluations.

## Prerequisites

- Continuous $f$ (smoothness helps local analysis)
- Optional background: [[Método de Newton-Raphson]]

## Problem Type

Solve $f(x)=0$ when $f'$ is unavailable or expensive.

## Method Definition

Given $x_{n-1}$ and $x_n$ with $f(x_n)\neq f(x_{n-1})$,

$$
x_{n+1} = x_n - f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}.
$$

This is the root of the secant line through $(x_{n-1},f(x_{n-1}))$ and $(x_n,f(x_n))$.[^burden]

## Assumptions / Requirements

- Two distinct initial guesses near a simple root
- $f(x_n)\neq f(x_{n-1})$ at each step
- Local theory typically assumes $f\in C^2$ near the root with $f'(r)\neq 0$

## Algorithm

1. Choose $x_0,x_1$ and tolerance $\varepsilon$.
2. While not stopped:
   - If $|f(x_n)-f(x_{n-1})|$ is extremely small relative to the step scale, abort (ill-conditioned update). A tiny denominator is **not** the same as having found a root.
   - Compute $x_{n+1}$ from the formula.
   - Stop if $|x_{n+1}-x_n|<\varepsilon$ or $|f(x_{n+1})|<\varepsilon$.

## Convergence

Local order is the golden ratio $\varphi\approx 1.618$ (superlinear) for simple roots under standard conditions. Global convergence is not guaranteed.

## Error / Accuracy

Monitor both the step $|x_{n+1}-x_n|$ and residual $|f(x_{n+1})|$.

## Worked Example

$f(x)=x^3-2x-5$, starts $x_0=2$, $x_1=2.5$.

$$
f(2)=-1,\qquad f(2.5)=15.625-5-5=5.625
$$

$$
x_2 = 2.5 - \frac{5.625\cdot(2.5-2)}{5.625-(-1)} = 2.5 - \frac{2.8125}{6.625} \approx 2.075472
$$

Continuing:

| $n$ | $x_n$ (approx.) | $f(x_n)$ (approx.) |
| --- | --- | --- |
| 0 | 2.000000 | −1.000 |
| 1 | 2.500000 | 5.625 |
| 2 | 2.075472 | −0.211 |
| 3 | 2.090798 | −0.042 |
| 4 | 2.094592 | $4.5\cdot 10^{-4}$ |
| 5 | 2.094551 | $\approx 0$ |

The root is $r\approx 2.094551$.

## Common Failure Modes

- Bad starts far from any root
- Division by nearly zero when $f(x_n)\approx f(x_{n-1})$
- Cycling or divergence without a bracket safeguard

## Connections

- [[Método de Newton-Raphson]]
- [[Método da Falsa Posição]]
- [[Zeros de Funções]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, secant method; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
