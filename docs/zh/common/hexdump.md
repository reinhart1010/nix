---
layout: page
title: common/hexdump (中文)
description: "一个 ASCII，十进制，十六进制，八进制转换查看工具。"
content_hash: 6d110e59010b0a5b57851e6377912009bb447d6f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hexdump

一个 ASCII，十进制，十六进制，八进制转换查看工具。
更多信息：<https://manned.org/hexdump>.

- 打印文件的十六进制表示形式：

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 以十六进制显示输入偏移量，并在最后两列中显示其 ASCII 表示形式：

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示文件的十六进制表示，但只解释输入的 N 个字节：

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字节数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
