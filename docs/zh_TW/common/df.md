---
layout: page
title: common/df (中文 (繁體, 台灣))
description: "概述檔案系統的磁碟空間的使用情況。"
content_hash: c2ab64fbb63c6cab389f2fbcec4bd1a3e4b17ece
last_modified_at: 2024-01-08
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

概述檔案系統的磁碟空間的使用情況。
更多資訊：<https://www.gnu.org/software/coreutils/df>.

- 顯示所有檔案系統及磁碟使用情況：

`df`

- 以人類可讀的形式顯示所有檔案系統及磁碟使用情況：

`df -h`

- 顯示包含給定檔案或目錄的檔案系統及其磁碟的使用情況：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>

- 顯示未被使用的 inode 數量的統計資訊：

`df -i`

- 顯示檔案系統但排除指定類型：

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
