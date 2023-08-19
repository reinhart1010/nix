---
layout: page
title: linux/swapoff (English)
description: "Disable devices and files for swapping."
content_hash: 2d19114ed7fe1be38c9ff2f73faa7927f4142117
last_modified_at: 2023-08-19
---
# swapoff

Disable devices and files for swapping.
Note: `path/to/file` can either point to a regular file or a swap partition.
More information: <https://manned.org/swapoff>.

- Disable a given swap area:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Disable all swap areas in `/proc/swaps`:

`swapoff --all`

- Disable a swap partition by its label:

`swapoff -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>
