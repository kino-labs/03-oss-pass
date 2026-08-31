#!/usr/bin/env python3
"""Fail if required open-source files are missing. No LLM required."""

from __future__ import annotations

from pathlib import Path
import sys

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "CHANGELOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    "docs/FAQ.md",
]

PLACEHOLDER_MARKERS = ("[請填寫", "your-org", "your-repo")
FORBIDDEN_FILES = ("TEMPLATE_USAGE.md", ".env")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).exists()]
    if missing:
        print("缺少必要檔案：")
        for path in missing:
            print(f"  - {path}")
        return 1

    forbidden = [rel for rel in FORBIDDEN_FILES if (root / rel).exists()]
    if forbidden:
        print("公開前必須移除內部範本／環境檔：")
        for path in forbidden:
            print(f"  - {path}")
        return 1

    placeholders: list[str] = []
    for rel in REQUIRED_FILES:
        path = root / rel
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(marker in text for marker in PLACEHOLDER_MARKERS):
            placeholders.append(rel)

    if placeholders:
        print("以下必要檔案仍含範本 placeholder：")
        for path in placeholders:
            print(f"  - {path}")
        return 1

    print("必要開源檔案都在，且未發現已知 placeholder。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
