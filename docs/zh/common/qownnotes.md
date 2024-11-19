---
layout: page
title: common/qownnotes (中文)
description: "Markdown 笔记应用程序。"
content_hash: af00def264267df3e0e666fecabdb4d7a9478be1
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qownnotes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qownnotes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qownnotes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qownnotes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qownnotes

Markdown 笔记应用程序。
可以选择与 Nextcloud 和 ownCloud 的笔记应用程序集成。
请参阅：`qc`，用于管理命令代码片段。
更多信息：<https://www.qownnotes.org/getting-started/cli-parameters.html>.

- 以便携模式运行：

`QOwnNotes --portable`

- 在 GitHub Markdown 中转储应用程序和环境的设置信息：

`QOwnNotes --dump-settings`

- 为设置和内部文件指定不同的上下文：

`QOwnNotes --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test</span>

- 应用程序启动后触发一个菜单操作：

`QOwnNotes --action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">actionShow_Todo_List</span>
