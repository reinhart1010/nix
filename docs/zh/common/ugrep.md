---
layout: page
title: common/ugrep (中文)
description: "超快速搜索工具，带有查询 TUI。"
content_hash: 5f2fc57dc33513e004e4544600042079adf021e8
last_modified_at: 2024-11-20
related_topics:
  - title: Deutsch version
    url: /de/common/ugrep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ugrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ugrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ugrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ugrep

超快速搜索工具，带有查询 TUI。
更多信息：<https://github.com/Genivia/ugrep>.

- 启动查询 TUI，在当前目录中递归搜索文件（按 CTRL-Z 获取帮助）：

`ugrep --query`

- 在当前目录中递归搜索包含正则表达式搜索模式的文件：

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- 在特定文件或特定目录中的所有文件中搜索，并显示匹配的行号：

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 递归搜索当前目录中的所有文件，并打印每个匹配文件的名称：

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- 模糊搜索文件，允许模式中多达 3 个额外、缺失或不匹配的字符：

`ugrep --fuzzy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- 也递归搜索压缩文件、Zip 和 tar 存档：

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- 仅搜索文件名匹配特定 glob 模式的文件：

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob_pattern</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- 仅搜索 C++ 源文件（使用 `--file-type=list` 列出所有文件类型）：

`ugrep --file-type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`
