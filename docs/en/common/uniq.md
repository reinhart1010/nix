---
layout: page
title: common/uniq (English)
description: "Output the unique lines from the given input or file."
content_hash: ab042deb55d50de3bf4d66f50893ff4972db2718
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# uniq

Output the unique lines from the given input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
More information: <https://www.gnu.org/software/coreutils/uniq>.

- Display each line once:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq`

- Display only unique lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -u`

- Display only duplicate lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -d`

- Display number of occurrences of each line along with that line:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -c`

- Display number of occurrences of each line, sorted by the most frequent:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -c | sort -nr`
