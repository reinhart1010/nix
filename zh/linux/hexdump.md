---
layout: page
title: linux/hexdump (中文)
description: "一个 ASCII，十进制，十六进制，八进制转换查看工具。"
content_hash: 5bbdc523e6a771d2836f0bdacd3a4f59dad8fbd9
---
# hexdump

一个 ASCII，十进制，十六进制，八进制转换查看工具。

- 打印文件的十六进制表示形式：

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 以十六进制显示输入偏移量，并在最后两列中显示其 ASCII 表示形式：

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 显示文件的十六进制表示，但只解释输入的 N 个字节：

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字节数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>
