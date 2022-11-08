---
layout: page
title: linux/ip-route-show (English)
description: "Display subcommand for IP Routing table management."
content_hash: 646a147a5f48b9ad2f5e2338686dde02450f3d96
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip route show

Display subcommand for IP Routing table management.
More information: <https://manned.org/ip-route>.

- Display the routing table:

`ip route show`

- Display the main routing table (same as first example):

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- Display the local routing table:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- Display all routing tables:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- List routes from a given device only:

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- List routes within a given scope:

`ip route show scope link`

- Display the routing cache:

`ip route show cache`

- Display only IPv6 or IPv4 routes:

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`
