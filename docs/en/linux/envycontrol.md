---
layout: page
title: linux/envycontrol (English)
description: "GPU switching utility for Nvidia Optimus laptops."
content_hash: f69b7351382622b21767008661db63b3432214fa
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# envycontrol

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

- Display help:

`envycontrol --help`

- Display version:

`envycontrol --version`
