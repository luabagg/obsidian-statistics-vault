---
dg-publish: true
tags:
  - calculus
  - series
---

# Sequences

## Summary

A sequence $\{a_n\}$ is an ordered list of numbers indexed by integers $n$. It converges if $a_n$ approaches a finite limit as $n\to\infty$. Series are built by summing sequence terms.

## Prerequisites

[[Limits]]

## Definition

A sequence is a function $n\mapsto a_n$ from $\mathbb{N}$ (or $\mathbb{N}\cup\{0\}$) to $\mathbb{R}$. We write $\{a_n\}_{n=1}^\infty$.

$$
\lim_{n\to\infty}a_n=L
$$

means: for every $\varepsilon>0$ there exists $N$ such that $n>N$ implies $|a_n-L|<\varepsilon$.

## Types (examples)

- Arithmetic: $a_n=a+(n-1)d$ (e.g. $1,3,5,7,\ldots$).
- Geometric: $a_n=ar^{n-1}$ (e.g. $2,6,18,54,\ldots$).
- Recursive: Fibonacci $F_n=F_{n-1}+F_{n-2}$.

## Worked Example

$a_n=1/n\to 0$ (convergent).
$b_n=n\to\infty$ (diverges).
$c_n=(-1)^n$ diverges by oscillation.

## Common Mistakes

- Confusing the limit of a sequence $a_n$ with the sum of the series $\sum a_n$.
- Claiming every bounded sequence converges (false in $\mathbb{R}$ without monotonicity; true for monotone bounded sequences).

## Connections

- Partial sums of series are sequences: [[Series Sums by Partial Sums]]
- Next: [[Infinite Series]]

## References

Sequences are introduced before series in OpenStax Calculus Volume 2.[^openstax-seq]

[^openstax-seq]: OpenStax, *Calculus Volume 2*, Section 5.1, https://openstax.org/details/books/calculus-volume-2
