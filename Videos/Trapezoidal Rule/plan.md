# Trapezoidal Rule — visual plan

## Teaching goal

Show that the trapezoidal rule approximates a definite integral by replacing the area under a curve with the area of trapezoids, and that increasing the number of subintervals visibly reduces the error.

## Narrative arc

1. Show a curve and the exact area under it (shaded green).
2. Overlay a single trapezoid spanning [a, b] — its area clearly over/under-estimates.
3. Split into 2 subintervals: two trapezoids hug the curve more tightly.
4. Split into 4 subintervals: the trapezoids nearly match the curve.
5. End with the formula: T_n = (h/2)[f(x_0) + 2f(x_1) + ... + 2f(x_{n-1}) + f(x_n)].

## Visual language

- Background: dark charcoal (#1C1C1C).
- Curve: blue (#58C4DD); exact area: green at low opacity.
- Trapezoid fills: yellow at low opacity; trapezoid top edges: yellow solid.
- Formula text: green for the final result.
- Font: DejaVu Sans Mono, no LaTeX.

## Verification

Render at low quality first, inspect the final frame for clipping. Render final MP4 at 1080p60. Embed in `Numerical Methods/Numerical Integration/Trapezoidal Rule.md`.