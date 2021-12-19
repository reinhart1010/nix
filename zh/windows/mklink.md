---
layout: page
title: windows/mklink (中文)
description: "创建符号链接。"
content_hash: d21c1c4fa3a3ba662840ca1abd00fb078213b079
related_topics:
  - title: English version
    url: /en/windows/mklink.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/mklink.html
    icon: bi bi-globe
---
# mklink

创建符号链接。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/mklink>.

- 创建指向文件的符号链接：

`mklink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">链接文件的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>

- 创建指向目录的符号链接：

`mklink /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">链接文件的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源目录路径</span>

- 创建指向文件的硬链接：

`mklink /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">链接文件的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源目录路径</span>

- 创建目录链接：

`mklink /j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">链接文件的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源目录路径</span>
