---
layout: page
title: windows/where (中文)
description: "显示与搜索模式匹配的文件的位置。"
content_hash: c69dfc371c66daa7c288a20a1a1650c590796922
related_topics:
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
---
# where

显示与搜索模式匹配的文件的位置。
在默认情况下，搜索是在当前目录和 PATH 环境变量指定的路径中执行的。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/where>.

- 显示匹配的文件的位置：

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 显示匹配的文件的位置、大小和日期：

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 在指定的路径下递归搜索要匹配的文件：

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>

- 只返回退出代码，不显示匹配文件列表：

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件模式</span>
