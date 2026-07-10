---
dg-publish: true
dg-show-local-graph: true
tags:
  - calculus
  - multivariable
---

%% Begin Waypoint %%
- **[[Funções de Mais de uma Variável]]**
	- [[Coordenadas Cilíndricas]]
	- [[Coordenadas Esféricas]]
	- [[Coordenadas Polares]]
	- [[Método dos Multiplicadores de Lagrange]]
	- [[Teorema de Clairaut]]
	- [[Valores de Máximo e Mínimo]]

%% End Waypoint %%

# Functions of Several Variables

## Summary

A function of several variables assigns a single real value to each point of a domain in $\mathbb{R}^n$. For two variables, $z=f(x,y)$ is visualized as a surface; level curves $f(x,y)=c$ describe horizontal slices.

## Prerequisites

Functions of one variable, plane geometry, [[Limites e Continuidade de Funções de 2 Variáveis]] for limit theory.

## Definition

A real-valued function of two variables is a map

$$
f:D\subseteq\mathbb{R}^2\to\mathbb{R},\qquad (x,y)\mapsto f(x,y).
$$

The **domain** $D$ is the set of $(x,y)$ for which the expression is defined. The **range** is $\{f(x,y):(x,y)\in D\}$.

A **level curve** (contour) of $f$ is the set

$$
\{(x,y)\in D:f(x,y)=c\}
$$

for a constant $c$ in the range. Level **surfaces** arise for $f(x,y,z)=c$.

## Notation

- Independent variables: $x,y$ (or $\mathbf{x}\in\mathbb{R}^n$).
- Dependent variable: $z=f(x,y)$.
- Graph: $\{(x,y,f(x,y)):(x,y)\in D\}\subset\mathbb{R}^3$.

## Conditions / Assumptions

- Domain restrictions come from the formula (denominators, even roots, logarithms, etc.).
- Continuity and differentiability are pointwise properties; see linked notes.

## Worked Example

For $f(x,y)=\sqrt{1-x^2-y^2}$, the domain is the closed unit disk $x^2+y^2\le 1$. Level curves $f=c$ for $0\le c\le 1$ are circles $x^2+y^2=1-c^2$.

For $g(x,y)=\dfrac{x}{y}$, the domain is $y\neq 0$; level curves are lines $x=cy$ (excluding the origin of the $x$-axis issue only when $c$ free and $y\neq 0$).

## Common Mistakes

- Treating the domain as all of $\mathbb{R}^2$ when the formula is not defined everywhere.
- Confusing level curves of $f$ with the graph of $f$.

## Connections

- Calculus tools: [[Derivadas Parciais]], [[Valores de Máximo e Mínimo]], [[Método dos Multiplicadores de Lagrange]]
- Coordinates: [[Coordenadas Polares]], [[Coordenadas Cilíndricas]], [[Coordenadas Esféricas]]
- Limits: [[Limites e Continuidade de Funções de 2 Variáveis]]

## References

Domains, graphs, and level curves are introduced in OpenStax Calculus Volume 3.[^openstax-mv-fn]

[^openstax-mv-fn]: OpenStax, *Calculus Volume 3*, Section 4.1, https://openstax.org/details/books/calculus-volume-3
