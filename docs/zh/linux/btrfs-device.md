---
layout: page
title: linux/btrfs-device (中文)
description: "管理 btrfs 文件系统中的设备。"
content_hash: 49ee75878933e7976371003405f569b3320bee40
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-device.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-device.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs device

管理 btrfs 文件系统中的设备。
更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- 将一个或多个设备添加到 btrfs 文件系统中：

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向设备1的路径</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向设备2的路径</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向 btrfs 文件系统的路径</span>

- 从 btrfs 文件系统中删除设备：

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向设备的路径|设备 ID</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- 显示错误统计：

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向 btrfs 文件系统的路径</span>

- 扫描所有磁盘并将所有检测到的 btrfs 文件系统通知内核：

`sudo btrfs device scan --all-devices`

- 显示详细的每个磁盘的空间分配统计信息：

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向 btrfs 文件系统的路径</span>
