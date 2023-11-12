---
layout: page
title: linux/btrfs-filesystem (中文)
description: "管理 btrfs 文件系统。"
content_hash: 68a77f28688a291bde99b040cee37c245c9bd5cd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-filesystem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs filesystem

管理 btrfs 文件系统。
更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- 显示文件系统使用情况（可以选择以 root 身份运行以显示详细信息）：

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 显示各个设备的使用情况：

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 对 btrfs 文件系统上的单个文件进行碎片整理（避免在运行数据去重的同时运行）：

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向文件的路径</span>

- 递归对目录进行碎片整理（不跨越子卷边界）：

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向目录的路径</span>

- 强制将未写入的数据块同步到磁盘：

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 递归总结目录中文件的磁盘使用情况：

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向目录的路径</span>
