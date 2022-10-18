---
layout: page
title: common/ac (中文)
description: "打印用户连接时间的统计数据。"
content_hash: 2e8c0e3c09126fa8f669282bff99c7d0af6286c3
related_topics:
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ac

打印用户连接时间的统计数据。
更多信息：<https://man.openbsd.org/ac>.

- 打印当前用户连接的时间，以小时为单位：

`ac`

- 打印用户连接的时间，以小时为单位：

`ac -p`

- 打印一个特定用户的连接时间，以小时为单位：

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 打印一个特定用户每天连接的时间，以小时为单位（包括总数）：

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>
