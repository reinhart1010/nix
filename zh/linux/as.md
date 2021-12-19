---
layout: page
title: linux/as (中文)
description: "一个可移植的 GUN 汇编器。"
content_hash: 2563393cb41dd6f0b11ac2cc7ff67d1db28816b7
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
---
# as

一个可移植的 GUN 汇编器。
主要用于汇编`gcc`的输出，以供链接器`ld`使用。
更多信息：<https://manned.org/as>.

- 汇编一个文件，输出为 a.out:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.s</span>

- 汇编文件，并指定输出文件：

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.o</span>

- 通过跳过空格和注释的预处理过程来更快的产生输出文件（只应该用于可信任的编译器的输出）：

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.s</span>

- 将给定路径添加到目录列表，来搜索.include 指令指定的文件：

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.s</span>
