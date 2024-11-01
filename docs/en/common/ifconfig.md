---
layout: page
title: common/ifconfig (English)
description: "Network Interface Configurator."
content_hash: 92b6165fa324278afbc77b1525c476e920ce078a
last_modified_at: 2024-11-01
related_topics:
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

Network Interface Configurator.
More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- View network settings of an interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>

- Display details of all interfaces, including disabled interfaces:

`ifconfig -a`

- Disable an interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` down`

- Enable an interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` up`

- Assign an IP address to an interface:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
