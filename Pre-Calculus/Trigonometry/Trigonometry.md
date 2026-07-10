---
dg-publish: true
tags:
  - precalculus
  - trigonometry
aliases:
  - Trigonometry
  - Unit Circle
---

%% Begin Waypoint %%
- **[[Trigonometry]]**

%% End Waypoint %%

# Trigonometry

## Summary

Trigonometry relates angles to ratios of sides and extends those ratios to all real angles via the unit circle. The six trigonometric functions, the fundamental identity, degree–radian conversion, and common angles are the core toolkit for calculus, geometry, and oscillatory models.

## Prerequisites

[[Functions]]. Helpful right-triangle geometry. Hub: [[Pre-Calculus]].

## Definition / Statement

### Right-triangle ratios (acute $\theta$)

In a right triangle, for an acute angle $\theta$:

$$
\begin{aligned}
\sin \theta &= \frac{\text{opposite}}{\text{hypotenuse}}, &
\cos \theta &= \frac{\text{adjacent}}{\text{hypotenuse}}, &
\tan \theta &= \frac{\text{opposite}}{\text{adjacent}}, \\
\csc \theta &= \frac{\text{hypotenuse}}{\text{opposite}}, &
\sec \theta &= \frac{\text{hypotenuse}}{\text{adjacent}}, &
\cot \theta &= \frac{\text{adjacent}}{\text{opposite}}.
\end{aligned}
$$

### Unit circle (all real angles)

The **unit circle** is $x^2 + y^2 = 1$. For an angle $\theta$ measured from the positive $x$-axis (counterclockwise positive), the terminal point is $(\cos \theta, \sin \theta)$. Thus

$$
\cos \theta = x, \qquad \sin \theta = y,
$$

and the other four functions are defined by reciprocals and quotients whenever the denominators are nonzero.

## Notation

| Symbol | Meaning |
|---|---|
| $\theta$ | angle (degrees or radians) |
| $\sin, \cos, \tan$ | sine, cosine, tangent |
| $\csc, \sec, \cot$ | cosecant, secant, cotangent |
| $^\circ$ | degrees |
| $\mathrm{rad}$ | radians (often omitted) |

## Conditions / Assumptions

- Real-valued functions unless stated otherwise.
- Reciprocal functions require nonzero denominators:
  - $\tan \theta$ and $\sec \theta$ undefined when $\cos \theta = 0$
  - $\cot \theta$ and $\csc \theta$ undefined when $\sin \theta = 0$
- Radians are the default unit in calculus formulas.

## Main Result / Formula

### Degree–radian conversion

$$
180^\circ = \pi \text{ rad}, \qquad
\theta_{\mathrm{rad}} = \theta^\circ \cdot \frac{\pi}{180}, \qquad
\theta^\circ = \theta_{\mathrm{rad}} \cdot \frac{180}{\pi}.
$$

A full turn is $360^\circ = 2\pi$ rad.

### Fundamental identity

For every $\theta$ where sine and cosine are defined (always for real $\theta$),

$$
\sin^2 \theta + \cos^2 \theta = 1.
$$

Dividing by $\cos^2 \theta$ or $\sin^2 \theta$ (where allowed) yields

$$
1 + \tan^2 \theta = \sec^2 \theta, \qquad
1 + \cot^2 \theta = \csc^2 \theta.
$$

### Six ratios via sine and cosine

$$
\tan \theta = \frac{\sin \theta}{\cos \theta}, \quad
\cot \theta = \frac{\cos \theta}{\sin \theta}, \quad
\sec \theta = \frac{1}{\cos \theta}, \quad
\csc \theta = \frac{1}{\sin \theta}.
$$

### Domains and ranges (real functions, principal conventions)

| Function | Domain (radians) | Range |
|---|---|---|
| $\sin \theta$ | $\mathbb{R}$ | $[-1,1]$ |
| $\cos \theta$ | $\mathbb{R}$ | $[-1,1]$ |
| $\tan \theta$ | $\mathbb{R} \setminus \{\tfrac{\pi}{2}+k\pi : k\in\mathbb{Z}\}$ | $\mathbb{R}$ |
| $\csc \theta$ | $\mathbb{R} \setminus \{k\pi : k\in\mathbb{Z}\}$ | $(-\infty,-1]\cup[1,\infty)$ |
| $\sec \theta$ | $\mathbb{R} \setminus \{\tfrac{\pi}{2}+k\pi : k\in\mathbb{Z}\}$ | $(-\infty,-1]\cup[1,\infty)$ |
| $\cot \theta$ | $\mathbb{R} \setminus \{k\pi : k\in\mathbb{Z}\}$ | $\mathbb{R}$ |

Periodicity: $\sin$ and $\cos$ have period $2\pi$; $\tan$ and $\cot$ have period $\pi$.

### Common angles

| $\theta$ (deg) | $\theta$ (rad) | $\sin \theta$ | $\cos \theta$ | $\tan \theta$ |
|---|---|---|---|---|
| $0^\circ$ | $0$ | $0$ | $1$ | $0$ |
| $30^\circ$ | $\pi/6$ | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ |
| $45^\circ$ | $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| $60^\circ$ | $\pi/3$ | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |
| $90^\circ$ | $\pi/2$ | $1$ | $0$ | undefined |
| $180^\circ$ | $\pi$ | $0$ | $-1$ | $0$ |
| $270^\circ$ | $3\pi/2$ | $-1$ | $0$ | undefined |
| $360^\circ$ | $2\pi$ | $0$ | $1$ | $0$ |

Signs by quadrant (ASTC): All positive in Q1; sine (and csc) positive in Q2; tangent (and cot) positive in Q3; cosine (and sec) positive in Q4.

## Worked Example

Evaluate $\sin(150^\circ)$ and $\cos(5\pi/3)$.

1. $150^\circ = 180^\circ - 30^\circ$ is in Q2, reference angle $30^\circ$:
   $$
   \sin 150^\circ = \sin 30^\circ = \tfrac{1}{2}.
   $$
2. $5\pi/3$ is in Q4, reference angle $\pi/3$:
   $$
   \cos\Bigl(\frac{5\pi}{3}\Bigr) = +\cos\Bigl(\frac{\pi}{3}\Bigr) = \tfrac{1}{2}.
   $$

## Common Mistakes

- Using degrees in calculus formulas that assume radians.
- Writing $\sin^{-1}$ for $1/\sin$ instead of arcsine (prefer $\arcsin$ or $\csc$).
- Forgetting undefined points of $\tan$ and $\sec$.
- Dropping signs when using reference angles outside Q1.

## Connections

- Related: [[Functions]], [[Exponentials and Logarithms]]
- Geometry links: [[Distance and Midpoint]], [[Vectors and Dot Product]]
- Next: limits and derivatives of trig functions in [[Calculus]]

## References

Unit circle, trig ratios, identities, and common values follow OpenStax Precalculus trigonometry chapters.[^openstax-trig]

[^openstax-trig]: OpenStax, *Precalculus 2e*, Trigonometric Functions, https://openstax.org/details/books/precalculus-2e
