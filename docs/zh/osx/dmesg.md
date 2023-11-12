---
layout: page
title: osx/dmesg (中文)
description: "将内核消息写入标准输出。"
content_hash: 95a32012b6a07b21d617f4652fb4ec93ea6f4f0a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

将内核消息写入标准输出。
更多信息：<https://www.manpagez.com/man/8/dmesg/>.

- 显示内核消息：

`dmesg`

- 显示此系统上有多少可用的物理内存：

`dmesg | grep -i memory`

- 一次显示一页内核消息：

`dmesg | less`
