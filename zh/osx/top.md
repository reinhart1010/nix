---
layout: page
title: osx/top (中文)
description: "显示运行进程的动态实时信息。"
content_hash: ce46eace6fee1a79a8637df12f60e927b666d799
related_topics:
  - title: English version
    url: /en/osx/top.html
    icon: bi bi-globe
---
# top

显示运行进程的动态实时信息。
更多信息：<https://ss64.com/osx/top.html>.

- 执行 top 命令，界面中提供所有选项：

`top`

- 按内部内存大小排序进程（默认顺序 - 进程 ID）：

`top -o mem`

- 首先按 CPU 启动顺序排序进程，然后按运行时间排序：

`top -o cpu -O time`

- 只显示给定用户拥有的进程：

`top -user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 获取有关交互式命令的帮助（我测试并没看到这个功能）：

`?`
