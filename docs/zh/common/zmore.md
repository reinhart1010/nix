---
layout: page
title: common/zmore (中文)
description: "使用 `more` 查看 `gzip` 压缩文件。"
content_hash: fc3786caa93745858f8940136b67e838df5f1b0a
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zmore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zmore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zmore

使用 `more` 查看 `gzip` 压缩文件。
更多信息：<https://manned.org/zmore>.

- 打开一个压缩文件：

`zmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.txt.gz</span>

- 显示文件的下一页：

`<Space>`

- 在文件中搜索一个模式（按 `n` 跳转到下一个匹配项）：

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>

- 退出：

`q`

- 显示交互式命令帮助：

`h`
