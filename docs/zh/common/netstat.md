---
layout: page
title: common/netstat (中文)
description: "显示与网络相关的信息，如打开的连接、打开的套接字端口等。"
content_hash: ec5fd03a404f09611e74600c288d20a60c4bcd19
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># netstat

显示与网络相关的信息，如打开的连接、打开的套接字端口等。
更多信息：<https://manned.org/netstat>.

- 列出所有端口：

`netstat -a`

- 列出所有被侦听端口：

`netstat -l`

- 列出侦听的 TCP 端口：

`netstat -t`

- 显示监听给定协议监听的 PID 和程序名：

`netstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">协议</span>

- 打印路由表：

`netstat -nr`
