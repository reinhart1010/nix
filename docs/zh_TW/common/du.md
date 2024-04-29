---
layout: page
title: common/du (中文 (繁體, 台灣))
description: "硬碟使用量：估算每個檔案以及目錄所佔用的硬碟容量。"
content_hash: 54876d24bc923fae87e88ff16a2106d482269e99
last_modified_at: 2024-04-29
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

硬碟使用量：估算每個檔案以及目錄所佔用的硬碟容量。
更多資訊：<https://www.gnu.org/software/coreutils/du>.

- 以給定單位（B/KiB/MiB）列出目錄和所有子目錄的大小：

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出目錄和所有子目錄的大小：

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出單一目錄大小：

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出目錄以及底下所有檔案大小：

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式列出目錄和任何子目錄的大小，最多 N 層：

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式列出目前目錄子目錄中所有 `.jpg` 檔案的大小，並在最後顯示累積總數：

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
