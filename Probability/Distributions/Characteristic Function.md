---
dg-publish: true
aliases:
  - Characteristic Function
  - Função Característica
---

# Characteristic Function

Compact study note.

## Summary

Characteristic functions use complex exponentials and uniquely determine real-valued distributions.[^mit-prob]

$$\varphi_X(t)=E[\exp(itX)].$$

## Prerequisites

- [[Random Variable|Random Variable]]
- [[Expectation of a Random Variable|Expected Value]]

## Notation and Assumptions

Use $i^2=-1$ and real $t$. Since

$$|\exp(itX)|=1,$$

the expectation is always finite.

## Essential Result

For independent $X$ and $Y$,

$$\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t).$$

If moments exist,

$$\varphi_X^{(n)}(0)=i^nE[X^n].$$

## Small Example

For $X\sim\operatorname{Uniform}(l,u)$,

$$\varphi_X(t)=\frac{\exp(itu)-\exp(itl)}{it(u-l)}, \qquad t\ne0.$$

Also $\varphi_X(0)=1$.

## Common Mistakes

- Thinking characteristic functions fail to exist when MGFs fail.
- Forgetting the special value at $t=0$ in formulas with $t$ in the denominator.

## Connections

- [[Moment Generating Functions|Moment Generating Functions]]
- [[Central Limit Theorem|Central Limit Theorem]]
- [[Uniform Distribution|Continuous Uniform Distribution]]

## References

[^mit-prob]: MIT OpenCourseWare, "6.041SC Probabilistic Systems Analysis and Applied Probability", Fall 2013, https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
