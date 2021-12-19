---
layout: page
title: linux/ipcalc (English)
description: "Perform simple operations and calculations on IP addresses and networks."
content_hash: bb13b532ead450982c196295f33e41e1779706d3
related_topics:
  - title: Deutsch version
    url: /de/linux/ipcalc.html
    icon: bi bi-globe
---
# ipcalc

Perform simple operations and calculations on IP addresses and networks.
More information: <https://manned.org/ipcalc>.

- Show information about an address or network with a given subnet mask:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>

- Show information about an address or network in CIDR notation:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Show the broadcast address of an address or network:

`ipcalc -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Show the network address of provided IP address and netmask:

`ipcalc -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Display geographic information about a given IP address:

`ipcalc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>
