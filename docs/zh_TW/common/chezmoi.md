---
layout: page
title: common/chezmoi (中文 (繁體, 台灣))
description: "一個用 Go 語言寫的 dotfile 管理工具。"
content_hash: 006245c61e7ea520f94d8951a7a8fb9b05f8c052
last_modified_at: 2023-04-13
related_topics:
  - title: English version
    url: /en/common/chezmoi.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Chezmoi

一個用 Go 語言寫的 dotfile 管理工具。
更多資訊：<https://chezmoi.io>.

- 初始化 chezmoi：

`chezmoi init`

- 叫 chezmoi 管理一個 dotfile：

`chezmoi add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 編輯一個已管理的 dotfile：

`chezmoi edit {檔案/完整/路徑</span>

- 檢視 chezmoi 所做的更動：

`chezmoi diff`

- 套用所做的更動：

`chezmoi -v apply`

- 用一個已存在的 git repository 來初始化 chezmoi：

`chezmoi init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/path/to/repository.git</span>

- 從遠端的 repository 獲取所做的更動：

`chezmoi update`
