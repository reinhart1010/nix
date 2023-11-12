---
layout: page
title: common/ninja (中文)
description: "一个快速的构建系统。"
content_hash: f8a08e7f519212335cd993253a1b520b79d02b6d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ninja.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ninja

一个快速的构建系统。
更多信息：<https://ninja-build.org/manual.html>.

- 在当前目录下构建：

`ninja`

- 在当前目录下构建，最多并行执行 4 个作业：

`ninja -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 在指定的目录中构建一个程序：

`ninja -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>

- 查看 target（如 `install` 和 `uninstall`）：

`ninja -t targets`

- 查看帮助：

`ninja -h`
