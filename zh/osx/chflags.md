---
layout: page
title: osx/chflags (中文)
description: "更改文件或文件夹的标志。"
content_hash: 7d49c00c24fb80d8936798e4b243b6c830c97c56
related_topics:
  - title: English version
    url: /en/osx/chflags.html
    icon: bi bi-globe
---
# chflags

更改文件或文件夹的标志。
更多信息：<https://ss64.com/osx/chflags.html>.

- 给文件设置 hidden（隐藏）标签：

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 取消文件的 hidden 标签：

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 递归地给文件夹中每个文件设置 uchg 标志：

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹路径</span>

- 递归地撤销文件夹中每个文件设置的 uchg 标志：

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹路径</span>
