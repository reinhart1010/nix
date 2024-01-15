---
layout: page
title: common/direnv (中文)
description: "Shell 扩展为加载和卸载环境变量，具体取决于当前目录。"
content_hash: 2d03bdfb911030b391a9920362a33470a79a79e7
last_modified_at: 2024-01-15
related_topics:
  - title: English version
    url: /en/common/direnv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/direnv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# direnv

Shell 扩展为加载和卸载环境变量，具体取决于当前目录。
更多信息：<https://github.com/direnv/direnv>.

- 授予 direnv 当前目录中加载 `.envrc`:

`direnv allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 撤销在当前目录加载 `.envrc` 的授权：

`direnv deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 使用默认编辑器编辑 `.envrc` 并在退出时重载环境：

`direnv edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 触发环境重载：

`direnv reload`

- 打印一些调试状态信息：

`direnv status`
