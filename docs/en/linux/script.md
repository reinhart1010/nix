---
layout: page
title: linux/script (English)
description: "Record all terminal output to file."
content_hash: c1b492840fbd1578992e53560f72aef7fe895caf
last_modified_at: 2023-08-09
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

`script -t 2> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timingfile</span>
