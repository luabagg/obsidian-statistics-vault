---
dg-publish: true
aliases:
  - Sample Space and Events
  - Espaco Amostral e Eventos
---

# Sample Space and Events

Compact study note.

## Summary

One sample space lists possible outcomes; events are sets of outcomes whose probability is defined. This distinction prevents many notation errors in later probability rules.[^openstax-prob]

## Prerequisites

- Prerequisites: None

## Notation and Assumptions

$\Omega$ is the sample space. An outcome is $\omega\in\Omega$. An event is one subset $A\subseteq\Omega$ that belongs to the event collection $\mathcal{F}$.

## Essential Result

For finite elementary models, every subset of $\Omega$ can be an event. For infinite models, events must be chosen through one sigma-algebra.

## Small Example

For two coin flips, $\Omega=\{HH,HT,TH,TT\}$. The event 'exactly one head' is $A=\{HT,TH\}$, not one single outcome.

## Common Mistakes

- Writing $P(H)$ before defining $H$ as an event set.
- Assuming every subset of an uncountable sample space is automatically measurable.

## Connections

- [[Probabilidade|Probability]]
- [[Sigma-Álgebra|Sigma-Algebra]]
- [[Espaço de Probabilidade|Probability Space]]

## References

[^openstax-prob]: OpenStax, *Introductory Statistics 2e*, "Chapter 3: Probability Topics", https://openstax.org/books/introductory-statistics-2e/pages/3-introduction
