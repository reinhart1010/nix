---
layout: page
title: common/code (中文)
description: "Visual Studio Code."
content_hash: 71a284a9ffa948b209c6ff7ca5e46b3016a914e5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># code

Visual Studio Code.
更多信息：<https://github.com/microsoft/vscode>.

- 打开 VS Code：

`code`

- 在 VS Code 中打开当前目录：

`code .`

- 在 VS Code 打开一个文件或目录：

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件或目录</span>

- 在当前打开的 VS Code 窗口中打开一个文件或目录：

`code --reuse-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件或目录</span>

- 在 VS Code 中对比两个文件：

`code -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件2</span>

- 用超级用户（sudo）权限打开 VS Code：

`sudo code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件或目录</span>` --user-data-dir`
