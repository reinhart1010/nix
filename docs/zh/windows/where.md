---
layout: page
title: windows/where (中文)
description: "显示与搜索模式匹配的文件的位置。"
content_hash: 4149da614a0686253028c79081ebac583898204e
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/where.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/where.html
    icon: bi bi-globe
tldri18n_status: 2
---
# where

显示与搜索模式匹配的文件的位置。
在默认情况下，搜索是在当前目录和 PATH 环境变量指定的路径中执行的。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- 显示匹配的文件的位置：

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 显示匹配的文件的位置、大小和日期：

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 在指定的路径下递归搜索要匹配的文件：

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 只返回退出代码，不显示匹配文件列表：

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>
