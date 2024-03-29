---
layout: page
title: linux/pidstat (English)
description: "Show system resource usage, including CPU, memory, IO etc."
content_hash: ffc01d82a8fee148be2cfcfb1375483bfa648d0d
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# pidstat

Show system resource usage, including CPU, memory, IO etc.
More information: <https://manned.org/pidstat>.

- Show CPU statistics at a 2 second interval for 10 times:

`pidstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Show page faults and memory utilization:

`pidstat -r`

- Show input/output usage per process ID:

`pidstat -d`

- Show information on a specific PID:

`pidstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Show memory statistics for all processes whose command name include "fox" or "bird":

`pidstat -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fox|bird</span>`" -r -p ALL`
