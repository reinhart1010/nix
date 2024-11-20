---
layout: page
title: common/qemu-img (中文)
description: "创建和操作 Quick Emulator 虚拟硬盘镜像。"
content_hash: a8afeda10566aa2513a86813008904b85d293169
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qemu-img.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qemu-img.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qemu-img

创建和操作 Quick Emulator 虚拟硬盘镜像。
更多信息：<https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- 创建一个指定大小（以 GB 为单位）的磁盘镜像：

`qemu-img create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gigabytes</span>`G`

- 显示有关磁盘镜像的信息：

`qemu-img info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>

- 增加或减少镜像大小：

`qemu-img resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gigabytes</span>`G`

- 导出指定磁盘镜像每个扇区的分配状态：

`qemu-img map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>

- 将 VMware 的 .vmdk 磁盘镜像转换为 KVM 的 .qcow2 磁盘镜像：

`qemu-img convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vmdk</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.vmdk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.qcow2</span>
