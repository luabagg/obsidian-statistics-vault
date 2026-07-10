#!/usr/bin/env python3
"""Validate migration readiness for the statistics learning vault."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


EXCLUDED_SCAN_DIRS = {
    ".git",
    ".hermes",
    ".obsidian",
    ".superpowers",
    "Copilot Custom Prompts",
    "Excalidraw",
    "Templates",
}
UTILITY_MARKDOWN = {
    "README.md",
    "CONTRIBUTING.md",
    "LEARNING_PATHS.md",
    "adjust-info.md",
}
PLACEHOLDER_RE = re.compile(
    r"TODO_TEMPLATE\b|\{\{[^}\n]+\}\}|<([A-Za-z][A-Za-z0-9 _./-]{1,60})>"
)
HTML_TAGS = {
    "a",
    "br",
    "code",
    "div",
    "em",
    "img",
    "li",
    "ol",
    "p",
    "span",
    "strong",
    "sub",
    "sup",
    "table",
    "td",
    "th",
    "tr",
    "ul",
}
WIKILINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")
FOOTNOTE_CITATION_RE = re.compile(r"(?<!\^)\[\^([^\]\s]+)\]")
FOOTNOTE_DEFINITION_RE = re.compile(r"^\[\^([^\]\s]+)\]:", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PORTUGUESE_WORD_RE = re.compile(
    r"\b("
    r"a|ao|aos|as|com|como|da|das|de|do|dos|e|em|entre|esta|este|"
    r"fun[cç][aã]o|m[eé]dia|m[eé]todo|n[aã]o|onde|para|por|probabilidade|"
    r"quando|que|seja|teorema|uma|vari[aá]vel"
    r")\b",
    re.IGNORECASE,
)
ACCENT_RE = re.compile(r"[ãõáéíóúâêôàç]")


@dataclass(frozen=True)
class Finding:
    code: str
    path: Path
    line: int
    message: str


@dataclass(frozen=True)
class ValidationResult:
    root: Path
    checked_markdown: int
    instructional_markdown: int
    findings: tuple[Finding, ...]


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in {".git", ".obsidian"} for part in rel.parts):
            continue
        yield rel


def iter_markdown(root: Path) -> Iterable[Path]:
    for rel in iter_files(root):
        if rel.suffix.lower() != ".md":
            continue
        if any(part in EXCLUDED_SCAN_DIRS for part in rel.parts[:-1]):
            continue
        yield rel


def is_instructional(rel: Path) -> bool:
    if rel.name in UTILITY_MARKDOWN:
        return False
    if rel.name.endswith(".excalidraw.md"):
        return False
    return True


def read_text(root: Path, rel: Path) -> str:
    return (root / rel).read_text(encoding="utf-8", errors="replace")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    return text[end + 5 :]


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def build_file_index(root: Path) -> tuple[set[str], dict[str, set[str]], dict[str, set[str]]]:
    all_paths: set[str] = set()
    markdown_stems: dict[str, set[str]] = {}
    no_ext_paths: dict[str, set[str]] = {}

    for rel in iter_files(root):
        normalized = rel.as_posix()
        all_paths.add(normalized)
        no_ext_paths.setdefault(rel.with_suffix("").as_posix(), set()).add(normalized)
        if rel.suffix.lower() == ".md":
            markdown_stems.setdefault(rel.stem, set()).add(normalized)

    return all_paths, markdown_stems, no_ext_paths


def normalize_wikilink(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target.lstrip("/")


def wikilink_exists(
    target: str,
    all_paths: set[str],
    markdown_stems: dict[str, set[str]],
    no_ext_paths: dict[str, set[str]],
) -> bool:
    if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.IGNORECASE):
        return True
    target_path = Path(target)
    target_posix = target_path.as_posix()
    if target_posix in all_paths:
        return True
    if target_path.suffix:
        if f"{target_posix}.md" in all_paths:
            return True
        target_markdown_name = f"{target_path.name}.md"
        if target_markdown_name in {Path(path).name for path in all_paths}:
            return True
        return Path(target_posix).name in {Path(path).name for path in all_paths}
    if f"{target_posix}.md" in all_paths:
        return True
    if target_posix in no_ext_paths:
        return True
    return target_path.name in markdown_stems


def section_body(text: str, heading_name: str) -> str:
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        if match.group(2).strip().lower() != heading_name.lower():
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        return text[start:end]
    return ""


def is_effectively_empty(body: str) -> bool:
    cleaned = strip_code_blocks(body)
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"[-*_`#>\s|:]+", "", cleaned)
    cleaned = cleaned.replace("TODO_TEMPLATE", "")
    return cleaned == ""


def validate_wikilinks(
    rel: Path,
    text: str,
    all_paths: set[str],
    markdown_stems: dict[str, set[str]],
    no_ext_paths: dict[str, set[str]],
) -> list[Finding]:
    findings: list[Finding] = []
    for match in WIKILINK_RE.finditer(text):
        target = normalize_wikilink(match.group(1))
        if wikilink_exists(target, all_paths, markdown_stems, no_ext_paths):
            continue
        findings.append(
            Finding(
                "broken-wikilink",
                rel,
                line_number(text, match.start()),
                f"[[{target}]] does not resolve",
            )
        )
    return findings


def validate_placeholders(rel: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    searchable = strip_code_blocks(strip_frontmatter(text))
    for match in PLACEHOLDER_RE.finditer(searchable):
        token = match.group(0)
        tag = match.group(1)
        if tag and tag.lower().strip("/ ") in HTML_TAGS:
            continue
        findings.append(
            Finding(
                "template-placeholder",
                rel,
                line_number(searchable, match.start()),
                f"unresolved placeholder {token!r}",
            )
        )
    return findings


def validate_references(rel: Path, text: str) -> list[Finding]:
    citations = set(FOOTNOTE_CITATION_RE.findall(text))
    definitions = set(FOOTNOTE_DEFINITION_RE.findall(text))
    if citations and definitions and citations <= definitions:
        return []
    if not citations or not definitions:
        return [Finding("missing-references", rel, 1, "missing footnote citation or definition")]
    missing = ", ".join(sorted(citations - definitions))
    return [Finding("missing-references", rel, 1, f"missing footnote definitions for: {missing}")]


def validate_connections(rel: Path, text: str) -> list[Finding]:
    body = section_body(text, "Connections")
    if not body:
        return [Finding("missing-connections", rel, 1, "missing ## Connections section")]
    if not WIKILINK_RE.search(body):
        line = line_number(text, text.find(body)) if body else 1
        return [Finding("missing-connections", rel, line, "Connections section has no wikilinks")]
    return []


def validate_empty_sections(rel: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        if is_effectively_empty(body):
            findings.append(
                Finding(
                    "empty-section",
                    rel,
                    line_number(text, match.start()),
                    f"section '{match.group(2).strip()}' is empty",
                )
            )
    return findings


def validate_english(rel: Path, text: str) -> list[Finding]:
    body = strip_code_blocks(strip_frontmatter(text))
    references_start = re.search(r"^##\s+References\s*$", body, flags=re.MULTILINE | re.IGNORECASE)
    if references_start:
        body = body[: references_start.start()]

    hits: list[tuple[int, str]] = []
    for line_index, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith(("$$", "|", "- [", "[^")):
            continue
        word_hits = PORTUGUESE_WORD_RE.findall(stripped)
        accent_hit = ACCENT_RE.search(stripped.lower())
        if len(word_hits) >= 2 or (word_hits and accent_hit):
            hits.append((line_index, stripped[:100]))
    if not hits:
        return []
    line, sample = hits[0]
    return [Finding("non-english-prose", rel, line, f"Portuguese prose heuristic matched: {sample!r}")]


def validate(root: Path) -> ValidationResult:
    root = root.resolve()
    all_paths, markdown_stems, no_ext_paths = build_file_index(root)
    markdown_files = sorted(iter_markdown(root))
    findings: list[Finding] = []
    instructional_count = 0

    for rel in markdown_files:
        text = read_text(root, rel)
        findings.extend(validate_wikilinks(rel, text, all_paths, markdown_stems, no_ext_paths))
        if not is_instructional(rel):
            continue
        instructional_count += 1
        findings.extend(validate_placeholders(rel, text))
        findings.extend(validate_references(rel, text))
        findings.extend(validate_connections(rel, text))
        findings.extend(validate_empty_sections(rel, text))
        findings.extend(validate_english(rel, text))

    findings.sort(key=lambda item: (item.code, item.path.as_posix(), item.line, item.message))
    return ValidationResult(root, len(markdown_files), instructional_count, tuple(findings))


def format_report(result: ValidationResult, max_examples: int) -> str:
    lines = [
        "Vault validation report",
        f"Root: {result.root}",
        f"Checked markdown files: {result.checked_markdown}",
        f"Instructional markdown files: {result.instructional_markdown}",
        f"Findings: {len(result.findings)}",
    ]
    if result.findings:
        lines.append("")
        lines.append("By code:")
        for code, count in sorted(Counter(finding.code for finding in result.findings).items()):
            lines.append(f"- {code}: {count}")
        lines.append("")
        shown = result.findings[:max_examples]
        lines.append(f"Examples (first {len(shown)} of {len(result.findings)}):")
        for finding in shown:
            lines.append(
                f"- {finding.code}: {finding.path.as_posix()}:{finding.line} - {finding.message}"
            )
    else:
        lines.append("")
        lines.append("No findings.")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="vault root to validate")
    parser.add_argument("--max-examples", type=int, default=40, help="maximum findings to print")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = validate(Path(args.root))
    print(format_report(result, max(0, args.max_examples)))
    return 1 if result.findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
