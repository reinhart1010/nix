---
layout: page
title: windows/systeminfo (中文 (繁體, 台灣))
description: "顯示本機或遠端電腦的作業系統配置。"
content_hash: 9fd9a20f915c91b1bc0f27e1818f349dec1c89fc
last_modified_at: 2023-10-16
related_topics:
  - title: English version
    url: /en/windows/systeminfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/systeminfo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systeminfo

顯示本機或遠端電腦的作業系統配置。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 顯示本機的系統配置：

`systeminfo`

- 以指定的輸出格式顯示系統配置：

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 顯示遠端電腦的系統配置：

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">遠端名稱</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密碼</span>

- 顯示詳細的使用資訊：

`systeminfo /?`
