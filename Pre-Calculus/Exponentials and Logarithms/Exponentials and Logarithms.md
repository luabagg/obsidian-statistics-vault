---
dg-publish: true
dg-show-local-graph: true
tags:
  - precalculus
  - exponentials
  - logarithms
aliases:
  - Exponential Functions
  - Logarithmic Functions
  - Logarithms
---

%% Begin Waypoint %%
- **[[Exponentials and Logarithms]]**
%% End Waypoint %%

# Exponentials and Logarithms

## Summary

Exponential functions model continuous growth and decay. Logarithms are their inverses and convert products into sums, powers into multiples, and exponential equations into algebraic ones. These tools appear throughout calculus, probability, and statistics.

## Prerequisites

[[Functions]]. Helpful: [[Polynomials and Rational Functions]]. Hub: [[Pre-Calculus]].

## Definition / Statement

For base $a > 0$ with $a \neq 1$, the **exponential function** is

$$
f(x) = a^x.
$$

The **logarithm base $a$** is the inverse of $a^x$:

$$
y = \log_a x \quad\Longleftrightarrow\quad a^y = x,
$$

for $x > 0$. Special cases:

- Natural logarithm: $\ln x = \log_e x$, with $e \approx 2.71828\ldots$
- Common logarithm: $\log x = \log_{10} x$ (when the base is omitted in a common-log context)

## Notation

| Symbol | Meaning |
|---|---|
| $a^x$ | exponential with base $a$ |
| $\log_a x$ | logarithm base $a$ of $x$ |
| $\ln x$ | natural logarithm |
| $e$ | base of the natural exponential |

## Conditions / Assumptions

- Exponential base: $a > 0$, $a \neq 1$.
- Logarithm argument: $x > 0$ (for real-valued logs).
- Logarithm base: same restrictions as exponential base.
- Domain of $a^x$: all real $x$; range: $(0,\infty)$.
- Domain of $\log_a x$: $(0,\infty)$; range: all real $y$.

## Main Result / Formula

**Inverse relationship**

$$
a^{\log_a x} = x \quad (x>0), \qquad \log_a(a^x) = x \quad (x \in \mathbb{R}).
$$

**Logarithm laws** (for positive $u,v$ and real $r$)

$$
\begin{aligned}
\log_a(uv) &= \log_a u + \log_a v, \\
\log_a\Bigl(\frac{u}{v}\Bigr) &= \log_a u - \log_a v, \\
\log_a(u^r) &= r \log_a u.
\end{aligned}
$$

**Change of base** (for any valid bases $a,b$ and $x>0$)

$$
\log_a x = \frac{\log_b x}{\log_b a} = \frac{\ln x}{\ln a}.
$$

**Growth / decay models** (continuous form)

$$
A(t) = A_0 e^{kt},
$$

where $A_0 = A(0)$ and $k$ is the continuous growth rate ($k>0$ growth, $k<0$ decay).

## Worked Example

Solve $3^{2x-1} = 27$.

Note $27 = 3^3$, so

$$
3^{2x-1} = 3^3 \implies 2x - 1 = 3 \implies 2x = 4 \implies x = 2.
$$

Using logs instead: take $\ln$ of both sides,

$$
(2x-1)\ln 3 = \ln 27 = 3\ln 3 \implies 2x-1 = 3 \implies x=2.
$$

## Common Mistakes

- Writing $\log(u+v) = \log u + \log v$ (false in general).
- Applying logs to nonpositive arguments.
- Confusing $\log_a(u^r)$ with $(\log_a u)^r$.
- Treating $\ln(e^x)$ as defined only for $x>0$ (it equals $x$ for all real $x$).

## Connections

- Related: [[Functions]], [[Polynomials and Rational Functions]]
- Next: [[Trigonometry]]
- Later: derivatives of $e^x$ and $\ln x$ in [[Calculus]]; exponential models in probability and statistics

## References

Exponential and logarithmic properties follow OpenStax Precalculus coverage of exponential and logarithmic functions.[^openstax-explog]

[^openstax-explog]: OpenStax, *Precalculus 2e*, Exponential and Logarithmic Functions, https://openstax.org/details/books/precalculus-2e
