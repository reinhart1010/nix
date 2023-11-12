---
layout: page
title: windows/del (中文 (繁體, 台灣))
description: "刪除一個或多個檔案。"
content_hash: 877c2ea1bc471877e347d2e40639772290c1b5a4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

刪除一個或多個檔案。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 刪除一個或多個以空格分隔的檔案：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案 檔案 ..</span>

- 在刪除每個檔案之前提示確認：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>` /p`

- 強制刪除唯讀檔案：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>` /f`

- 遞歸刪除所有子目錄中的檔案：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>` /s`

- 在使用全域萬用字元刪除檔案時不做提示確認：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>` /q`

- 顯示幫助訊息和列出所有可用屬性：

`del /?`

- 刪除符合指定屬性的檔案：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">属性</span>
