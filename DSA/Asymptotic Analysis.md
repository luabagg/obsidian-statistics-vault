---
dg-publish: true
aliases:
  - Big O
  - Big Theta
  - Big Omega
  - Asymptotic Notation
---

# Asymptotic Analysis

Asymptotic analysis describes how an algorithm's resource use grows as input size $n$ becomes large. It ignores machine-specific constants when the goal is to compare growth rates, but the definitions are still precise mathematical bounds.[^clrs-asymptotic]

## Prerequisites

Prerequisites: functions, inequalities, and limits.

## Definition

Let $f(n)$ and $g(n)$ be nonnegative functions for all sufficiently large $n$.
Usually $f(n)$ is running time or memory use.
Usually $g(n)$ is a simpler comparison function.

## Notation

| Notation | Meaning | Formal definition |
|---|---|---|
| $f(n)=O(g(n))$ | Asymptotic upper bound | There exist constants $c>0$ and $n_0$ such that $0\le f(n)\le c g(n)$ for all $n\ge n_0$. |
| $f(n)=\Omega(g(n))$ | Asymptotic lower bound | There exist constants $c>0$ and $n_0$ such that $0\le c g(n)\le f(n)$ for all $n\ge n_0$. |
| $f(n)=\Theta(g(n))$ | Asymptotically tight bound | There exist constants $c_1,c_2>0$ and $n_0$ such that $0\le c_1g(n)\le f(n)\le c_2g(n)$ for all $n\ge n_0$. |

## Examples

- Linear search worst-case time is $\Theta(n)$: it may inspect every item, and it never inspects more than $n$ items.
- Binary search worst-case time is $\Theta(\log n)$: each comparison halves the remaining sorted search interval.
- $3n^2+10n+7=\Theta(n^2)$, because constants and lower-order terms are dominated for large $n$.
- $3n^2+10n+7=O(n^3)$ is true but loose; $O$ alone does not mean "best possible."

## Worked Example

Show that $5n+20=\Theta(n)$.

For $n\ge 1$:

$$
5n+20 \le 25n,
$$

so $5n+20=O(n)$ with $c_2=25$. Also:

$$
5n \le 5n+20,
$$

so $5n+20=\Omega(n)$ with $c_1=5$. Since both bounds hold, $5n+20=\Theta(n)$.

## Common Mistakes

- Saying Big-O means exact runtime; it is only an upper bound.
- Writing $O(2n)$ instead of simplifying to $O(n)$.
- Treating $\Omega$ like "best case"; it is lower-bound notation, not automatically one case label.
- Ignoring the phrase "for all sufficiently large $n$."
- Comparing algorithms only by asymptotic order when constants or input sizes dominate in practice.

## Connections

| Related note | Use |
|---|---|
| [[LEARNING_PATHS|Learning Paths]] | Navigation hub |

## References

[^clrs-asymptotic]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms*, 3rd ed., MIT Press, ISBN 978-0-262-03384-8.
