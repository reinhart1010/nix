---
layout: page
title: common/rm (中文 (繁體, 台灣))
description: "移除檔案或目錄。"
content_hash: 0f606701b75adb1d8329b5f70c7b43a54c595ccd
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rm

移除檔案或目錄。
更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- 移除位於指定路徑的檔案：

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案一/完整/路徑 檔案二/完整/路徑 ...</span>

- 移除檔案，且每次移除都會進行確認：

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案一</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案二</span>

- 移除目錄中的所有檔案，並顯示每個檔案的移除資訊：

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄/完整/路徑/*</span>

- 遞迴移除目錄與其所有子目錄：

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目錄/完整/路徑</span>
