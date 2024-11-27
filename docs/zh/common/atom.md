---
layout: page
title: common/atom (中文)
description: "一个跨平台的可扩展文本编辑器。"
content_hash: 6645907c10af6b0e22e6a482c7858f770d4bd841
last_modified_at: 2024-11-27
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
  - title: हिन्दी version
    url: /hi/common/atom.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/atom.html
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

一个跨平台的可扩展文本编辑器。
插件由 `apm` 管理。
注意：Atom 已经停止更新并且不再积极维护。
更多信息：<https://atom.io/>.

- 打开文件或目录：

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 在新窗口中打开文件或目录：

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 在已有窗口中打开文件或目录：

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 以安全模式启动 Atom（不加载额外插件）：

`atom --safe`

- 阻止 Atom 分叉到后台，保持 Atom 与终端连接：

`atom --foreground`

- 等待 Atom 窗口关闭后再返回（对于 Git 提交编辑器很有用）：

`atom --wait`
