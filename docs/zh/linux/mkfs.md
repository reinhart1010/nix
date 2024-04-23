---
layout: page
title: linux/mkfs (中文)
description: "在硬盘分区上建立一个 Linux 文件系统。"
content_hash: c625f81e4027cb8ed9d4cf325e628fb5227ced5b
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/mkfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mkfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs

在硬盘分区上建立一个 Linux 文件系统。
该命令已被废弃，建议使用特定文件系统的 mkfs.<type> 工具。
更多信息：<https://manned.org/mkfs>.

- 在分区上建立一个 Linux ext2 文件系统：

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- 建立指定类型的文件系统：

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- 建立指定类型的文件系统并检查坏块：

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>
