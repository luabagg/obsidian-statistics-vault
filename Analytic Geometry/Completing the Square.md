---
dg-publish: true
tags:
  - geometry
  - algebra
  - completing-the-square
aliases:
  - Completing the Square
  - Completamento de quadrados
---

# Completing the Square

## Summary

Completing the square rewrites a quadratic expression as a perfect square plus a constant. In analytic geometry it reveals centers and radii of circles and the standard forms of other conics.

## Prerequisites

Polynomial algebra (expanding and factoring). Helpful: [[Polynomials and Rational Functions]]. Hub: [[Analytic Geometry]].

## Object / Concept

Given a monic quadratic in one variable,

$$
x^2 + bx + c,
$$

**completing the square** produces

$$
x^2 + bx + c = \Bigl(x + \frac{b}{2}\Bigr)^2 - \Bigl(\frac{b}{2}\Bigr)^2 + c.
$$

For a leading coefficient $a \neq 0$,

$$
ax^2 + bx + c = a\Biggl[\Bigl(x + \frac{b}{2a}\Bigr)^2 - \Bigl(\frac{b}{2a}\Bigr)^2\Biggr] + c.
$$

## Coordinate System

Usually the Cartesian plane or space, when rewriting equations such as $x^2 + y^2 + Dx + Ey + F = 0$.

## Notation

| Symbol | Meaning |
|---|---|
| $a,b,c$ | coefficients of $ax^2+bx+c$ |
| $(h,k)$ | center after rewriting in completed-square form |

## Conditions / Assumptions

- Real coefficients unless stated otherwise.
- For the monic formula, divide through by $a$ first when $a \neq 1$.
- Completing the square does not change the solution set of an equation; both sides must be handled consistently.

## Equations

**One variable (monic)**

$$
x^2 + bx = \Bigl(x + \frac{b}{2}\Bigr)^2 - \Bigl(\frac{b}{2}\Bigr)^2.
$$

**Circle general form**

$$
x^2 + y^2 + Dx + Ey + F = 0
$$

becomes, after completing the square in $x$ and in $y$,

$$
\Bigl(x + \frac{D}{2}\Bigr)^2 + \Bigl(y + \frac{E}{2}\Bigr)^2 = \frac{D^2 + E^2 - 4F}{4},
$$

provided the right-hand side is positive (circle), zero (point), or negative (empty over the reals).

## Procedure

1. Group $x$ terms (and $y$ terms if present); move constants to the other side if solving/identifying.
2. Factor out the leading coefficient of each quadratic variable if it is not $1$.
3. Add and subtract $\bigl(\tfrac{b}{2a}\bigr)^2$ inside each group (or add the same quantity to both sides of an equation).
4. Write each group as a square and simplify constants.
5. Read off center, radius, or other geometric data.

## Worked Example

Rewrite $x^2 + y^2 - 6x + 4y - 3 = 0$ and identify the circle.

$$
\begin{aligned}
x^2 - 6x + y^2 + 4y &= 3, \\
(x^2 - 6x + 9) + (y^2 + 4y + 4) &= 3 + 9 + 4, \\
(x-3)^2 + (y+2)^2 &= 16.
\end{aligned}
$$

Center $(3,-2)$, radius $4$.

## Common Mistakes

- Forgetting to multiply the completed-square constant by $a$ when $a \neq 1$.
- Adding $\bigl(\tfrac{b}{2}\bigr)^2$ to only one side of an equation.
- Sign errors: $x^2 - 6x$ completes with $(x-3)^2$, not $(x+3)^2$.
- Treating a nonpositive right-hand side as a circle of real radius without checking.

## Connections

- Related: [[Distance and Midpoint]], [[Conic Sections]], [[Polynomials and Rational Functions]]
- Next: [[Conic Sections]], [[Lines and Planes]]
- Later: quadratic forms in [[Linear Algebra]]

## References

Completing the square for conics and quadratics is standard in OpenStax Precalculus analytic geometry material.[^openstax-cts]

[^openstax-cts]: OpenStax, *Precalculus 2e*, Analytic Geometry / Quadratic Functions, https://openstax.org/details/books/precalculus-2e
