---
layout: page
title: linux/slurmctld (English)
description: "Monitor all other Slurm daemons and resources, accept work (jobs), and allocate resources to those jobs."
content_hash: 6d77bba4b8324e3be0686728a4945fc807abcd35
last_modified_at: 2023-10-22
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># slurmctld

Monitor all other Slurm daemons and resources, accept work (jobs), and allocate resources to those jobs.
More information: <https://slurm.schedmd.com/slurmctld.html>.

- Clear all previous `slurmctld` states from its last checkpoint:

`slurmctld -c`

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmctld -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Write log messages to the specified file:

`slurmctld -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Display help:

`slurmctld -h`

- Display version:

`slurmctld -V`
