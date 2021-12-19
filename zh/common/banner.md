---
layout: page
title: common/banner (中文)
description: "将给定参数输出为大型 ASCII 文字。"
content_hash: 772b5cb73f74e4cc69828c095e248fa70fa8e72b
related_topics:
  - title: English version
    url: /en/common/banner.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/banner.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/banner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/banner.html
    icon: bi bi-globe
---
# banner

将给定参数输出为大型 ASCII 文字。
更多信息：<https://man.archlinux.org/man/banner.1>.

- 将文字信息打印为大横幅（引号是可选的）：

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 将文字信息打印为横幅，宽度为 50 个字：

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 从 stdin 中读取文本：

`banner`
