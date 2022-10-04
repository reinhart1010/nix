---
layout: page
title: windows/taskkill (中文)
description: "按进程 id 或进程名终止进程。"
content_hash: eb8cc50145153ecf4e24cc94cb53736dc8798aa3
related_topics:
  - title: English version
    url: /en/windows/taskkill.html
    icon: bi bi-globe
---
# taskkill

按进程 id 或进程名终止进程。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 通过进程 id 终止进程：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程 id</span>

- 通过进程名终止进程：

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>

- 强制终止一个指定的进程：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>` /f`

- 终止一个进程及其子进程：

`taskkill /im `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>` /t`

- 终止远程计算机上的进程：

`taskkill /pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程 id</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机名</span>

- 显示命令的帮助信息：

`taskkill /?`
