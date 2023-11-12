---
layout: page
title: common/arp-scan (中文)
description: "发送 ARP 数据包到特定主机（指定 IP 地址或主机名），来扫描本地网络。"
content_hash: 7fb107e7f3e00abd2b3500023561801342a8c6de
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/arp-scan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp-scan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp-scan

发送 ARP 数据包到特定主机（指定 IP 地址或主机名），来扫描本地网络。
更多信息：<https://github.com/royhills/arp-scan>.

- 扫描当前本地网络：

`arp-scan --localnet`

- 扫描带有自定义位掩码的 IP 网络：

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- 扫描自定义范围内的 IP 网络：

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- 扫描带有自定义子网掩码的 IP 网络：

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
