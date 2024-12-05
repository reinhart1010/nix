---
layout: page
title: common/zellij (中文)
description: "带有内置功能的终端复用器。"
content_hash: 1f76f662cd120f5baad16e6c662921385de0a20a
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zellij.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zellij.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zellij.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zellij

带有内置功能的终端复用器。
请参阅：`tmux` 和 `screen`。
更多信息：<https://zellij.dev/documentation/>.

- 启动一个新的命名会话：

`zellij --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 列出现有会话：

`zellij list-sessions`

- 附加到最近使用的会话：

`zellij attach`

- 打开一个新窗格（在 zellij 会话中）：

`<Alt> + N`

- 从当前会话分离（在 zellij 会话中）：

`<Ctrl> + O, D`
