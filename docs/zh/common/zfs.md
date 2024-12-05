---
layout: page
title: common/zfs (中文)
description: "管理 ZFS 文件系统。"
content_hash: a5c2ed51a153144d6d83163424fe1e380086441c
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zfs

管理 ZFS 文件系统。
更多信息：<https://manned.org/zfs>.

- 列出所有可用的 ZFS 文件系统：

`zfs list`

- 创建一个新的 ZFS 文件系统：

`zfs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称/文件系统名称</span>

- 删除一个 ZFS 文件系统：

`zfs destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称/文件系统名称</span>

- 创建一个 ZFS 文件系统的快照：

`zfs snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称/文件系统名称</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">快照名称</span>

- 在文件系统上启用压缩：

`zfs set compression=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称/文件系统名称</span>

- 更改文件系统的挂载点：

`zfs set mountpoint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/我的/挂载/路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存储池名称/文件系统名称</span>
