---
layout: page
title: common/ninja (中文)
description: "一个快速的构建系统。"
content_hash: b654ce07715fc415bb5c8a0266fda3e5fdcf0191
related_topics:
  - title: English version
    url: /en/common/ninja.html
    icon: bi bi-globe
---
# ninja

一个快速的构建系统。
更多信息：<https://ninja-build.org/manual.html>.

- 在当前目录下构建：

`ninja`

- 在指定的目录中构建一个程序：

`ninja -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>

- 查看 target（如 `install` 和 `uninstall`）：

`ninja -t targets`

- 查看帮助：

`ninja -h`
