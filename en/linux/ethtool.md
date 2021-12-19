---
layout: page
title: linux/ethtool (English)
description: "Display and modify Network Interface Controller (NIC) parameters."
content_hash: 149e3347b95e812d14ea0ac4d362154ccb9f96bf
---
# ethtool

Display and modify Network Interface Controller (NIC) parameters.
More information: <http://man7.org/linux/man-pages/man8/ethtool.8.html>.

- Display the current settings for an interface:

`ethtool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the driver information for an interface:

`ethtool --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the network usage statistics for an interface:

`ethtool --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Blink one or more LEDs on an interface for 10 seconds:

`ethtool --identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Set the link speed, duplex mode, and parameter auto-negotiation for a given interface:

`ethtool -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10|100|1000</span>` duplex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">half|full</span>` autoneg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
