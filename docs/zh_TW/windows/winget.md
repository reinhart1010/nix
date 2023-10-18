---
layout: page
title: windows/winget (中文 (繁體, 台灣))
description: "Windows 套件管理員的命令列工具。"
content_hash: c8e5f2cb485fd254b0a566e48ee2486bc668270d
last_modified_at: 2023-10-18
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
---
# winget

Windows 套件管理員的命令列工具。
更多資訊：<https://learn.microsoft.com/windows/package-manager/winget>.

- 安裝一個套件：

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">套件</span>

- 刪除一個套件（註：可以用 `remove` 代替 `uninstall`）：

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- 顯示指定套件的相關資訊：

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">套件</span>

- 搜尋指定套件：

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">套件</span>

- 升級所有套件至最新版本：

`winget upgrade --all`

- 列出所有可由 `winget` 管理的已安裝套件：

`winget list --source winget`

- 從檔案匯入套件，或將已安裝的套件匯出至檔案：

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 在提交 PR 到 winget-pkgs 存儲庫之前，請驗證 manifest 檔：

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manifest檔案/完整/路徑</span>
