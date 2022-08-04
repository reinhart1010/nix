---
layout: page
title: linux/avahi-browse (中文)
description: "显示通过 mDNS/DNS-SD 暴露在本地网络的服务和主机。"
content_hash: 37a64cc0bffe66d0ea93e8042f5b25efc2a637ee
related_topics:
  - title: English version
    url: /en/linux/avahi-browse.html
    icon: bi bi-globe
---
# avahi-browse

显示通过 mDNS/DNS-SD 暴露在本地网络的服务和主机。
Avahi 与苹果设备的 Bonjour（Zeroconf）兼容。
更多信息：<https://www.avahi.org/>.

- 列出本地网络中的所有服务和他们的地址与端口，忽略他们本地的地址和端口：

`avahi-browse --all --resolve --ignore-local`

- 列出所有的域名：

`avahi-browse --browse-domains`

- 只搜索一个特定的域名：

`avahi-browse --all --domain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>
