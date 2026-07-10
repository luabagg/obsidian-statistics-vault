---
dg-publish: true
tags:
  - precalculus
  - functions
aliases:
  - Function
  - Domain and Range
---

# Functions

## Summary

A function assigns to each valid input exactly one output. Domain, range, composition, and inverses are the core tools used throughout pre-calculus and calculus.

## Prerequisites

Prerequisites: real numbers, coordinate plane, solving basic equations. Hub: [[Pré-Cálculo]].

## Definition / Statement

A **function** $f$ from a set $D$ to a set $R$ is a rule that assigns to each $x \in D$ a unique value $f(x) \in R$.

- **Domain** of $f$: the set of all admissible inputs $x$.
- **Range** (image) of $f$: the set of all outputs $f(x)$ for $x$ in the domain.
- Two functions $f$ and $g$ are **equal** if they have the same domain and $f(x)=g(x)$ for every $x$ in that domain.

## Notation

| Symbol | Meaning |
|---|---|
| $f: D \to R$ | function from domain $D$ into codomain $R$ |
| $f(x)$ | output of $f$ at input $x$ |
| $(f \circ g)(x)$ | composition $f(g(x))$ |
| $f^{-1}$ | inverse function of $f$ (when it exists) |
| $y = f(x)$ | graph-equation form |

## Conditions / Assumptions

Unless stated otherwise, work over the real numbers $\mathbb{R}$.

- Composition $f \circ g$ requires the range of $g$ to lie in the domain of $f$.
- An inverse $f^{-1}$ exists as a function if and only if $f$ is **one-to-one** (injective) on its domain: $f(a)=f(b)$ implies $a=b$.
- The graph of $y=f(x)$ passes the vertical line test (exactly one $y$ for each $x$ in the domain).

## Main Result / Formula

**Composition**

$$
(f \circ g)(x) = f\bigl(g(x)\bigr).
$$

Composition is not commutative in general: $f \circ g$ need not equal $g \circ f$.

**Inverse (when $f$ is one-to-one)**

$$
f^{-1}\bigl(f(x)\bigr) = x \quad\text{for all } x \text{ in the domain of } f,
$$
$$
f\bigl(f^{-1}(y)\bigr) = y \quad\text{for all } y \text{ in the range of } f.
$$

The graph of $y = f^{-1}(x)$ is the reflection of $y = f(x)$ across the line $y = x$.

**Finding an inverse algebraically (common procedure)**

1. Write $y = f(x)$.
2. Solve for $x$ in terms of $y$.
3. Swap names: $x = f^{-1}(y)$ becomes $y = f^{-1}(x)$.
4. Restrict the domain of $f$ first if needed so that $f$ is one-to-one.

## Worked Example

Let $f(x) = 2x - 3$ and $g(x) = x^2$.

1. Domain of $f$ and $g$: both $\mathbb{R}$.
2. Composition:
   $$
   (f \circ g)(x) = f(x^2) = 2x^2 - 3, \qquad
   (g \circ f)(x) = g(2x-3) = (2x-3)^2.
   $$
3. Inverse of $f$: set $y = 2x - 3$, so $x = \frac{y+3}{2}$. Thus
   $$
   f^{-1}(x) = \frac{x+3}{2}.
   $$
   Check: $f(f^{-1}(x)) = 2\cdot\frac{x+3}{2} - 3 = x$.

Note that $g(x)=x^2$ is not one-to-one on $\mathbb{R}$, so it has no inverse as a function unless the domain is restricted (e.g. to $[0,\infty)$).

## Common Mistakes

- Confusing **codomain** with **range**: the range is the actual set of outputs attained.
- Treating $f^{-1}$ as $1/f$: reciprocal and inverse function are different.
- Composing in the wrong order: $(f \circ g)(x)$ means apply $g$ first.
- Claiming every function has an inverse without checking injectivity.

## Connections

- Related: [[Polynomials and Rational Functions]], [[Exponentials and Logarithms]], [[Trigonometria]]
- Next: polynomial/rational behavior, then exponential/log and trig functions
- Later: limits and continuity in [[Cálculo]]

## References

Domain, range, composition, and inverses follow standard function treatment in OpenStax Precalculus.[^openstax-precalc-fn]

[^openstax-precalc-fn]: OpenStax, *Precalculus 2e*, Functions, https://openstax.org/details/books/precalculus-2e
