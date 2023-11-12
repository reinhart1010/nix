---
layout: page
title: linux/lspci (中文)
description: "列出所有 PCI 设备。"
content_hash: 52fa4464bc57c4018a4ef58d296870c7cf278409
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lspci.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lspci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lspci

列出所有 PCI 设备。
更多信息：<https://manned.org/lspci>.

- 显示设备的简要列表：

`lspci`

- 显示额外信息：

`lspci -v`

- 显示处理每个设备的驱动程序和模块：

`lspci -k`

- 显示特定设备：

`lspci -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:18.3</span>

- 以可读形式转储信息：

`lspci -vm`
