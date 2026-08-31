#!/usr/bin/env python3
"""Verify the committed CycloneDX SBOM still matches the installed dependencies.

The committed SBOM is what the company check agent reads, so it has to be
regenerated whenever dependencies change — the same discipline as a lock file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def load_components(path: Path) -> list[dict[str, Any]]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"找不到 SBOM：{path}。請先產生並提交 sbom.cdx.json。")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"SBOM JSON 格式錯誤（{path}）：{exc}")
    if str(document.get("bomFormat") or "") != "CycloneDX":
        raise SystemExit(f"{path} 缺少 bomFormat: CycloneDX。")
    components = document.get("components") or []
    if not isinstance(components, list):
        raise SystemExit(f"{path} 的 components 必須是 array。")
    return [item for item in components if isinstance(item, dict)]


# syft catalogs GitHub Actions as `pkg:github/...`. They are CI tooling, never
# shipped with the product, and carry no license metadata.
NON_DISTRIBUTED_PURL_PREFIXES = ("pkg:github/",)


def packages(components: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Index shipped dependencies by purl; `file` and CI-only entries are not."""
    result: dict[str, dict[str, Any]] = {}
    for component in components:
        if str(component.get("type") or "") != "library":
            continue
        purl = str(component.get("purl") or "").strip()
        key = purl.split("?")[0].split("#")[0].casefold() if purl else ""
        if key.startswith(NON_DISTRIBUTED_PURL_PREFIXES):
            continue
        if not key:
            key = "name:" + str(component.get("name") or "").strip().casefold()
        if key.strip(":"):
            result[key] = component
    return result


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("用法：python scripts/check_sbom.py <committed> <generated>")

    committed = packages(load_components(Path(sys.argv[1])))
    generated = packages(load_components(Path(sys.argv[2])))

    missing = sorted(set(generated) - set(committed))
    unlicensed = sorted(key for key, item in committed.items() if not item.get("licenses"))

    if missing:
        print("提交的 SBOM 漏列了已安裝的相依：")
        for key in missing:
            print(f"  - {key}")
        print("請重新產生 sbom.cdx.json 並一併提交。")

    if unlicensed:
        print("提交的 SBOM 有元件沒有 License 資訊：")
        for key in unlicensed:
            print(f"  - {key}")
        print("多半是 SBOM 掃了原始碼而不是已安裝的相依；License 只存在於套件 metadata。")

    if missing or unlicensed:
        return 1
    print(f"SBOM 涵蓋 {len(committed)} 個相依，且都帶有 License 資訊。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
