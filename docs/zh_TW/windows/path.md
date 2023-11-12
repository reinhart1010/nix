---
layout: page
title: windows/path (中文 (繁體, 台灣))
description: "顯示或設定可執行檔的搜尋路徑。"
content_hash: 5aa4a08957ddc30df60ae97c60c6f6c67f6511fb
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/path.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/path.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/path.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
tldri18n_status: 2
---
# path

顯示或設定可執行檔的搜尋路徑。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- 顯示當前的 PATH 環境變數的設定：

`path`

- 將路徑設定為一個或多個以分號分隔的路徑目錄：

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>`;`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑]</span>

- 將新的路徑目錄附加到到原始路徑：

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>`;%path%`

- 將命令提示字元設定為僅在當前目錄中搜尋可執行檔：

`path ;`
