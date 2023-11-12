---
layout: page
title: linux/perf (English)
description: "Framework for Linux performance counter measurements."
content_hash: 43c41ccb7f62a7efc32e5a1d6cdb23464eabd6a3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# perf

Framework for Linux performance counter measurements.
More information: <https://perf.wiki.kernel.org>.

- Display basic performance counter stats for a command:

`perf stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc hello.c</span>

- Display system-wide real-time performance counter profile:

`sudo perf top`

- Run a command and record its profile into `perf.data`:

`sudo perf record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Record the profile of an existing process into `perf.data`:

`sudo perf record -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Read `perf.data` (created by `perf record`) and display the profile:

`sudo perf report`
