---
layout: page
title: common/zsh (中文)
description: "Z SHell，一个兼容 Bash 的命令行解释器。"
content_hash: f12fb42511e1939743179f50e7971c6c9f64389c
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zsh

Z SHell，一个兼容 Bash 的命令行解释器。
参见：`bash`，`histexpand`.
更多信息：<https://www.zsh.org>.

- 启动交互式解释器：

`zsh`

- 执行指定的命令：

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>`"`

- 执行指定的脚本：

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.zsh</span>

- 不执行指定的脚本，只检查其语法错误：

`zsh --no-exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.zsh</span>

- 执行来自 `stdin` 的命令：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>` | zsh`

- 执行指定的脚本，并打印出每一个将要执行的命令：

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.zsh</span>

- 启动详细模式的交互式解释器，会打印出每一个将要执行的命令：

`zsh --verbose`

- 在 `zsh` 里执行指定的命令，但禁用 glob 模式：

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>
