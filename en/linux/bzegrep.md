---
layout: page
title: linux/bzegrep (English)
description: "Find extended regular expression patterns in bzip2 compressed files using egrep."
content_hash: 4a5ff14b08d5a50f83ef361b986d1ceab46499a7
---
# bzegrep

Find extended regular expression patterns in bzip2 compressed files using egrep.
More information: <https://manned.org/bzegrep>.

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-sensitive):

`bzegrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`) in a compressed file (case-insensitive):

`bzegrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for lines that do not match a pattern:

`bzegrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print file name and line number for each match:

`bzegrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for lines matching a pattern, printing only the matched text:

`bzegrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively search files in a bzip2 compressed tar archive for a pattern:

`bzegrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
