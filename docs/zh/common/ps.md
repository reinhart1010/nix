---
layout: page
title: common/ps (中文)
description: "提供正在运行的进程的信息。"
content_hash: 38e9a7a15d4abc3f0784da6332a3e33de4e5eaa3
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

提供正在运行的进程的信息。
更多信息：<https://manned.org/ps>.

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 查找与字符串匹配的进程：

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 以 extra full 格式列出当前用户的所有进程：

`ps --user $(id -u) -F`

- 以树形方式列出当前用户的所有进程：

`ps --user $(id -u) f`

- 获取一个进程的父进程 ID：

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程 ID</span>

- 按内存使用量对进程进行排序：

`ps --sort size`
