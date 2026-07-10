from manim import *

BG = "#1C1C1C"
BLUE = "#58C4DD"
YELLOW = "#FFFF00"
RED = "#FF6B6B"
GREEN = "#83C167"
MUTED = "#888888"
MONO = "DejaVu Sans Mono"


class BisectionConvergence(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "Bisection: certainty from a bracket",
            font=MONO,
            font_size=34,
            color=BLUE,
        ).to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.2)
        self.wait(0.8)

        axes = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[-2.5, 6.5, 2],
            x_length=7.0,
            y_length=5.0,
            axis_config={"color": MUTED, "stroke_opacity": 0.65},
            tips=False,
        ).shift(LEFT * 1.25 + DOWN * 0.25)
        curve = axes.plot(lambda x: x**3 - 2, x_range=[0.55, 2.05], color=BLUE)
        zero = DashedLine(
            axes.c2p(0, 0), axes.c2p(2.2, 0), color=MUTED, stroke_opacity=0.6
        )
        root_x = 2 ** (1 / 3)
        root = Dot(axes.c2p(root_x, 0), color=GREEN, radius=0.09)
        root_label = Text("root ≈ 1.26", font=MONO, font_size=20, color=GREEN)
        root_label.next_to(root, UP + RIGHT, buff=0.12)
        self.play(Create(axes), Create(zero), Create(curve), run_time=1.8)
        self.play(FadeIn(root), Write(root_label), run_time=0.8)
        self.wait(0.8)

        side = VGroup(
            Text("Invariant", font=MONO, font_size=24, color=YELLOW),
            Text("continuous f", font=MONO, font_size=20),
            Text("f(a) and f(b) have opposite signs", font=MONO, font_size=18),
            Text("→ a root remains inside [a, b]", font=MONO, font_size=18, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.35).shift(UP * 1.0)
        self.play(FadeIn(side, shift=LEFT), run_time=1.2)
        self.wait(1.0)

        intervals = [
            (1.0, 2.0, "f(1) < 0 < f(2)"),
            (1.0, 1.5, "midpoint 1.50 has f(mid) > 0"),
            (1.25, 1.5, "midpoint 1.25 has f(mid) < 0"),
            (1.25, 1.375, "midpoint 1.375 has f(mid) > 0"),
            (1.25, 1.3125, "the bracket keeps halving"),
        ]
        previous = None
        for step, (left, right, explanation) in enumerate(intervals):
            mid = (left + right) / 2
            bracket = Line(
                axes.c2p(left, 0), axes.c2p(right, 0),
                color=YELLOW, stroke_width=8,
            )
            left_dot = Dot(axes.c2p(left, 0), color=YELLOW, radius=0.07)
            right_dot = Dot(axes.c2p(right, 0), color=YELLOW, radius=0.07)
            midpoint = Dot(axes.c2p(mid, 0), color=RED, radius=0.1)
            label = Text(
                f"step {step}: [{left:g}, {right:g}]",
                font=MONO,
                font_size=19,
                color=YELLOW,
            ).to_edge(DOWN, buff=0.45)
            note = Text(explanation, font=MONO, font_size=17, color=RED)
            note.next_to(side, DOWN, buff=0.35).align_to(side, LEFT)
            current = VGroup(bracket, left_dot, right_dot, midpoint, label, note)
            if previous is None:
                self.play(Create(bracket), FadeIn(left_dot), FadeIn(right_dot), FadeIn(midpoint), Write(label), Write(note), run_time=1.2)
            else:
                self.play(ReplacementTransform(previous, current), run_time=1.2)
            self.wait(0.9)
            previous = current

        assert previous is not None
        bound = Text(
            "After n steps: width = (b − a) / 2^n",
            font=MONO,
            font_size=24,
            color=GREEN,
        ).to_edge(DOWN, buff=0.45)
        conclusion = VGroup(
            Text("The guarantee comes from", font=MONO, font_size=18, color=GREEN),
            Text("the bracket, not a lucky guess.", font=MONO, font_size=18, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        conclusion.next_to(side, DOWN, buff=0.35).align_to(side, LEFT)
        self.play(ReplacementTransform(previous, VGroup(bound, conclusion)), run_time=1.3)
        self.wait(2.5)
