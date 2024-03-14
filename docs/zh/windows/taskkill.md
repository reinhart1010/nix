---
layout: page
title: windows/taskkill (中文)
description: "按进程 ID 或进程名终止进程。"
content_hash: 7e5c2d9d546692d154f4e19872bca2f3f32428a6
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/windows/taskkill.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/taskkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# taskkill

按进程 ID 或进程名终止进程。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- 通过进程 ID 终止进程：

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
