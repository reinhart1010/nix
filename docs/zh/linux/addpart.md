---
layout: page
title: linux/addpart (中文)
description: "将特定分区的存在告知 Linux 内核。"
content_hash: c68d54eae3338f14b944f74cf21fe646d4f07feb
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/addpart.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/addpart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addpart

将特定分区的存在告知 Linux 内核。
这个命令是 `add partition` ioctl 的简单封装。
更多信息：<https://manned.org/addpart>.

- 将特定分区的存在告知 Linux 内核：

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">设备名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分区名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">起始点</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">长度</span>
