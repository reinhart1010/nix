---
layout: page
title: osx/opensnoop (中文)
description: "跟踪系统中打开的文件标识符。"
content_hash: 3681f39f467fadbb0a83d8f6a31d90addc809548
related_topics:
  - title: English version
    url: /en/osx/opensnoop.html
    icon: bi bi-globe
---
# opensnoop

跟踪系统中打开的文件标识符。

- 输出当前系统内被打开的所有文件：

`sudo opensnoop`

- 跟踪给定进程名，打开的所有文件：

`sudo opensnoop -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>

- 跟踪给定 PID（进程号），打开的所有文件：

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID 进程号</span>

- 跟踪打开了指定文件的继承：

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 文件</span>
