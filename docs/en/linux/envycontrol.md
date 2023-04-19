---
layout: page
title: linux/envycontrol (English)
description: "GPU switching utility for Nvidia Optimus laptops."
content_hash: 8c17ed69a05dd634ccf6eeb51d348bd75789c113
last_modified_at: 2023-04-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># envycontrol

GPU switching utility for Nvidia Optimus laptops.
More information: <https://github.com/bayasdev/envycontrol>.

- Switch between different GPU modes:

`sudo envycontrol -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nvidia|integrated|hybrid</span>

- Specify your display manager manually:

`envycontrol --dm`

- Check current GPU mode:

`sudo envycontrol --query`

- Reset settings:

`sudo envycontrol --reset`

- Display version:

`envycontrol --version`

- Display help:

`envycontrol --help`
