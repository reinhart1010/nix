---
layout: page
title: common/pdfgrep (中文)
description: "在 PDF 文件中搜索文本。"
content_hash: 2d0f9065787d9b0257804fa77e2d21606153ddf9
related_topics:
  - title: English version
    url: /en/common/pdfgrep.html
    icon: bi bi-globe
---
# pdfgrep

在 PDF 文件中搜索文本。

- 在 PDF 中查找与关键词匹配的行：

`pdfgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.pdf</span>

- 包含每个匹配行的文件名和页码：

`pdfgrep --with-filename --page-number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.pdf</span>

- 对以 "foo" 开头关键词搜索，返回前 3 个匹配项，不区分大小写：

`pdfgrep --max-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'^foo'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.pdf</span>

- 在当前目录中扩展名为.pdf 的文件中递归查找关键词：

`pdfgrep --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 在与当前目录中特定文件名 "*book.pdf" 匹配的文件上递归查找关键词：

`pdfgrep --recursive --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*book.pdf'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>
