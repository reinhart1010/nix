---
layout: page
title: linux/mkfs.fat (中文)
description: "在分区内创建一个 MS-DOS 文件系统。"
content_hash: d5dc5feb4c5382c2b0ef1f7e05335c48f3799aa9
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.fat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.fat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.fat

在分区内创建一个 MS-DOS 文件系统。
更多信息：<https://manned.org/mkfs.fat>.

- 在设备 b 的分区 1 内创建一个 FAT 文件系统（`sdb1`）：

`mkfs.fat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷名的文件系统：

`mkfs.fat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷 ID 的文件系统：

`mkfs.fat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 使用 5 个而不是 2 个文件分配表：

`mkfs.fat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
