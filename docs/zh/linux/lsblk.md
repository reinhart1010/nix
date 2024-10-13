---
layout: page
title: linux/lsblk (中文)
description: "列出设备信息。"
content_hash: 4417349e89df7e005742a13a50a10df6b291280b
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsblk.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsblk

列出设备信息。
更多信息：<https://manned.org/lsblk>.

- 以树状格式列出所有存储设备：

`lsblk`

- 同时列出空设备：

`lsblk -a`

- 以字节为单位而不是以人类可读的格式打印 SIZE 列：

`lsblk -b`

- 输出文件系统信息：

`lsblk -f`

- 输出块设备的拓扑结构：

`lsblk -t`

- 排除由逗号分隔的主要设备编号列表指定的设备：

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7,...</span>

- 使用逗号分隔的列列表显示自定义摘要：

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...</span>
