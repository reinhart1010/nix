---
layout: page
title: common/trap (中文)
description: "在进程或操作系统接收到信号后自动执行命令。"
content_hash: 4943c3e69046a11a56eb861e96281680e8a2c4b1
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/trap.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># trap

在进程或操作系统接收到信号后自动执行命令。
可用于对用户中断或其他操作执行清理。
更多信息：<https://manned.org/trap>.

- 列出设置 trap 的可用信号：

`trap -l`

- 列出当前 shell 程序的活动 trap 程序：

`trap -p`

- 设置 trap 以在检测到一个或多个信号时执行命令：

`trap 'echo "检测到信号 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- 移除活动 trap：

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
