---
layout: page
title: linux/slurmrestd (English)
description: "Interface to Slurm via REST API. It can be used in two modes: *Inetd Mode* & *Listen Mode*."
content_hash: b5a47b62639cfa992f6332d32cc40d024928410d
last_modified_at: 2023-10-22
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># slurmrestd

Interface to Slurm via REST API. It can be used in two modes: *Inetd Mode* & *Listen Mode*.
More information: <https://slurm.schedmd.com/slurmrestd.html>.

- Change the group ID (and drop supplemental groups) before processing client requests:

`slurmrestd --g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[host]:port | unix:/path/to/socket</span>

- Comma-delimited list of authentication plugins to load:

`slurmrestd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">authentication_plugins</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[host]:port | unix:/path/to/socket</span>

- Read Slurm configuration from the specified file:

`slurmrestd -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Change user ID before processing client request:

`slurmrestd -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id</span>

- Display help:

`slurmrestd -h`

- Display version:

`slurmrestd -V`
