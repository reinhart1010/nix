---
layout: page
title: linux/uprecords (English)
description: "Displays a summary of historical uptime records."
content_hash: 8f0b73ddf2b2b1262b4c0a96138a354372f95184
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# uprecords

Displays a summary of historical uptime records.
More information: <https://manned.org/uprecords>.

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
