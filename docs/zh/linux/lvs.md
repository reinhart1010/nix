---
layout: page
title: linux/lvs (中文)
description: "显示逻辑卷信息。"
content_hash: 5f58a979c227701d7c9783d54fe4270f8993e1b2
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/linux/lvs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lvs

显示逻辑卷信息。
另见：`lvm`.
更多信息：<https://manned.org/lvs>.

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
