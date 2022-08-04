---
layout: page
title: common/netstat (中文)
description: "显示与网络相关的信息，如打开的连接、打开的套接字端口等。"
content_hash: 614f6127cbc5aaf9c64796b2ef7675afb7dc88b9
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netstat

显示与网络相关的信息，如打开的连接、打开的套接字端口等。
更多信息：<https://man7.org/linux/man-pages/man8/netstat.8.html>.

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
