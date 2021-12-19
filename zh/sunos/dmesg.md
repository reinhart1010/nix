---
layout: page
title: sunos/dmesg (中文)
description: "将内核消息写入标准输出。"
content_hash: 989e9c223bc6f9c9278643322b11427c86bd04bc
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
---
# dmesg

将内核消息写入标准输出。
更多信息：<https://www.unix.com/man-page/sunos/1m/dmesg>.

- 显示内核消息：

`dmesg`

- 显示此系统上可用的物理内存：

`dmesg | grep -i memory`

- 一次显示一页内核消息：

`dmesg | less`
