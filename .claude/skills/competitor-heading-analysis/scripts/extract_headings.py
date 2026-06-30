#!/usr/bin/env python3
"""Extract H1-H6 heading structure from an HTML document.

Usage:
    python extract_headings.py path/to/page.html
    cat page.html | python extract_headings.py
"""
import re
import sys

HEADING_RE = re.compile(r"<h([1-6])\b[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def clean_text(raw: str) -> str:
    text = TAG_RE.sub("", raw)
    return re.sub(r"\s+", " ", text).strip()


def extract_headings(html: str) -> list[tuple[int, str]]:
    headings = []
    for match in HEADING_RE.finditer(html):
        level = int(match.group(1))
        text = clean_text(match.group(2))
        if text:
            headings.append((level, text))
    return headings


def main() -> None:
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8", errors="ignore") as f:
            html = f.read()
    else:
        html = sys.stdin.read()

    headings = extract_headings(html)
    if not headings:
        print("見出し（h1〜h6）が見つかりませんでした。")
        return

    print("| レベル | 見出しテキスト |")
    print("|---|---|")
    for level, text in headings:
        indent = "　" * (level - 1)
        print(f"| H{level} | {indent}{text} |")


if __name__ == "__main__":
    main()
