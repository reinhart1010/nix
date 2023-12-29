---
layout: page
title: common/orca-c (English)
description: "A C-port of the ORCA live programming environment."
content_hash: e2c5000b5eedde6286dd80b7c727deaa0ceb2d06
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# orca-c

A C-port of the ORCA live programming environment.
ORCA is an esoteric programming language for creating procedural sequencers.
More information: <https://github.com/hundredrabbits/Orca-c>.

- Start ORCA with an empty workspace:

`orca-c`

- Start ORCA and open a specific file:

`orca-c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.orca</span>

- Start ORCA and set a specific tempo (defaults to 120):

`orca-c --bpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beats_per_minute</span>

- Start ORCA and set the size of the grid:

`orca-c --initial-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columns</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows</span>

- Start ORCA and set the maximum number of undo steps (defaults to 100):

`orca-c --undo-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limit</span>

- Show the main menu inside of ORCA:

`F1`

- Show all shortcuts inside of ORCA:

`?`

- Show all ORCA operators inside of ORCA:

`<Ctrl> + g`
