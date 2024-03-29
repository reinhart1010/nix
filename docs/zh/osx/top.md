---
layout: page
title: osx/top (中文)
description: "显示运行进程的动态实时信息。"
content_hash: eb5d81442ed3e521a487dcec4c28fe2fd57d8104
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

显示运行进程的动态实时信息。
更多信息：<https://keith.github.io/xcode-man-pages/top.1.html>.

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
