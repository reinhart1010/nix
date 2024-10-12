---
layout: page
title: linux/script (English)
description: "Record all terminal output to file."
content_hash: cf2f4ccc188cf41af7da3d1c32dfebbceca4eec5
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# script

Record all terminal output to file.
More information: <https://manned.org/script>.

- Record a new session to a file named `typescript` in the current directory:

`script`

- Record a new session to a custom filepath:

`script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/session.out</span>

- Record a new session, appending to an existing file:

`script -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/session.out</span>

- Record timing information (data is outputted to `stderr`):

`script -t 2> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timing_file</span>

- Write out data as soon as it happens:

`script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
