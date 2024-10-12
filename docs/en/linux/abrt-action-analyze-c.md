---
layout: page
title: linux/abrt-action-analyze-c (English)
description: "Calculate UUID for a problem data directory with `coredump`."
content_hash: 8dec0ddad4ca3aefcf6801eef4a4971f3aca2e51
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# abrt-action-analyze-c

Calculate UUID for a problem data directory with `coredump`.
More information: <https://manned.org/abrt-action-analyze-c>.

- Calculate and save the UUID for the current working directory:

`abrt-action-analyze-c`

- Calculate and save the UUID for a specific directory:

`abrt-action-analyze-c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Calculate and save the UUID verbosely:

`abrt-action-analyze-c -v`
