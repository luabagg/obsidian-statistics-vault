---
dg-publish: true
tags:
  - calculus
  - series
---

# Root Test

## Summary

The root test uses $L=\limsup_{n\to\infty}|a_n|^{1/n}$ (or the ordinary limit when it exists). Absolute convergence holds if $L<1$; divergence if $L>1$; the test is inconclusive if $L=1$.

## Prerequisites

[[Convergência Absoluta]], sequences and limits

## Theorem

For a series $\sum a_n$, set

$$
L=\limsup_{n\to\infty}\sqrt[n]{|a_n|}.
$$

- If $L<1$, then $\sum a_n$ converges absolutely.
- If $L>1$ (including $L=\infty$), then $a_n\not\to 0$, so the series diverges.
- If $L=1$, the test gives no information.

When $\lim |a_n|^{1/n}$ exists, it equals this limsup.

## Conditions / Assumptions

- No sign restriction for the absolute-convergence conclusion.
- Prefer the ratio test when factorials appear; the root test is natural for $n$th powers.

## Worked Example

For $\sum (1/2)^n$, $|a_n|^{1/n}=1/2$, so $L=1/2<1$: absolute convergence.

For $\sum n^2/e^n$, $|a_n|^{1/n}=n^{2/n}/e\to 1/e<1$ (since $n^{1/n}\to 1$), so absolute convergence.

## Common Mistakes

- Treating $L=1$ as convergence (harmonic series and $p$-series both give $L=1$).
- Computing $\sqrt[n]{a_n}$ without absolute values when terms change sign.

## Connections

- [[Teste da Razão]], [[Séries de Potências]] (root form of the radius formula)

## References

The root test appears in OpenStax Calculus Volume 2.[^openstax-root]

[^openstax-root]: OpenStax, *Calculus Volume 2*, Section 5.6, https://openstax.org/details/books/calculus-volume-2
