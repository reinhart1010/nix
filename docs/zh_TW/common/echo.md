---
layout: page
title: common/echo (中文 (繁體, 台灣))
description: "印出文字。"
content_hash: 0324506fe090daac3b832f621e9ee9704e0e7900
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># echo

印出文字。
更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- 印出一行文字（如果文字中沒有連續的空格，可以不加引號）：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字</span>`"`

- 印出包含環境變數的文字：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的家目錄位於 $HOME</span>`"`

- 印出文字，但結尾不換行：

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字</span>`"`

- 將一段文字加到檔案的結尾：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案</span>

- 將以「\\」開頭的跳脫序列轉換為特殊字元（例如「\t」會被顯示為水平定位字元）：

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一欄\t第二欄</span>`"`
