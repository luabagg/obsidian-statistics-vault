# Design Guide — Statistics Learning Vault

This file defines the visual and structural standard for all generated content in the vault. Agents creating videos, diagrams, or notes must follow these conventions.

## Manim Videos

### When to create a video

Create a Manim animation only when motion materially reduces the text needed to explain a concept. Good candidates:

- Iterative processes where each step builds on the last (bisection, Newton-Raphson, trapezoidal refinement)
- Continuous parameter changes that reshape a distribution or function
- Geometric constructions where static diagrams fail to show the process

Do NOT create a video when a single static figure or a few lines of prose suffices.

### Directory structure

Every video lives under `Videos/` with this layout:

```
Videos/<Topic Name>/
  plan.md          # teaching goal, narrative arc, visual language
  script.py        # Manim scene class, runnable as-is
  <TopicName>.mp4  # rendered output (committed to git)
```

### plan.md format

Each plan must include:

- **Teaching goal**: one sentence on what misconception or difficulty the animation resolves.
- **Narrative arc**: numbered steps describing what the viewer sees, in order.
- **Visual language**: color palette, font choices, and any constraints (e.g. "no LaTeX").
- **Verification**: how to confirm the render is correct before linking.

### script.py conventions

1. **Framework**: Manim Community Edition (ManimCE). Import with `from manim import *`.
2. **No LaTeX**: use `Text(...)` not `MathTex(...)` or `Tex(...)`. The vault environment has no TeX installation.
3. **Colors**: dark charcoal background (`#1C1C1C`). Use the established palette:
   - `#58C4DD` blue — curves, axes constructs
   - `#FFFF00` yellow — active elements, brackets, highlights
   - `#FF6B6B` red — intermediate points, warnings
   - `#83C167` green — final results, accepted values, conclusions
   - `#888888` muted gray — axes, grid lines, reference elements
4. **Font**: `DejaVu Sans Mono` for all text labels.
5. **Timing**: total video 15-25 seconds. Use `run_time` per animation and `self.wait()` for pauses. The viewer needs time to read each label.
6. **Positioning**: check that no text clips off-screen. Use `.to_edge()`, `.next_to()`, and `VGroup.arrange()` for layout. Avoid absolute coordinates.
7. **Scene transitions**: prefer `ReplacementTransform` for morphing between steps (e.g. bracket shrinking). Use `FadeIn`/`FadeOut` for elements that appear or disappear.
8. **Closing**: end with a concise conclusion (1-2 lines) stating the key takeaway or formula, in green.

### Rendering

```bash
# Quick preview (low quality, fast)
manim -ql "Videos/<Topic>/script.py" <SceneName>

# Final render (1080p60)
manim -qh "Videos/<Topic>/script.py" <SceneName>
```

Manim is at `/home/luanb/development/manim/.venv/bin/manim` (ManimCE v0.20.1).
FFmpeg is at `/usr/bin/ffmpeg`.
LaTeX is NOT installed — do not use TeX-based Mobjects.

### Verification

1. Render at low quality (`-ql`) first.
2. Inspect the final frame for clipping, overlap, or readability issues.
3. Render at high quality (`-qh`) only after the preview looks correct.
4. Commit the MP4, `plan.md`, and `script.py` to git.
5. Embed the video in the relevant note using `![[TrapezoidalRule.mp4]]`.

## Note Structure Standard

All instructional notes follow the templates in `Templates/`. Key rules:

- Frontmatter with `dg-publish: true` and English aliases.
- Sections: Summary, Prerequisites, Definition, Notation/Assumptions, Essential Result, Worked Example, Common Mistakes, Connections (with wikilinks), References (footnotes).
- Each note names prerequisites at the top and next steps in Connections.
- References use Markdown footnotes (`[^id]`) citing authoritative sources (OpenStax, NIST, MIT OCW, DLMF).
- No Portuguese prose in instructional notes.
- File and directory names in English.

## Validation

Run `python3 scripts/validate_vault.py --max-examples 120` before committing. Target: 0 findings.

Run `uv run --with numpy --with sympy python scripts/verify_math_examples.py` to verify worked examples. Target: all checks pass.