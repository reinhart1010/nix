---
layout: page
title: linux/slurmdbd (English)
description: "Provides a secure enterprise-wide interface to a database for Slurm."
content_hash: daae23c0574176f3f7956c897ebdc05f823f63e0
last_modified_at: 2023-10-22
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># slurmdbd

Provides a secure enterprise-wide interface to a database for Slurm.
More information: <https://slurm.schedmd.com/slurmdbd.html>.

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmdbd -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Change the working directory of `slurmdbd` to the LogFile path or to `/var/tmp`:

`slurmdbd -s`

- Display help:

`slurmdbd -h`

- Display version:

`slurmdbd -V`
