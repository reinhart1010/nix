---
layout: page
title: common/uniq (English)
description: "Output the unique lines from a input or file."
content_hash: ad58f549452e3dc89a082784ce493fbcb50d9099
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# uniq

Output the unique lines from a input or file.
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
