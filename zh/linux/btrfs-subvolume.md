---
layout: page
title: linux/btrfs-subvolume (中文)
description: "管理 btrfs 子卷和快照。"
content_hash: 70853095d1a6d462715ebbcbd40c085120ab717e
related_topics:
  - title: English version
    url: /en/linux/btrfs-subvolume.html
    icon: bi bi-globe
---
# btrfs subvolume

管理 btrfs 子卷和快照。
更多信息：<https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- 创建一个新的空子卷：

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向新子卷的路径</span>

- 列出指定文件系统中的所有子卷和快照：

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向 btrfs 文件系统的路径</span>

- 删除一个子卷：

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向子卷的路径</span>

- 创建现有子卷的只读快照：

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向源子卷的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向目标的路径</span>

- 创建现有子卷的读写快照：

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向源子卷的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向目标的路径</span>

- 显示有关子卷的详细信息：

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向子卷的路径</span>
