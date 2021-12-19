---
layout: page
title: linux/lvs (中文)
description: "显示逻辑卷信息。"
content_hash: 1225af5e64614761fc26aa4cb735f2f0d97080f2
related_topics:
  - title: English version
    url: /en/linux/lvs.html
    icon: bi bi-globe
---
# lvs

显示逻辑卷信息。
另见：`lvm`.
更多信息：<https://man7.org/linux/man-pages/man8/lvs.8.html>.

- 显示逻辑卷信息：

`lvs`

- 显示所有逻辑卷：

`lvs -a`

- 改变默认显示以显示更多细节：

`lvs -v`

- 只显示特定字段：

`lvs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">域名 1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">域名 2</span>

- 将字段附加到显示：

`lvs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">域名</span>

- 抑制标题行：

`lvs --noheadings`

- 使用特殊分隔符分隔特定字段：

`lvs --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">=</span>
