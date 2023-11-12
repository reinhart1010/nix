---
layout: page
title: linux/ip-address (English)
description: "IP Address management subcommand."
content_hash: ea36ac2a473e6efaed2c49b9c0706b81f3a8e348
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ip-address.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-address.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-address.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip address

IP Address management subcommand.
More information: <https://manned.org/ip-address>.

- List network interfaces and their associated IP addresses:

`ip address`

- Filter to show only active network interfaces:

`ip address show up`

- Display information about a specific network interface:

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Add an IP address to a network interface:

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Remove an IP address from a network interface:

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Delete all IP addresses in a given scope from a network interface:

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>
