---
layout: page
title: common/banner (中文)
description: "将给定参数输出为大型 ASCII 文字。"
content_hash: 2f1465b63f6b9d3875e89481b39a1ebebdfb67aa
last_modified_at: 2024-10-13
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

`banner -w 50 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 从 `stdin` 中读取文本：

`banner`
