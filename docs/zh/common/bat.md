---
layout: page
title: common/bat (中文)
description: "可以打印并且合并文件的命令。"
content_hash: da502f4c5d9cf34cec4eab4763af0ac2ad6a033e
last_modified_at: 2024-11-28
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/bat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/bat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bat

可以打印并且合并文件的命令。
`cat` 的复制品，外加语法高亮和 Git 集成。
更多信息：<https://github.com/sharkdp/bat>.

- 使用美化样式打印一个或多个文件的内容到 `stdout`：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>

- 将多个文件连接成一个目标文件：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标文件</span>

- 移除修饰并禁用分页（`--style plain` 可以用 `-p` 代替，或用 `-pp` 组合两个选项）：

`bat --style plain --pager never `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 使用不同的背景颜色高亮显示特定行或一行范围：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--highlight-line</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10|5:10|:10|10:|10:+5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示不可打印字符，如空格、制表符或换行：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-A|--show-all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 在输出中只保留行号，移除所有其他修饰：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 通过明确设置语言来语法高亮显示 JSON 文件：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--language</span>` json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.json</span>

- 显示所有支持的语言：

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--list-languages</span>
