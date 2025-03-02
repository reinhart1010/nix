---
layout: page
title: common/lsof (中文)
description: "列出打开的文件和相应的进程。"
content_hash: f1c384d00142c4b050b44bacbeb343809dace9e8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/lsof.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/lsof.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lsof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsof

列出打开的文件和相应的进程。
注意：列出其他人打开的文件需要 root 权限（或 sudo）。
更多信息：<https://manned.org/lsof>.

- 查找打开了给定文件的进程：

`lsof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 查找打开了本地互联网端口的进程：

`lsof -i :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>

- 仅输出进程 ID (PID)：

`lsof -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 列出给定用户打开的文件：

`lsof -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 列出给定命令或进程打开的文件：

`lsof -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程或命令的名称</span>

- 列出特定进程打开的文件（给定其 PID）：

`lsof -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 列出目录中打开的文件：

`lsof +D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 查找正在监听本地 IPv6 TCP 端口的进程，不转换网络或端口号：

`lsof -i6TCP:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>` -sTCP:LISTEN -n -P`
