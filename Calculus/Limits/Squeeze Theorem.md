---
dg-publish: true
tags:
  - calculus
  - limits
aliases:
  - Squeeze Theorem
  - Sandwich Theorem
---

# Squeeze Theorem

## Summary

The squeeze theorem (sandwich theorem) finds a limit by trapping a function between two others that share the same limit.

## Prerequisites

[[Limits]]

## Definition / Theorem

Suppose \(g(x)\le f(x)\le h(x)\) for all \(x\) in a deleted neighborhood of \(a\). If

\[
\lim_{x\to a}g(x)=\lim_{x\to a}h(x)=L,
\]

then

\[
\lim_{x\to a}f(x)=L.
\]

The same idea works for one-sided limits and for \(x\to\pm\infty\).

## Conditions / Assumptions

- The inequality must hold near the limit point (except possibly at the point itself).
- Both bounding functions must share **the same** finite (or infinite) limit. One bound alone is not enough.

## Worked Example

Because \(-1\le\sin(1/x)\le 1\) for \(x\neq 0\),

\[
-|x|\le x\sin(1/x)\le |x|.
\]

Since \(\lim_{x\to 0}(-|x|)=\lim_{x\to 0}|x|=0\), the squeeze theorem gives

\[
\lim_{x\to 0}x\sin(1/x)=0.
\]

## Common Mistakes

- Using only an upper bound (for example \(0<e^{-x^2}<x^4\)) and concluding a wrong limit. In fact \(\lim_{x\to\infty}e^{-x^2}=0\).
- Applying the theorem when the two bounds have different limits.

## Connections

- Related: [[Fundamental Limits of Calculus]]
- Uses: many trigonometric limits

## References

The squeeze theorem is a standard limit theorem in calculus.[^ost1]

[^ost1]: OpenStax, *Calculus Volume 1*, https://openstax.org/details/books/calculus-volume-1
