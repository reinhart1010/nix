---
layout: page
title: osx/chflags (中文)
description: "更改文件或文件夹的标志。"
content_hash: a6b75113394ccedee5f95c0c1a451387ff96be45
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/chflags.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/chflags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chflags

更改文件或文件夹的标志。
更多信息：<https://keith.github.io/xcode-man-pages/chflags.1.html>.

- 给文件设置 hidden（隐藏）标签：

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 取消文件的 hidden 标签：

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 递归地给文件夹中每个文件设置 uchg 标志：

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹路径</span>

- 递归地撤销文件夹中每个文件设置的 uchg 标志：

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹路径</span>
