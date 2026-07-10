---
dg-publish: true
---

# Bolzano’s Theorem (Intermediate Value Theorem for Roots)

## Summary

Bolzano’s theorem is the existence engine behind bracketed root methods. Continuity on a closed interval plus opposite endpoint signs implies at least one root in the open interval.

## Prerequisites

- Continuity of real functions on closed intervals
- Intermediate value theorem from calculus

## Problem Type

Prove that $f(x)=0$ has a solution in $(a,b)$ before applying numerical root finders.

## Method Definition

**Theorem.** If $f$ is continuous on $[a,b]$ and $f(a)f(b)<0$, then there exists at least one $c\in(a,b)$ such that $f(c)=0$.[^ivt]

## Assumptions / Requirements

- $f$ continuous on the whole interval $[a,b]$
- Endpoint values have opposite signs (strict inequality $f(a)f(b)<0$)
- The theorem does **not** assert uniqueness

## Convergence

This is an existence result, not an algorithm. Bracketed methods (bisection, false position) exploit the same sign condition at every step.

## Error / Accuracy

Bolzano alone does not locate $c$. It only certifies that a root lies in $(a,b)$. For uniqueness, extra structure is needed (e.g. $f'$ never zero, so $f$ is strictly monotone).

## Worked Example

Let $f(x)=x^3-4x+1$ on $[0,2]$.

$$
f(0)=1,\qquad f(2)=8-8+1=1.
$$

No sign change on $[0,2]$. On $[0,1]$:

$$
f(0)=1,\qquad f(1)=1-4+1=-2,
$$

so $f(0)f(1)<0$. Hence at least one root lies in $(0,1)$.

Derivative $f'(x)=3x^2-4$ vanishes at $x=\pm 2/\sqrt{3}$. The positive critical point $\approx 1.15$ lies outside $(0,1)$, and $f'<0$ on $[0,1]$, so $f$ is strictly decreasing there and the root is unique on that interval.

## Common Failure Modes

- Same-sign endpoints: no conclusion (a root may still exist, e.g. a double root with no sign change)
- Discontinuities inside $[a,b]$: the theorem does not apply
- Multiple roots: the theorem still holds but does not say which root a numerical method will find

## Connections

- [[Método da Bisseção]], [[Método da Falsa Posição]]
- [[Método Gráfico]] for choosing brackets
- [[Zeros de Funções]]

## References

[^ivt]: Standard intermediate value theorem / Bolzano theorem; see also NIST DLMF numerical methods overview, https://dlmf.nist.gov/3
