---
layout: page
title: osx/du (中文 (繁體, 台灣))
description: "硬碟使用量：估算每個檔案以及目錄所佔用的硬碟容量。"
content_hash: 72d49b29ff98a55f1a7c5c75ee8b22750dc49078
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

硬碟使用量：估算每個檔案以及目錄所佔用的硬碟容量。
更多資訊：<https://keith.github.io/xcode-man-pages/du.1.html>.

- 以給定單位（KiB/MiB/GiB）列出目錄和所有子目錄的大小：

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出目錄和所有子目錄的大小：

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出單一目錄大小：

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式（自動選擇單位）列出目錄以及底下所有檔案大小：

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式列出目錄和任何子目錄的大小，最多 N 層：

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄路徑</span>

- 以人類可讀形式列出目前目錄子目錄中所有 `.jpg` 檔案的大小，並在最後顯示累積總數：

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
