---
layout: page
title: common/htop (中文)
description: "显示正在运行的进程的动态实时信息。`top` 的增强版。"
content_hash: e22ac4dc030b7e50646789a43ab9bcf4345013e9
last_modified_at: 2024-07-26
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

显示正在运行的进程的动态实时信息。`top` 的增强版。
更多信息：<https://htop.dev/>.

- 启动 `htop`:

`htop`

- 启动 `htop`, 显示指定用户拥有的进程：

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 使用指定的 `sort_item` 对进程排序（使用 `htop --sort help` 获取可用选项）：

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort_item</span>

- 以指定的更新间隔启动 `htop`, 以十分之一秒为单位（即 50 = 5 秒）：

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- 运行 `htop` 时查看交互式命令：

`?`

- 切换到不同的标签：

`tab`

- 显示帮助：

`htop --help`
