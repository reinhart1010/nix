---
layout: page
title: linux/uprecords (English)
description: "Displays a summary of historical uptime records."
content_hash: faf8250ba559fc4f78a8298c26095eda37b23cbf
---
# uprecords

Displays a summary of historical uptime records.

- Display a summary of the top 10 historical uptime records:

`uprecords`

- Display the top 25 records:

`uprecords -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Display the downtime between reboots instead of the kernel version:

`uprecords -d`

- Show the most recent reboots:

`uprecords -B`

- Don't truncate information:

`uprecords -w`
