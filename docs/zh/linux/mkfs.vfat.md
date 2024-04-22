---
layout: page
title: linux/mkfs.vfat (中文)
description: "在分区内创建一个 MS-DOS 文件系统。"
content_hash: 8e4a7e12dca34fca88045baafa0bca23e195ac51
last_modified_at: 2024-04-22
related_topics:
  - title: English version
    url: /en/linux/mkfs.vfat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.vfat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.vfat

在分区内创建一个 MS-DOS 文件系统。
更多信息：<https://manned.org/mkfs.vfat>.

- 在设备 b 的分区 1 内创建一个 vfat 文件系统（`sdb1`）：

`mkfs.vfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷名的文件系统：

`mkfs.vfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷 ID 的文件系统：

`mkfs.vfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 使用 5 个而不是 2 个文件分配表：

`mkfs.vfat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
