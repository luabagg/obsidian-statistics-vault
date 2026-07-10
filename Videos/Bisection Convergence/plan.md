# Bisection Convergence — visual plan

## Teaching goal

Correct the misconception that a root finder is merely “guess and check.” Bisection is guaranteed by a sign-changing bracket and converges because each accepted interval is half the previous width.

## Narrative arc

1. Show a continuous curve crossing the axis and a bracket with opposite signs.
2. Mark the midpoint and explain that its sign selects one half of the bracket.
3. Repeat the halving several times while the bracket visibly contracts.
4. End with the invariant and the error bound: after `n` steps, width is `(b-a)/2^n`.

## Visual language

- Background: dark charcoal.
- Curve: blue; axis: muted gray.
- Current bracket: yellow.
- Midpoint: red.
- Accepted root neighborhood: green.
- Use text labels instead of LaTeX so the scene renders without a TeX installation.

## Verification

Render with Manim Community Edition at low quality first, inspect the final frame, then render the final MP4. Link the finished video from `Métodos Numéricos/Zeros de Funções/Método da Bisseção.md`.
