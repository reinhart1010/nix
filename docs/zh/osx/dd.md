---
layout: page
title: osx/dd (中文)
description: "转换并复制文件。"
content_hash: bc3681aab8c260ecf079e5fa4e39eba79fe97457
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dd

转换并复制文件。
更多信息：<https://keith.github.io/xcode-man-pages/dd.1.html>.

- 从 isohybrid 文件（如 archlinux-xxx.iso）制作可用于引导系统启动的 USB 驱动器：

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb 设备</span>

- 将驱动器克隆到具有 4MB 块的另一个驱动器并忽略错误：

`dd bs=4m conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/源设备</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/目标设备</span>

- 使用内核随机驱动程序生成 100 个随机字节的文件：

`dd bs=100 count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标驱动器，接收随机数据文件名</span>

- 对磁盘的写入性能进行基准测试：

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1GB 的文件名</span>
