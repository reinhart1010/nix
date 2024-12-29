---
layout: page
title: common/readarray (English)
description: "Read lines from `stdin` into an array."
content_hash: 31eb7f52e2717e759727561d97734464906edc91
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# readarray

Read lines from `stdin` into an array.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactively input lines into an array:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_name</span>

- Read lines from a file and insert them in an array:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Remove trailing deliminators (newline by default):

`readarray -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Copy at most the specified number of lines:

`readarray -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_name</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
