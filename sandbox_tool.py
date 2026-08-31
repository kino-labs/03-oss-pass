#!/usr/bin/env python3
"""Flatten a JSON file into dotted key=value lines.

Deliberately trivial and dependency-free: this repository exists to give the
open-source gate something real to clone, scan, and build an SBOM from, not to
be useful software.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterator


def flatten(value: Any, prefix: str = "") -> Iterator[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from flatten(item, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from flatten(item, f"{prefix}.{index}" if prefix else str(index))
    else:
        yield prefix, value


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("用法：python sandbox_tool.py <path-to-json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"找不到檔案：{path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"JSON 格式錯誤：{exc}", file=sys.stderr)
        return 1

    for key, value in flatten(data):
        print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
