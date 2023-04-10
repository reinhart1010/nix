---
layout: page
title: common/arp (中文)
description: "显示和操作系统的 ARP 缓存。"
content_hash: b85d49d657172786f17aac31c5c10b0dfcce8a12
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/arp.html
    icon: bi bi-globe
---
# arp

显示和操作系统的 ARP 缓存。
更多信息：<https://manned.org/arp>.

- 显示当前的 ARP 表：

`arp -a`

- 删除特定条目：

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">地址</span>

- 创建指定条目：

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MAC 地址</span>
