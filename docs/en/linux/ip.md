---
layout: page
title: linux/ip (English)
description: "Show/manipulate routing, devices, policy routing and tunnels."
content_hash: d44055b4e13c8836f7528e6ff7fcd140874f93d0
last_modified_at: 2023-06-13
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
---
# ip

Show/manipulate routing, devices, policy routing and tunnels.
Some subcommands such as `ip address` have their own usage documentation.
More information: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- List interfaces with detailed info:

`ip address`

- List interfaces with brief network layer info:

`ip -brief address`

- List interfaces with brief link layer info:

`ip -brief link`

- Display the routing table:

`ip route`

- Show neighbors (ARP table):

`ip neighbour`

- Make an interface up/down:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` up/down`

- Add/Delete an IP address to an interface:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Add a default route:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
