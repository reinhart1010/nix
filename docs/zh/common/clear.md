---
layout: page
title: common/clear (中文)
description: "清空终端的屏幕。"
content_hash: e50d24aa3da926e5868ef8b0257c980d3cbbe0df
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
---
# clear

清空终端的屏幕。
更多信息：<https://manned.org/clear>.

- 清空屏幕（相当于在 Bash shell 中按 Control-L 键）：

`clear`

- 清空屏幕但保留终端的回滚缓冲区：

`clear -x`

- 指明要清空的终端类型（默认为环境变量 `TERM` 的值）：

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_of_terminal</span>

- 显示 `clear` 使用的 `ncurses` 版本：

`clear -V`
