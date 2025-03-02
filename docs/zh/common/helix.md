---
layout: page
title: common/helix (中文)
description: "Helix，一个后现代的文本编辑器，为不同类型的文本操作提供了几种模式。"
content_hash: 0160aef8dfcca9e87071324584b255dd99ee3dd3
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/helix.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/helix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/helix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helix

Helix，一个后现代的文本编辑器，为不同类型的文本操作提供了几种模式。
按 `i` 进入插入模式。按 `<Esc>` 进入正常模式，并且可以使用 Helix 命令。
更多信息：<https://helix-editor.com>.

- 打开文件：

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 并排打开多个文件：

`helix --vsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2</span>

- 显示 Helix 教程（也可以在 Helix 中按 `<Esc>` 后输入 `:tutor` 访问）：

`helix --tutor`

- 更改 Helix 主题：

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主题名称</span>

- 保存并退出：

`:wq<Enter>`

- 强制退出并不保存：

`:q!<Enter>`

- 撤销上次操作：

`u`

- 搜索文件中的关键字（按 `n`/`N` 前往下一个/上一个匹配）：

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`<Enter>`
