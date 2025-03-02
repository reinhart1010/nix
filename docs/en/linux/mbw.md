---
layout: page
title: linux/mbw (English)
description: "Memory Bandwidth Benchmark."
content_hash: 47cdc1a1f0250e7255abf21b53c4364dfee3a2a1
last_modified_at: 2025-03-02
related_topics:
  - title: 中文 version
    url: /zh/linux/mbw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mbw

Memory Bandwidth Benchmark.
More information: <https://github.com/raas/mbw>.

- Run 3 memory bandwidth tests with 512MB size:

`mbw -n 3 512`

- Run 3 memory bandwidth tests with 512MB memory size, output only statistics, not averages:

`mbw -n 3 -q -a 512`

- Run memcpy test 3 times with 512MB size, only display statistics:

`mbw -n 3 -q -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` 512`

- Run the memcpy test 10 times with 1024 byte blocks allocated 8192MB of memory:

`mbw -n 10 -q -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -b 1024 8192`

- Run dumb test with 2048MB size, output only statistics, run forever:

`mbw -n 0 -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -q 2048`
