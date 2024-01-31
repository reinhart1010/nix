---
layout: page
title: osx/diskutil (中文)
description: "用于管理本地磁盘和卷的实用程序。"
content_hash: 343830b5bae9489462c9e64cc2de2910df696f81
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

用于管理本地磁盘和卷的实用程序。
更多信息：<https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- 列出所有当前可用的磁盘、分区和已装入的卷：

`diskutil list`

- 修复卷的文件系统数据结构：

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标卷文件</span>

- 卸载卷：

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标卷文件</span>

- 弹出 CD/DVD（先卸载）：

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ 光驱文件名</span>
