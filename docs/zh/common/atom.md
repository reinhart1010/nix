---
layout: page
title: common/atom (中文)
description: "一个跨平台的，可插拔的文本编辑器。"
content_hash: 03d3c28d3ed3ca0e08c01069e5a606548090817d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># atom

一个跨平台的，可插拔的文本编辑器。
由 `apm` 管理插件。
更多信息：<https://atom.io/>.

- 打开文件或目录：

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 在新窗口中打开文件或目录：

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 在已有窗口中打开文件或目录：

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 以安全模式启动 Atom（不加载额外插件）：

`atom --safe`

- 在终端前台运行 Atom：

`atom --foreground`
