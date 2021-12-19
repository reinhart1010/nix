---
layout: page
title: linux/tracepath (English)
description: "Trace the path to a network host discovering MTU along this path."
content_hash: d41edc7bb97b32f2e9a7432f0e1ccc6fbc696676
---
# tracepath

Trace the path to a network host discovering MTU along this path.
More information: <https://manned.org/tracepath>.

- A preferred way to trace the path to a host:

`tracepath -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33434</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Specify the initial destination port, useful with non-standard firewall settings:

`tracepath -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `

- Print both hostnames and numerical IP addresses:

`tracepath -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Specify a maximum TTL (number of hops):

`tracepath -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_hops</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Specify the initial packet length (defaults to 65535 for IPv4 and 128000 for IPv6):

`tracepath -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">packet_length</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Use only IPv6 addresses:

`tracepath -6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
