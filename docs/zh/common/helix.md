---
layout: page
title: common/helix (中文)
description: "Helix, 一个后现代的文本编辑器，为不同类型的文本操纵提供了几种模式。"
content_hash: baabda51e60fe6b8c9c68699a6de0dc868b8a2ef
last_modified_at: 2024-01-20
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/helix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/helix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># helix

Helix, 一个后现代的文本编辑器，为不同类型的文本操纵提供了几种模式。
按 `i` 进入插入模式。按 `<Esc>` 进入正常模式，并且可以使用 Helix 命令。
更多信息：<https://helix-editor.com>.

- 打开文件：

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 更改 Helix 主题：

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主题</span>

- 保存并退出：

`:wq<Enter>`

- 强制退出并不保存：

`:q!<Enter>`

- 撤销上次操作：

`u`

- 搜索文件中的关键字（按 `n`/`N` 前往下一个/上一个匹配）：

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>`<Enter>`

- 格式化文件：

`:format`
