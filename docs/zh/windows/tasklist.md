---
layout: page
title: windows/tasklist (中文)
description: "显示本地或远程计算机上当前正在运行的进程的列表。"
content_hash: 2e3b7372f36cac56000d2284f4fd907166498cc0
related_topics:
  - title: English version
    url: /en/windows/tasklist.html
    icon: bi bi-globe
---
# tasklist

显示本地或远程计算机上当前正在运行的进程的列表。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- 显示当前正在运行的进程：

`tasklist`

- 使用指定的格式显示当前进程列表：

`tasklist /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 已匹配的方式（.exe, .dll）显示当前运行的进程：

`tasklist /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">匹配模式</span>

- 显示在远程计算机上运行的进程：

`tasklist /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机名</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 显示每个进程中的服务信息：

`tasklist /svc`
