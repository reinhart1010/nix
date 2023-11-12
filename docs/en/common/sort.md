---
layout: page
title: common/sort (English)
description: "Sort lines of text files."
content_hash: 2dfb7989664c0fe2b5ee8d4b70633cc2d39d2b2c
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/sort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sort

Sort lines of text files.
More information: <https://www.gnu.org/software/coreutils/sort>.

- Sort a file in ascending order:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort a file in descending order:

`sort --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort a file in case-insensitive way:

`sort --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort a file using numeric rather than alphabetic order:

`sort --numeric-sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort `/etc/passwd` by the 3rd field of each line numerically, using ":" as a field separator:

`sort --field-separator=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- Sort a file preserving only unique lines:

`sort --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort a file, printing the output to the specified output file (can be used to sort a file in-place):

`sort --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sort numbers with exponents:

`sort --general-numeric-sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
