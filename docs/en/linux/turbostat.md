---
layout: page
title: linux/turbostat (English)
description: "Report processor topology, frequency, temperature, power, and idle statistics."
content_hash: e83ff551ee4d6d8b8e67ceb9d77980dea67e8932
last_modified_at: 2024-06-08
tldri18n_status: 2
---
# turbostat

Report processor topology, frequency, temperature, power, and idle statistics.
More information: <https://manned.org/turbostat.8>.

- Display statistics every 5 seconds:

`sudo turbostat`

- Display statistics every specified amount of seconds:

`sudo turbostat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_seconds</span>

- Do not decode and print the system configuration header information:

`sudo turbostat --quiet`

- Display useful information about CPU every 1 second, without header information:

`sudo turbostat --quiet --interval 1 --cpu 0-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CPU_thread_count</span>` --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- Display help:

`turbostat --help`
