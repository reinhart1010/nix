---
layout: page
title: common/banner (中文)
description: "将给定参数输出为大型 ASCII 文字。"
content_hash: fd0f8d4a5e978e90783ade66a2caa97d7b9f4820
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/banner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# banner

将给定参数输出为大型 ASCII 文字。
更多信息：<https://manned.org/banner>.

- 将文字信息打印为大横幅（引号是可选的）：

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 将文字信息打印为横幅，宽度为 50 个字：

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 从 `stdin` 中读取文本：

`banner`
