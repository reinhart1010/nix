---
layout: page
title: common/act (中文)
description: "使用 Docker 本地运行 GitHub Actions."
content_hash: 3eeb42c71b87cbceb2f67841c674209301781e0b
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
---
# act

使用 Docker 本地运行 GitHub Actions.
更多信息：<https://github.com/nektos/act>.

- 列出可用的 actions 清单：

`act -l`

- 运行默认 event:

`act`

- 运行指定 event:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">事件类型</span>

- 运行指定 action:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- 非实际运行 actions（也就是 dry-run 模式）：

`act -n`

- 展示详细记录：

`act -v`
