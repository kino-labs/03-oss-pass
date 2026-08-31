# 專案治理

## 決策方式

- Project Owner Team：`kino-labs/oss-maintainers`
- 日常 Bug fix、文件與 dependency update 由 Maintainers review。
- 破壞性變更、支援範圍、Roadmap、License、商標及 EOL 由 Project Owner 決定。
- 法律／智財問題由 Owner 先確認；Owner 不確定或屬高風險時再升級法務／智財。
- 安全例外與公開時間不可由 AI Agent 自行核准。

## Maintainer

Maintainer 必須持續提供有效 review、遵守行為準則及保護敏感資訊。新增或移除 Maintainer 由 Project Owner Team 決定，並更新 `MAINTAINERS.md` 與 CODEOWNERS。

## 變更提案

大型功能或破壞性變更先建立 Feature Request／設計提案，說明使用情境、相容性、替代方案、測試與文件影響。

## 發布與停止維護

- 版本方式：Semantic Versioning 2.0.0
- Release 核准方式：由 Project Owner Team 於每次 Release 核准
- EOL 會提前公告支援截止日與替代方案。
- 封存由 Project Owner 與流程管理者決定；Agent 只能建立 EOL Review。

