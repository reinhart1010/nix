---
layout: page
title: osx/sed (中文)
description: "以可用脚本的来批量编辑文本。"
content_hash: d31baabe9b3c3abf2d8b09ca8e0edba1144e2724
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/sed.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sed

以可用脚本的来批量编辑文本。
更多信息：<https://keith.github.io/xcode-man-pages/sed.1.html>.

- 替换文件中第一个出现的字符串，并打印结果：

`sed 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 替换文件中所有符合正则表达式的部分：

`sed -E 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 替换文件中所有出现的字符串，覆盖文件（直接覆盖文件）：

`sed --in-place='' 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 仅替换与行模式（一种搜索条件）匹配的行内容：

`sed '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行模式</span>`/s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 只打印第 n 行到下一行之间的文本：

`sed -n '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行号</span>`,/^$/p' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 将多个查找替换表达式应用于文件：

`sed -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/' -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 将分隔符 / 替换为查找或替换模式中没有用到的的任何其他字符，例如 #（用于查找或替换内容中使用了 / 的情况）：

`sed 's#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找内容</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">替换内容</span>`#' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>
