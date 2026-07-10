# Contributing

This vault is being rewritten as a concise English learning center. Favor correctness, short notes, explicit assumptions, and source-backed formulas over coverage volume.[^nist-handbook]

## Compact Note Contract

- Use one focused concept per note.
- Write instructional prose in clear English.
- Put prerequisites near the top. Use `Prerequisites: None` only when that is true.
- Define notation before using it.
- State assumptions before formulas, theorems, algorithms, or interpretations.
- Include only sections that improve understanding.
- Add one worked example when it teaches a method or prevents a common error.
- Put next steps and related links near the bottom.
- Cite every finished note with Markdown footnotes.

## Footnote References

Use inline citations and footnote definitions:

```markdown
The normal density integrates to one under its usual parameter constraints.[^normal-source]

[^normal-source]: NIST/SEMATECH e-Handbook of Statistical Methods, "Normal Distribution", https://www.itl.nist.gov/div898/handbook/
```

References must include a source title plus URL, DOI, or ISBN. Do not use a bare link list, invented sources, or uncited bibliography entries.

## Hub Notes

Hub notes should guide navigation. They may contain:

- A short purpose statement.
- A learning order.
- Prerequisites for the path.
- Links to child notes.
- Brief notes on where to go next.

Hub notes should not repeat child-note formulas, proofs, or long examples.

## Video Rule

Add a Manim explainer only when motion replaces substantial prose: convergence, geometric motion, sampling behavior, or changing approximations. If a static formula or diagram is clearer, do not add a video.[^manim-docs]

## Validation

Run the vault validator before committing note rewrites:

```bash
python scripts/validate_vault.py
```

For migration baselines, save reports outside the vault, for example:

```bash
python scripts/validate_vault.py > /tmp/statistics-vault-baseline.txt
```

[^nist-handbook]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, https://www.itl.nist.gov/div898/handbook/
[^manim-docs]: Manim Community, *Manim Community Documentation*, https://docs.manim.community/
