---
layout: page
title: common/ulimit (中文)
description: "获取和设置用户限制。"
content_hash: 32891ee0671fe0e1a171f7f218b4d7ff317e200b
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/ulimit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ulimit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ulimit

获取和设置用户限制。
更多信息：<https://manned.org/ulimit>.

- 获取所有用户限制的属性：

`ulimit -a`

- 获取同时打开文件数量的硬限制：

`ulimit -H -n`

- 获取同时打开文件数量的软限制：

`ulimit -S -n`

- 设置每个用户的最大进程限制：

`ulimit -u 30`
