---
layout: page
title: linux/boltctl (中文)
description: "控制雷电（thunderbolt）设备。"
content_hash: 6cf4d2e75688fed02ba056c045643d545b26318f
related_topics:
  - title: English version
    url: /en/linux/boltctl.html
    icon: bi bi-globe
---
# boltctl

控制雷电（thunderbolt）设备。
更多信息：<https://manned.org/boltctl>.

- 列出已连接并授权的设备：

`boltctl`

- 列出已连接的设备，且包含未授权的设备：

`boltctl list`

- 临时授权一个设备：

`boltctl authorize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备uuid</span>

- 授权并记住一个设备：

`boltctl enroll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备uuid</span>

- 取消一个设备的授权：

`boltctl forget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备uuid</span>

- 显示一个设备的详细信息：

`boltctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备uuid</span>
