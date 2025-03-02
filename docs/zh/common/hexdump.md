---
layout: page
title: common/hexdump (中文)
description: "一个 ASCII、十进制、十六进制、八进制转换查看工具。"
content_hash: dfa103d8bbbbe43a32e9de74f6c7edfff640f8fc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/hexdump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hexdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexdump

一个 ASCII、十进制、十六进制、八进制转换查看工具。
更多信息：<https://manned.org/hexdump>.

- 打印文件的十六进制表示形式，重复的行用 '*' 替代：

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 以十六进制显示输入偏移量，并在最后两列中显示其 ASCII 表示形式：

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示文件的十六进制表示，但只解释输入的指定字节数：

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字节数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 不使用 '*' 替换重复的行：

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
