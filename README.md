# oss-gate-sandbox

這個 repository 存在的唯一目的，是讓 `kino-labs` 的開源治理閘門有地方被真的跑一次。它刻意保持極小：一支不依賴外部服務的 Python 工具，加上一整套開源專案該有的必備檔案，讓檢核 Agent 的每個閘門都有東西可以檢查。

**這不是產品。** 不要拿它當作任何功能的參考實作，也不要在正式環境依賴它。它不連線任何公司內部服務，不讀寫任何內部資料。

## 功能

- `sandbox_tool.py`：把一份 JSON 檔案的鍵值攤平成單層，用來當作被檢核的實際程式碼。
- 完整的開源必備檔案，供 `open-source-gate` 的必要檔案閘門驗證。

## 支援版本

| 專案版本 | 執行環境 | 支援狀態 |
|---|---|---|
| 0.1.x | Python 3.10 以上 | Supported |

## 安裝

```text
git clone https://github.com/kino-labs/oss-gate-sandbox.git
cd oss-gate-sandbox
```

不需要安裝任何 dependency，只用 Python 標準函式庫。

## 快速開始

```text
python sandbox_tool.py examples/sample.json
```

預期結果：

```text
service.name=gate-sandbox
service.port=8080
tags.0=demo
```

## 設定與資料

- 需要的環境變數：無。
- 是否連線外部服務：否，完全離線執行。
- 遙測預設：無，不收集任何使用資料。
- 收集或傳送的資料：無。

## 文件

- [FAQ](docs/FAQ.md)
- [貢獻方式](CONTRIBUTING.md)
- [支援範圍](SUPPORT.md)
- [安全通報](SECURITY.md)
- [治理方式](GOVERNANCE.md)

## 問題回報

- 一般問題或 Bug：使用 GitHub Issue Forms。
- 安全漏洞、Secret 或個資：不要建立公開 Issue，請依 [SECURITY.md](SECURITY.md) 私密通報。

## 相依清單（SBOM）

本 repository 提交 `sbom.cdx.json`（CycloneDX），列出所有第三方相依與其 License。本專案只用 Python 標準函式庫，所以元件清單是空的——**沒有相依也要提交**，讓「沒有」是明確聲明而不是漏檔。

日後若加入任何第三方套件，安裝後重新產生並一併提交：

```bash
syft scan dir:<已安裝相依的路徑> -o cyclonedx-json=sbom.cdx.json
```

路徑要指向安裝後的位置，不是原始碼目錄——License 只寫在套件自己的 metadata 裡。

## License

MIT。完整內容見 [LICENSE](LICENSE)；第三方聲明見 `NOTICE` 或 `THIRD_PARTY_NOTICES`（如適用）。
