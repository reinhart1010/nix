---
layout: page
title: linux/ethtool (English)
description: "Display and modify Network Interface Controller (NIC) parameters."
content_hash: 4b06d0ac5b5d081a4e072baa263bb50b4b283b0b
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# ethtool

Display and modify Network Interface Controller (NIC) parameters.
More information: <http://manned.org/ethtool>.

- Display the current settings for an interface:

`ethtool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the driver information for an interface:

`ethtool --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display all supported features for an interface:

`ethtool --show-features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the network usage statistics for an interface:

`ethtool --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Blink one or more LEDs on an interface for 10 seconds:

`ethtool --identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Set the link speed, duplex mode, and parameter auto-negotiation for a given interface:

`ethtool -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10|100|1000</span>` duplex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">half|full</span>` autoneg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
