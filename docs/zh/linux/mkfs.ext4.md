---
layout: page
title: linux/mkfs.ext4 (中文)
description: "在分区内创建一个 ext4 文件系统。"
content_hash: c62be163710112eb991c65a5f6259e74c94887c1
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.ext4.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.ext4

在分区内创建一个 ext4 文件系统。
更多信息：<https://manned.org/mkfs.ext4>.

- 在设备 b 的分区 1 内创建一个 ext4 文件系统（`sdb1`）：

`sudo mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷标签的 ext4 文件系统：

`sudo mkfs.ext4 -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
