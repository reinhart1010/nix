---
layout: page
title: osx/dmesg (中文)
description: "将内核消息写入标准输出。"
content_hash: 67cc361ac9a90d696e57f9aabc7a7fe3b855f612
last_modified_at: 2024-01-31
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
更多信息：<https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- 显示内核消息：

`dmesg`

- 显示此系统上有多少可用的物理内存：

`dmesg | grep -i memory`

- 一次显示一页内核消息：

`dmesg | less`
