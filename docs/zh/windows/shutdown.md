---
layout: page
title: windows/shutdown (中文)
description: "用于关闭、重启或注销计算机的工具。"
content_hash: d4476965df0e4022447ad22aa78299d25e354ee7
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/windows/shutdown.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/shutdown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/shutdown.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># shutdown

用于关闭、重启或注销计算机的工具。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 关闭当前计算机：

`shutdown /s`

- 强制关闭当前计算机的所有应用程序：

`shutdown /s /f`

- 立即重启当前计算机：

`shutdown /r /t 0`

- 休眠当前计算机：

`shutdown /h`

- 注销当前计算机：

`shutdown /l`

- 指定在关闭前等待的秒数：

`shutdown /s /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒</span>

- 中止尚未超时的关机序列：

`shutdown /a`

- 关闭远程计算机：

`shutdown /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\ 主机名</span>
