---
layout: page
title: osx/diskutil (中文)
description: "用于管理本地磁盘和卷的实用程序。"
content_hash: 1f02000c4d68f644fa1f77af7e8b8c67b954bf95
related_topics:
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
---
# diskutil

用于管理本地磁盘和卷的实用程序。
更多信息：<https://ss64.com/osx/diskutil.html>.

- 列出所有当前可用的磁盘、分区和已装入的卷：

`diskutil list`

- 修复卷的文件系统数据结构：

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标卷文件</span>

- 卸载卷：

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标卷文件</span>

- 弹出 CD/DVD（先卸载）：

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ 光驱文件名</span>
