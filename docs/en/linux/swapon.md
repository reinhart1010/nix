---
layout: page
title: linux/swapon (English)
description: "Enable devices and files for swapping."
content_hash: 36ef26e9dbcfa29c39e3884bdf1399c90f7b84d8
last_modified_at: 2023-08-19
---
# swapon

Enable devices and files for swapping.
Note: `path/to/file` can either point to a regular file or a swap partition.
More information: <https://manned.org/swapon>.

- Show swap information:

`swapon`

- Enable a given swap area:

`swapon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Enable all swap areas specified in `/etc/fstab` except those with the `noauto` option:

`swapon --all`

- Enable a swap partition by its label:

`swapon -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>
