---
dg-publish: true
aliases:
  - De Morgan's Laws
  - Leis de Morgan
---

# De Morgan's Laws

Compact study note.

## Summary

De Morgan's laws describe how complements distribute over unions and intersections. They are used constantly when translating probability statements involving 'not', 'and', and 'or'.[^openstax-prob]

## Prerequisites

- [[Sample Space and Events|Sample Space and Events]]

## Notation and Assumptions

Complements are taken relative to $\Omega$:

$$A^c=\Omega\setminus A.$$

## Essential Result

De Morgan identities:

$$(A\cup B)^c=A^c\cap B^c.$$

$$(A\cap B)^c=A^c\cup B^c.$$

The same identities hold for countable families.

## Small Example

If events are 'rain' and 'wind', then 'neither rain nor wind' is

$$(R\cup W)^c=R^c\cap W^c.$$

## Common Mistakes

- Confusing 'not both' with 'neither'.
- Forgetting that complements depend on the chosen sample space.

## Connections

- [[Sigma-Algebra|Sigma-Algebra]]
- [[Conditional Probability|Conditional Probability]]
- [[Independence|Independence]]

## References

[^openstax-prob]: OpenStax, *Introductory Statistics 2e*, "Chapter 3: Probability Topics", https://openstax.org/books/introductory-statistics-2e/pages/3-introduction
