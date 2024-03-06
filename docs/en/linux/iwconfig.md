---
layout: page
title: linux/iwconfig (English)
description: "Configure and show the parameters of a wireless network interface."
content_hash: 736b81a7b9ee27072f668fc1d74a7a1b9cb7cd4a
last_modified_at: 2024-03-06
tldri18n_status: 2
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

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto</span>
