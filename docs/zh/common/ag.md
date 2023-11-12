---
layout: page
title: common/ag (中文)
description: "The Silver Searcher. 类似 ack, 但是更快。"
content_hash: 9a1b312cab717018588b76578d3d888cf4a0e9c3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

The Silver Searcher. 类似 ack, 但是更快。
更多信息：<https://github.com/ggreer/the_silver_searcher>.

- 寻找内容包含"小明"的文件，并列出所在的行数：

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小明</span>

- 在指定目录中寻找内容包含 "foo" 的文件：

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小明</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>

- 寻找内容包含 "foo" 的文件，但只列出文件名：

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小明</span>

- 忽略大小写，寻找内容包含 "ABC" 的文件，并只输出匹配的内容，而非整行：

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ABC</span>

- 在文件名包含"小红"的文件中寻找"小明"：

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小明</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小红</span>

- 使用正则表达式来匹配文件内容：

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- 输出文件名包含"小明"的文件名：

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">小明</span>
