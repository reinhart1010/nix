---
layout: page
title: linux/dmesg (中文)
description: "显示或控制内核环形缓冲区。"
content_hash: 4925fcc559ede3ddae9c72f666da4cfac239ead8
last_modified_at: 2024-09-30
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

显示或控制内核环形缓冲区。
更多信息：<https://manned.org/dmesg>.

- 显示来自内核环形缓冲区的所有消息：

`sudo dmesg`

- 只显示严重错误级别的消息：

`sudo dmesg --level err`

- 等待新消息。仅在具有可读性的系统上支持此功能，类似于 `tail -f`（从内核 3.5.0 版本开始）：

`sudo dmesg -w`

- 显示此系统上有多少物理内存可用：

`sudo dmesg | grep -i memory`

- 以分页方式显示内核缓冲区的所有消息：

`sudo dmesg | less`

- 打印人类可读的时间戳（从内核 3.5.0 版本开始）：

`sudo dmesg -T`

- 启用人类可读的输出：

`sudo dmesg -H`

- 着色输出：

`sudo dmesg -L`
