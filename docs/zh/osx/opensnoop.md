---
layout: page
title: osx/opensnoop (中文)
description: "跟踪系统中打开的文件标识符。"
content_hash: 67ab0563defaf9773654436c12db2707defb3fdb
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/opensnoop.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/opensnoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opensnoop

跟踪系统中打开的文件标识符。
更多信息：<https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- 输出当前系统内被打开的所有文件：

`sudo opensnoop`

- 跟踪给定进程名，打开的所有文件：

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>`"`

- 跟踪给定 PID（进程号），打开的所有文件：

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID 进程号</span>

- 跟踪打开了指定文件的继承：

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 文件</span>
