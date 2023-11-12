---
layout: page
title: linux/ip-link (English)
description: "Manage network interfaces."
content_hash: a9a81756bc6de76e335cdfbc3096a70257ebb782
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/ip-link.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip link

Manage network interfaces.
More information: <https://man7.org/linux/man-pages/man8/ip-link.8.html>.

- Show information about all network interfaces:

`ip link`

- Show information about a specific network interface:

`ip link show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>

- Bring a network interface up or down:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Give a meaningful name to a network interface:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` alias "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LAN Interface</span>`"`

- Change the MAC address of a network interface:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff</span>

- Change the MTU size for a network interface to use jumbo frames:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9000</span>
