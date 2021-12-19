---
layout: page
title: linux/dstat (English)
description: "Versatile tool for generating system resource statistics."
content_hash: 27cde56288295e8da238ed10315b3a5679043faa
---
# dstat

Versatile tool for generating system resource statistics.
More information: <http://dag.wieers.com/home-made/dstat>.

- Display CPU, disk, net, paging and system statistics:

`dstat`

- Display statistics every 5 seconds and 4 updates only:

`dstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Display CPU and memory statistics only:

`dstat --cpu --mem`

- List all available dstat plugins:

`dstat --list`

- Display the process using the most memory and most CPU:

`dstat --top-mem --top-cpu`

- Display battery percentage and remaining battery time:

`dstat --battery --battery-remain`
