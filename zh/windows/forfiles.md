---
layout: page
title: windows/forfiles (中文)
description: "选择一个或多个文件以执行指定的命令。"
content_hash: 57f3cb1f091f7bd6d95931873d8dbc37b0c9aed5
related_topics:
  - title: English version
    url: /en/windows/forfiles.html
    icon: bi bi-globe
---
# forfiles

选择一个或多个文件以执行指定的命令。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- 在当前的目录中寻找文件：

`forfiles`

- 在一个指定目录中寻找文件：

`forfiles /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 为每个文件执行指定的命令：

`forfiles /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>`"`

- 使用通配符来寻找指定的文件：

`forfiles /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">通配符</span>

- 递归寻找文件：

`forfiles /s`

- 搜索超过 5 天的文件：

`forfiles /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+5</span>
