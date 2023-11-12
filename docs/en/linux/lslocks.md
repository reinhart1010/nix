---
layout: page
title: linux/lslocks (English)
description: "List local system locks."
content_hash: d216cd800f7ee943c4623ada9049af30cb0927fb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lslocks

List local system locks.
More information: <https://manned.org/lslocks>.

- List all local system locks:

`lslocks`

- List locks with defined column headers:

`lslocks --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COMMAND</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PATH</span>

- List locks producing a raw output (no columns), and without column headers:

`lslocks --raw --noheadings`

- List locks by PID input:

`lslocks --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- List locks with JSON output to `stdout`:

`lslocks --json`
