---
layout: page
title: common/read (中文)
description: "从标准输入（或文件）读取一行并将单词分配给变量。"
content_hash: 98487e7501efe0033043668d8735cc627cb2e161
last_modified_at: 2025-01-04
related_topics:
  - title: English version
    url: /en/common/read.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/read.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/read.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/read.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/read.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># read

从标准输入（或文件）读取一行并将单词分配给变量。
更多信息：<https://manned.org/read.1p>.

- 读取键盘输入的数据赋值给变量：

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量</span>

- 将您输入的每一行存储为数组一个元素：

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数组</span>

- 指定要读取的字符数，将数据赋值给变量：

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量</span>

- 将多个数据依次赋值给多个变量：

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_ 变量1 _ 变量2</span>` <<< "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">The surname is Bond</span>`"`

- 读取键盘输入的数据赋值给变量，不对\进行转义：

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量</span>

- 键盘输入前显示提示语：

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">提示语：</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量</span>

- 静默模式（如果输入来自终端，则不回显字符）读取键盘输入的数据赋值给变量：

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量</span>

- 从标准输入读取每一行进行操作：

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标准输入|路径/到/文件|...</span>
