# 貢獻指南

感謝你參與 oss-gate-sandbox。

## 提交前

1. 先搜尋是否已有相同 Issue 或 Pull Request。
2. 一般問題使用 Discussion／Issue；安全問題依 `SECURITY.md` 私密通報。
3. 大型功能先開 Feature Request，確認方向後再投入實作。

## 開發環境

```text
git clone https://github.com/kino-labs/oss-gate-sandbox.git
cd oss-gate-sandbox
# 只用標準函式庫，不需要安裝 dependency
```

## 測試與格式

```text
python -m compileall sandbox_tool.py
python sandbox_tool.py examples/sample.json
```

PR 必須：

- 說明改了什麼及為什麼。
- 包含適當測試與文件。
- 通過 repository 的自動檢查。
- 若新增、移除或升級相依，一併重新產生並提交 `sbom.cdx.json`（做法見 `README.md`）。
- 不含 Secret、個資、內部網址、客戶資料或未公開功能。
- 同意貢獻會依本專案 License 發布。

## Review

Maintainer 可能要求修改、拆小 PR 或補充測試。提交 PR 不代表一定會合併；方向與支援範圍由 `GOVERNANCE.md` 說明。

