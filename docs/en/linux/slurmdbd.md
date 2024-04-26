---
layout: page
title: linux/slurmdbd (English)
description: "A secure enterprise-wide interface to a database for Slurm."
content_hash: f6df681c160a244215ff683eae06247f35cf2c40
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# slurmdbd

A secure enterprise-wide interface to a database for Slurm.
More information: <https://slurm.schedmd.com/slurmdbd.html>.

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmdbd -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Change the working directory of `slurmdbd` to the LogFile path or to `/var/tmp`:

`slurmdbd -s`

- Display help:

`slurmdbd -h`

- Display version:

`slurmdbd -V`
