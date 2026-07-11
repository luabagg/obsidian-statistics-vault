---
dg-publish: true
tags:
  - calculus
  - limits
aliases:
  - Fundamental Limits
---

# Fundamental Limits of Calculus

## Summary

A small set of standard limits underpins derivatives of trigonometric and exponential functions. The three below are the ones used most often in first-year calculus.

## Prerequisites

[[Limits]], [[Trigonometry]], [[Exponentials and Logarithms]]

## Main Result / Formula

Assume angles are in **radians**.

1. **Sine over argument**
$$
\lim_{x\to 0}\frac{\sin x}{x}=1.
$$

2. **Cosine deficit**
$$
\lim_{x\to 0}\frac{1-\cos x}{x}=0,\qquad
\lim_{x\to 0}\frac{1-\cos x}{x^2}=\frac12.
$$

3. **Exponential / continuous compounding**
$$
\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e,\qquad
\lim_{h\to 0}\frac{e^h-1}{h}=1.
$$

## Conditions / Assumptions

- Limits involving $\sin$ and $\cos$ require radian measure.
- The squeeze theorem is the usual rigorous path for $\sin x/x$.
- The base $e$ may be *defined* via one of the exponential limits above; then the others become theorems.

## Worked Example

$$
\lim_{x\to 0}\frac{\sin(5x)}{x}
=\lim_{x\to 0}5\cdot\frac{\sin(5x)}{5x}
=5\cdot 1=5.
$$

## Common Mistakes

- Evaluating $\sin x/x$ in degree mode.
- Replacing $\sin x$ by $x$ without justification outside a limit $x\to 0$.

## Connections

- Related: [[Squeeze Theorem]], [[Derivatives]]
- Next: derivatives of $\sin$, $\cos$, $e^x$

## References

These standard limits appear throughout calculus texts.[^ost1]

[^ost1]: OpenStax, *Calculus Volume 1*, https://openstax.org/details/books/calculus-volume-1
