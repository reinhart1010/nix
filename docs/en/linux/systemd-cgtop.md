---
layout: page
title: linux/systemd-cgtop (English)
description: "Show the top control groups of the local Linux control group hierarchy, ordered by their CPU, memory, or disk I/O load."
content_hash: 5502b6f5767e2072eb23383f7ab15314729f3a82
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-cgtop

Show the top control groups of the local Linux control group hierarchy, ordered by their CPU, memory, or disk I/O load.
See also: `top`.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-cgtop.html>.

- Start an interactive view:

`systemd-cgtop`

- Change the sort order:

`systemd-cgtop --order=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu|memory|path|tasks|io</span>

- Show the CPU usage by time instead of percentage:

`systemd-cgtop --cpu=percentage`

- Change the update interval in seconds (or one of these time units: `ms`, `us`, `min`):

`systemd-cgtop --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>

- Only count userspace processes (without kernel threads):

`systemd-cgtop -P`
