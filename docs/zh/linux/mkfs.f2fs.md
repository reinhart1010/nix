---
layout: page
title: linux/mkfs.f2fs (中文)
description: "在分区内创建一个 F2FS 文件系统。"
content_hash: 3a416dc1909954a1a081bac1024a5bdac9d66a5e
last_modified_at: 2024-04-22
related_topics:
  - title: English version
    url: /en/linux/mkfs.f2fs.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/mkfs.f2fs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.f2fs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.f2fs

在分区内创建一个 F2FS 文件系统。
更多信息：<https://manned.org/mkfs.f2fs>.

- 在设备 b 的第 1 个分区内创建一个 F2FS 文件系统（`sdb1`）：

`sudo mkfs.f2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷标签的 F2FS 文件系统：

`sudo mkfs.f2fs -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
