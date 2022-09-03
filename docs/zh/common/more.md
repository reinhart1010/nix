---
layout: page
title: common/more (中文)
description: "打开一个文件进行交互式阅读，允许滚动和搜索。"
content_hash: 0c4550f25c1b2f117122f8529f68f891d8990619
related_topics:
  - title: English version
    url: /en/common/more.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/more.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/more.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># more

打开一个文件进行交互式阅读，允许滚动和搜索。
更多信息：<https://manned.org/more>.

- 打开一个文件：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 打开一个文件，从特定行开始显示：

`more +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示帮助：

`more --help`

- 转到下一页：

`<空格>`

- 搜索一个字符串（按 `n` 键跳转到下一个匹配）:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 退出：

`q`

- 显示关于交互式命令的帮助：

`h`
