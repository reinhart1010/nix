---
layout: page
title: common/ifconfig (English)
description: "Network Interface Configurator."
content_hash: 43576d96114665670cdf17d1b4a02e571fc1a100
last_modified_at: 2023-11-12
related_topics:
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

Network Interface Configurator.
More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- View network settings of an Ethernet adapter:

`ifconfig eth0`

- Display details of all interfaces, including disabled interfaces:

`ifconfig -a`

- Disable eth0 interface:

`ifconfig eth0 down`

- Enable eth0 interface:

`ifconfig eth0 up`

- Assign IP address to eth0 interface:

`ifconfig eth0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
