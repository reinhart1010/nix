---
layout: page
title: linux/ip-route-get (English)
description: "Get a single route to a destination and print its contents exactly as the kernel sees it."
content_hash: 5325c5b99b6ca0f25b1615f8dcf6877935f80b6d
last_modified_at: 2024-11-01
tldri18n_status: 2
---
# ip route get

Get a single route to a destination and print its contents exactly as the kernel sees it.
More information: <https://manned.org/ip-route>.

- Print route to a destination:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- Print route to a destination from a specific source address:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>

- Print route to a destination for packets arriving on a specific interface:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` iif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Print route to a destination, forcing output through a specific interface:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` oif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Print route to a destination with a specified Type of Service (ToS):

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` tos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x10</span>

- Print route to a destination using a specific VRF (Virtual Routing and Forwarding) instance:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` vrf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myvrf</span>
