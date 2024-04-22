---
layout: page
title: linux/mkfs.cramfs (中文)
description: "创建一个 ROM 文件系统，放置在分区内。"
content_hash: 1a010e5cb254bfc00dbc72cc25cc9f8c5e5e1913
last_modified_at: 2024-04-22
related_topics:
  - title: English version
    url: /en/linux/mkfs.cramfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.cramfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.cramfs

创建一个 ROM 文件系统，放置在分区内。
更多信息：<https://manned.org/mkfs.cramfs>.

- 在设备 b 的第 1 个分区内创建一个 ROM 文件系统（`sdb1`）：

`mkfs.cramfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷名的 ROM 文件系统：

`mkfs.cramfs -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
