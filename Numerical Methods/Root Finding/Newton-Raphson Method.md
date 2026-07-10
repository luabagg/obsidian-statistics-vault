---
dg-publish: true
---

# Newton–Raphson Method

## Summary

Newton–Raphson linearizes $f$ at the current guess and takes the root of that tangent line. For simple roots with a good start, convergence is locally quadratic.

## Prerequisites

- Differentiable $f$ with computable $f'$
- Optional: [[Secant Method]] as a derivative-free cousin

## Problem Type

Solve $f(x)=0$ when $f'$ is available and a reasonable initial guess is known.

## Method Definition

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)},\qquad f'(x_n)\neq 0.
$$

Geometrically, $x_{n+1}$ is where the tangent at $(x_n,f(x_n))$ hits the $x$-axis.[^burden]

## Assumptions / Requirements

- $f\in C^2$ near the root (for the classical local theory)
- Simple root: $f(r)=0$ and $f'(r)\neq 0$
- Initial $x_0$ sufficiently close to $r$
- $f'(x_n)\neq 0$ at every iterate

## Algorithm

1. Choose $x_0$, tolerance $\varepsilon$, max iterations.
2. Compute $x_{n+1}=x_n-f(x_n)/f'(x_n)$.
3. Stop if $|x_{n+1}-x_n|<\varepsilon$ or $|f(x_{n+1})|<\varepsilon$.
4. Fail if $f'(x_n)=0$ or the budget is exhausted.

## Convergence

For a simple root and $x_0$ close enough, the error satisfies $e_{n+1}\approx C e_n^2$ (quadratic). Multiple roots reduce the order to linear unless the method is modified.

## Error / Accuracy

Use step size and residual together. Quadratic convergence means digits roughly double each successful iteration near the root.

## Worked Example

$f(x)=x^3-2x-5$, $f'(x)=3x^2-2$, start $x_0=2$.

$$
x_1 = 2 - \frac{f(2)}{f'(2)} = 2 - \frac{-1}{10} = 2.1
$$

$$
x_2 = 2.1 - \frac{2.1^3-4.2-5}{3\cdot 2.1^2-2} = 2.1 - \frac{0.061}{11.23}\approx 2.09457
$$

$$
x_3 \approx 2.09455148
$$

Residual at $x_3$ is already near machine noise for double precision in a few more steps.

## Common Failure Modes

- $f'(x_n)=0$ or tiny (step blows up)
- Poor initial guess → divergence or attraction to a different root
- Multiple roots → slow linear convergence and unstable division
- Cycles for some nonlinear $f$

## Connections

- [[Secant Method]]
- [[Bisection Method]] for a safe global phase before Newton polish
- [[Root Finding]]

## References

[^burden]: Burden & Faires, *Numerical Analysis*, Newton’s method; NIST DLMF Ch. 3, https://dlmf.nist.gov/3
