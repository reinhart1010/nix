---
layout: page
title: linux/vnstat (English)
description: "A console-based network traffic monitor."
content_hash: dbc29a07beb2774935b0249dfe5a0fbaf49650e3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vnstat

A console-based network traffic monitor.
More information: <https://manned.org/vnstat>.

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
