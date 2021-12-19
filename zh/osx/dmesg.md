---
layout: page
title: osx/dmesg (中文)
description: "将内核消息写入标准输出。"
content_hash: c95f38e3106c6c60ba528903c9c79f59fb8824bf
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
---
# dmesg

将内核消息写入标准输出。

- 显示内核消息：

`dmesg`

- 显示此系统上有多少可用的物理内存：

`dmesg | grep -i memory`

- 一次显示一页内核消息：

`dmesg | less`
