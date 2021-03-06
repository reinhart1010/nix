---
layout: page
title: windows/find (中文 (繁體, 台灣))
description: "在一個或多個文件中查詢指定字串。"
content_hash: 31e58f9604881438a48ae3ae6c13e2120d9638ec
related_topics:
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
---
# find

在一個或多個文件中查詢指定字串。
更多資訊：<https://docs.microsoft.com/windows-server/administration/windows-commands/find>.

- 查詢包含指定字串的行：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>

- 查詢不包含指定字串的行：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>` /v`

- 顯示包含指定字串的行總數：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>` /c`

- 顯示符合的行號：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>` /n`
