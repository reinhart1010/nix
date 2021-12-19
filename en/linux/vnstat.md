---
layout: page
title: linux/vnstat (English)
description: "A console-based network traffic monitor."
content_hash: 374a6f113a1f695a3f235b834d97024a5273ffae
---
# vnstat

A console-based network traffic monitor.

- Display traffic summary for all interfaces:

`vnstat`

- Display traffic summary for a specific network interface:

`vnstat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display live stats for a specific network interface:

`vnstat -l -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Show traffic statistics on an hourly basis for the last 24 hours using a bar graph:

`vnstat -hg`

- Measure and show average traffic for 30 seconds:

`vnstat -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
