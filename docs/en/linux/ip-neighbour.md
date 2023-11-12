---
layout: page
title: linux/ip-neighbour (English)
description: "Neighbour/ARP tables management IP subcommand."
content_hash: b73ccdcdef705b99c201ffd7b92b58866a37348f
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/ip-neighbour.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip neighbour

Neighbour/ARP tables management IP subcommand.
More information: <https://manned.org/ip-neighbour.8>.

- Display the neighbour/ARP table entries:

`ip neighbour`

- Remove entries in the neighbour table on device `eth0`:

`sudo ip neighbour flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Perform a neighbour lookup and return a neighbour entry:

`ip neighbour get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lookup_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Add or delete an ARP entry for the neighbour IP address to `eth0`:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|del</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` nud reachable`

- Change or replace an ARP entry for the neighbour IP address to `eth0`:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_mac_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
