---
layout: page
title: common/jrnl (中文)
description: "一个简单的命令行日记应用程序。"
content_hash: f8d76b74712f19af6b3f2c52c79ceba0196da127
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jrnl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/jrnl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jrnl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jrnl

一个简单的命令行日记应用程序。
更多信息：<https://jrnl.sh>.

- 使用编辑器插入一个新条目：

`jrnl`

- 快速插入一个新条目：

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today at 3am</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标题</span>`. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">内容</span>

- 查看最近的十条条目：

`jrnl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 查看从去年开始到今年三月初所有发生的事情：

`jrnl -from "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last year</span>`" -until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">march</span>

- 编辑所有用 "texas" 和 "history" 标签标记的条目：

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@texas</span>` -and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@history</span>` --edit`
