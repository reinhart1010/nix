---
layout: page
title: common/compgen (中文)
description: "用于在 bash 中自动完成的内置命令，按两次 tab 键即可调用该命令。"
content_hash: 05cacbb56bb0ea79aefea91c5160f1bb9069c702
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/compgen.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/compgen.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/compgen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/compgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compgen

用于在 bash 中自动完成的内置命令，按两次 tab 键即可调用该命令。
更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- 显示所有可以执行的命令：

`compgen -c`

- 列出所有以指定字符串开头的可执行命令：

`compgen -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 列出所有别名：

`compgen -a`

- 列出所有可以运行的函数：

`compgen -A function`

- 列出所有 shell 的保留关键字：

`compgen -k`

- 查看以 'ls' 开头的所有可用命令和别名：

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
