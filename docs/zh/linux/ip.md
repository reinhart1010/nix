---
layout: page
title: linux/ip (中文)
description: "显示/操作路由、设备、策略路由和隧道。"
content_hash: 7e978a915c8a1c4f083b015104c6ad7bbceb1798
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/ip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

显示/操作路由、设备、策略路由和隧道。
一些子命令（例如 `address`）有自己的使用文档。
更多信息：<https://www.manned.org/ip.8>.

- 列出带有详细信息的接口：

`ip address`

- 列出带有简要网络层信息的接口：

`ip -brief address`

- 列出带有简要链路层信息的接口：

`ip -brief link`

- 显示路由表：

`ip route`

- 显示邻居（ARP 表）：

`ip neighbour`

- 使接口启动/关闭：

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- 向接口添加/删除 IP 地址：

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- 添加默认路由：

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
