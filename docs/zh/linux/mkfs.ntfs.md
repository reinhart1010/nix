---
layout: page
title: linux/mkfs.ntfs (中文)
description: "在分区内创建一个 NTFS 文件系统。"
content_hash: a8e673371004f438ad82624414fe037e8c6fff85
last_modified_at: 2024-04-22
related_topics:
  - title: English version
    url: /en/linux/mkfs.ntfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.ntfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.ntfs

在分区内创建一个 NTFS 文件系统。
更多信息：<https://manned.org/mkfs.ntfs>.

- 在设备 b 的分区 1 内创建一个 NTFS 文件系统（`sdb1`）：

`mkfs.ntfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷标签的文件系统：

`mkfs.ntfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有特定 UUID 的文件系统：

`mkfs.ntfs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
