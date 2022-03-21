---
layout: page
title: linux/script (English)
description: "Record all terminal output to file."
content_hash: 3fbb2bc8d8e85fc1d217e3fbefae4d17c970e169
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

- Record timing information (data is outputted to the standard error):

`script -t 2> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timingfile</span>
