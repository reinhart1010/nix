---
layout: page
title: common/qemu (中文)
description: "通用机器模拟器和虚拟化器。"
content_hash: 1e2269623c231502e337bf98f7f22432a319e4ba
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qemu.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qemu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qemu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qemu

通用机器模拟器和虚拟化器。
支持多种 CPU 架构。
更多信息：<https://www.qemu.org>.

- 启动镜像并模拟 i386 架构：

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>

- 启动镜像并模拟 x64 架构：

`qemu-system-x86_64 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>

- 使用现场 ISO 镜像启动 QEMU 实例：

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">操作系统镜像.iso</span>` -boot d`

- 为实例指定 RAM 大小：

`qemu-system-i386 -m 256 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像名称.img</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">操作系统镜像.iso</span>` -boot d`

- 从物理设备启动（例如，从 USB 启动以测试可启动介质）：

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/存储设备</span>
