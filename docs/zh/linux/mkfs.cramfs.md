---
layout: page
title: linux/mkfs.cramfs (中文)
description: "创建一个 ROM 文件系统，放置在分区内。"
content_hash: 1a010e5cb254bfc00dbc72cc25cc9f8c5e5e1913
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.cramfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.cramfs

创建一个 ROM 文件系统，放置在分区内。
更多信息：<https://manned.org/mkfs.cramfs>.

- 在设备 b 的第 1 个分区内创建一个 ROM 文件系统（`sdb1`）：

`mkfs.cramfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷名的 ROM 文件系统：

`mkfs.cramfs -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
