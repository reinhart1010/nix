---
layout: page
title: windows/taskkill (中文 (繁體, 台灣))
description: "經由處理程序識別碼 (PID) 或映像名稱終止程序。"
content_hash: a4880bbffe02a77f1761840f66637d823d189136
related_topics:
  - title: English version
    url: /en/windows/taskkill.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/taskkill.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># taskkill

經由處理程序識別碼 (PID) 或映像名稱終止程序。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 經由處理程序識別碼終止程序：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">處理程序識別碼</span>

- 經由映像名稱終止程序：

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像名稱</span>

- 強制終止特定程序：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">處理程序識別碼</span>` /f`

- 終止程序與其子程序：

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像名稱</span>` /t`

- 終止遠端電腦上的程序：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">處理程序識別碼</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">遠端名稱</span>

- 顯示此命令的使用資訊：

`taskkill /?`
