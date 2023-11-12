---
layout: page
title: linux/ip-route (English)
description: "IP Routing table management subcommand."
content_hash: ef7de6d33b8a4d92c4cbc20f99a9351ba29a8782
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/ip-route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip route

IP Routing table management subcommand.
More information: <https://manned.org/ip-route>.

- Display the routing table:

`ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Add a default route using gateway forwarding:

`sudo ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_ip</span>

- Add a default route using `eth0`:

`sudo ip route add default dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Add a static route:

`sudo ip route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Delete a static route:

`sudo ip route del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Change or replace a static route:

`sudo ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Show which route will be used by the kernel to reach an IP address:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip</span>
