---
layout: page
title: linux/btrfs (中文)
description: "一种基于写时复制（COW）原理的 Linux 文件系统。"
content_hash: cd9062b6980862416063287d9d5a51e831d91644
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
---
# btrfs

一种基于写时复制（COW）原理的 Linux 文件系统。
此命令也有关于其子命令的文件，例如：`btrfs device`.
更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- 创建子卷：

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向子卷的路径</span>

- 列出子卷：

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 显示空间使用情况信息：

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 启用配额（quota）：

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向子卷的路径</span>

- 显示配额（quota）：

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向子卷的路径</span>
