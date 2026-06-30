#!/usr/bin/env python3
"""Count characters in 4 patterns: newline x space inclusion/exclusion."""
import sys

SPACE_CHARS = (" ", "　", "\t")  # half-width space, full-width space, tab
NEWLINE_CHARS = ("\n", "\r")


def strip_chars(text: str, chars: tuple[str, ...]) -> str:
    return "".join(c for c in text if c not in chars)


def count_all_patterns(text: str) -> dict[str, int]:
    no_newline = strip_chars(text, NEWLINE_CHARS)
    no_space = strip_chars(text, SPACE_CHARS)
    no_newline_no_space = strip_chars(no_newline, SPACE_CHARS)
    return {
        "改行含む・スペース含む": len(text),
        "改行含む・スペース除く": len(no_space),
        "改行除く・スペース含む": len(no_newline),
        "改行除く・スペース除く": len(no_newline_no_space),
    }


def main() -> None:
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    counts = count_all_patterns(text)
    print("| 種類 | 文字数 |")
    print("|---|---|")
    for label, count in counts.items():
        print(f"| {label} | {count} |")


if __name__ == "__main__":
    main()
