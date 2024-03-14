---
layout: page
title: linux/pmap (English)
description: "Report memory map of a process or processes."
content_hash: 14a4d0a515e57a9ddf6486decd02ee90ff01eab7
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# pmap

Report memory map of a process or processes.
More information: <https://manned.org/pmap>.

- Print memory map for a specific process ID (PID):

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show the extended format:

`pmap --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show the device format:

`pmap --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Limit results to a memory address range specified by `low` and `high`:

`pmap --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">high</span>

- Print memory maps for multiple processes:

`pmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>
