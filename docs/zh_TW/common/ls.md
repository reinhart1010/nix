---
layout: page
title: common/ls (中文 (繁體, 台灣))
description: "列出目錄內容。"
content_hash: bcec8df3f8bc2c277cc3fa7ca3743baa49bb1ddf
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/ls.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ls.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/ls.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ls.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ls

列出目錄內容。
更多資訊：<https://www.gnu.org/software/coreutils/ls>.

- 列出目錄中的檔案，其中每個檔案佔一行：

`ls -1`

- 列出包含隱藏檔案的所有檔案：

`ls -a`

- 列出檔案，並依照檔案類型在檔案後面加上對應的符號（例如目錄會加上「/」）：

`ls -F`

- 列出包含隱藏檔案的完整檔案列表（包括權限、擁有者、檔案大小與修改日期）：

`ls -la`

- 列出完整檔案列表，其中檔案大小會用 KiB、MiB、GiB 表示：

`ls -lh`

- 列出完整檔案列表，並依檔案大小降序排序：

`ls -lS`

- 列出完整檔案列表，並依修改時間由舊到新排序：

`ls -ltr`
