---
layout: page
title: linux/pmap (English)
description: "Report memory map of a process or processes."
content_hash: 83f3368627ff52a517245bdd949242540c8f3f84
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pmap

Report memory map of a process or processes.
More information: <https://manned.org/pmap>.

- Print memory map for a specific process id (PID):

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show the extended format:

`pmap --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show the device format:

`pmap --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Limit results to a memory address range specified by `low` and `high`:

`pmap --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">high</span>

- Print memory maps for multiple processes:

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>
