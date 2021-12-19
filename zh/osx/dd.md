---
layout: page
title: osx/dd (中文)
description: "转换并复制文件。"
content_hash: 0b28f3baa6f624cfd7583b3d79af4c2e4b474645
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
---
# dd

转换并复制文件。
更多信息：<https://ss64.com/osx/dd.html>.

- 从 isohybrid 文件（如 archlinux-xxx.iso）制作可用于引导系统启动的 USB 驱动器：

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb 设备</span>

- 将驱动器克隆到具有 4MB 块的另一个驱动器并忽略错误：

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源设备</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标设备</span>` bs=4m conv=noerror`

- 使用内核随机驱动程序生成 100 个随机字节的文件：

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标驱动器，接收随机数据文件名</span>` bs=100 count=1`

- 对磁盘的写入性能进行基准测试：

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1GB 的文件名</span>` bs=1024 count=1000000`
