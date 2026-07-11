from manim import *

BG = "#1C1C1C"
BLUE = "#58C4DD"
YELLOW = "#FFFF00"
RED = "#FF6B6B"
GREEN = "#83C167"
MUTED = "#888888"
MONO = "DejaVu Sans Mono"


class TrapezoidalRule(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Title ──
        title = Text(
            "Trapezoidal Rule",
            font=MONO, font_size=34, color=BLUE,
        ).to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.0)
        self.wait(0.4)

        # ── Axes ──
        f = lambda x: 0.45 * x ** 2 + 0.3
        a_val, b_val = 0.5, 3.5

        axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 6.0, 2],
            x_length=7.0,
            y_length=4.5,
            axis_config={"color": MUTED, "stroke_opacity": 0.65},
            tips=False,
        ).shift(LEFT * 1.4 + DOWN * 0.4)

        curve = axes.plot(f, x_range=[a_val, b_val], color=BLUE, stroke_width=3)

        # Exact area (green fill under curve)
        exact_area = axes.get_area(
            curve, x_range=[a_val, b_val], color=GREEN, opacity=0.25
        )

        self.play(Create(axes), Create(curve), run_time=1.5)
        self.play(FadeIn(exact_area), run_time=0.8)
        exact_label = Text(
            "exact area", font=MONO, font_size=18, color=GREEN,
        ).next_to(exact_area, RIGHT, buff=0.15)
        self.play(Write(exact_label), run_time=0.6)
        self.wait(0.8)

        # ── Helper: build trapezoids for n subintervals ──
        def make_trapes(n):
            h = (b_val - a_val) / n
            xs = [a_val + i * h for i in range(n + 1)]
            ys = [f(x) for x in xs]

            traps = VGroup()
            tops = VGroup()
            for i in range(n):
                p1 = axes.c2p(xs[i], 0)
                p2 = axes.c2p(xs[i], ys[i])
                p3 = axes.c2p(xs[i + 1], ys[i + 1])
                p4 = axes.c2p(xs[i + 1], 0)
                poly = Polygon(p1, p2, p3, p4, color=YELLOW, fill_color=YELLOW, fill_opacity=0.20, stroke_width=2)
                top = Line(p2, p3, color=YELLOW, stroke_width=3)
                traps.add(poly)
                tops.add(top)

            dots = VGroup()
            for x, y in zip(xs, ys):
                dots.add(Dot(axes.c2p(x, y), color=YELLOW, radius=0.06))

            return traps, tops, dots

        # ── Step 1: single trapezoid (n=1) ──
        traps1, tops1, dots1 = make_trapes(1)
        step1_label = Text(
            "1 trapezoid: rough fit",
            font=MONO, font_size=19, color=YELLOW,
        ).to_edge(DOWN, buff=0.45)

        self.play(
            FadeOut(exact_area), FadeOut(exact_label),
            FadeIn(traps1), Create(tops1), FadeIn(dots1),
            Write(step1_label),
            run_time=1.5,
        )
        self.wait(1.0)

        # ── Step 2: two trapezoids (n=2) ──
        traps2, tops2, dots2 = make_trapes(2)
        step2_label = Text(
            "2 trapezoids: closer",
            font=MONO, font_size=19, color=YELLOW,
        ).to_edge(DOWN, buff=0.45)

        self.play(
            ReplacementTransform(traps1, traps2),
            ReplacementTransform(tops1, tops2),
            ReplacementTransform(dots1, dots2),
            ReplacementTransform(step1_label, step2_label),
            run_time=1.2,
        )
        self.wait(1.0)

        # ── Step 3: four trapezoids (n=4) ──
        traps4, tops4, dots4 = make_trapes(4)
        step4_label = Text(
            "4 trapezoids: nearly exact",
            font=MONO, font_size=19, color=YELLOW,
        ).to_edge(DOWN, buff=0.45)

        self.play(
            ReplacementTransform(traps2, traps4),
            ReplacementTransform(tops2, tops4),
            ReplacementTransform(dots2, dots4),
            ReplacementTransform(step2_label, step4_label),
            run_time=1.2,
        )
        self.wait(1.0)

        # Fade trapezoids, bring back exact area for comparison
        self.play(
            FadeOut(traps4), FadeOut(tops4), FadeOut(dots4),
            FadeOut(step4_label),
            FadeIn(exact_area), run_time=1.0,
        )
        self.wait(0.5)

        # ── Formula ──
        formula = VGroup(
            Text("T_n = (h/2) [ f(x_0) + 2f(x_1) + ... + 2f(x_{n-1}) + f(x_n) ]",
                 font=MONO, font_size=18, color=GREEN),
            Text("error halves each time n doubles",
                 font=MONO, font_size=16, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        formula.next_to(exact_area, RIGHT, buff=0.2).shift(UP * 0.3)

        self.play(Write(formula), run_time=1.5)
        self.wait(2.5)