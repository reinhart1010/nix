---
layout: page
title: common/btop (中文)
description: "显示有关 CPU、内存、磁盘、网络和进程的信息的资源监视器。"
content_hash: 582f5bd8387073640e9b5af1dd73ecd9d12fdd7e
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/btop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/btop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/btop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/btop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btop

显示有关 CPU、内存、磁盘、网络和进程的信息的资源监视器。
`bpytop` 的 C++ 版本。
更多信息：<https://github.com/aristocratos/btop>.

- 启动 `btop`:

`btop`

- 使用指定预设启动 `btop`:

`btop --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>

- 使用 16 种颜色和 TTY 友好的图形符号在 TTY 模式下启动 `btop`:

`btop --tty_on`

- 在 256 色模式而不是 24 位颜色模式下启动 `btop`:

`btop --low-color`
