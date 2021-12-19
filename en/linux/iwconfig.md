---
layout: page
title: linux/iwconfig (English)
description: "Configure and show the parameters of a wireless network interface."
content_hash: 051e17d4e10abc0e8d0588cc1825edc51cf9e1c4
---
# iwconfig

Configure and show the parameters of a wireless network interface.
More information: <https://manned.org/iwconfig>.

- Show the parameters and statistics of all the interfaces:

`iwconfig`

- Show the parameters and statistics of the specified interface:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Set the ESSID (network name) of the specified interface (e.g. eth0 or wlp2s0):

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_network_name</span>

- Set the operating mode of the specified interface:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ad hoc|Managed|Master|Repeater|Secondary|Monitor|Auto</span>
