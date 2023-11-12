---
layout: page
title: windows/fondue (中文)
description: "可选 Windows 功能的命令行安装程序。"
content_hash: 45acaa7b7bf478b3688520c0e9c1b6e754ad7b49
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/fondue.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/fondue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fondue

可选 Windows 功能的命令行安装程序。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- 启用一个指定的 Windows 功能：

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能</span>

- 向用户隐藏所有输出信息：

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能</span>` /hide-ux:all`

- 为错误报告指定调用者进程名称：

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
