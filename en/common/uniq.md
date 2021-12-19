---
layout: page
title: common/uniq (English)
description: "Output the unique lines from the given input or file."
content_hash: 4c21b19df5a27067a663edae96a4f65c63038fb8
---
# uniq

Output the unique lines from the given input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
More information: <https://www.gnu.org/software/coreutils/uniq>.

- Display each line once:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | uniq`

- Display only unique lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | uniq -u`

- Display only duplicate lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | uniq -d`

- Display number of occurrences of each line along with that line:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | uniq -c`

- Display number of occurrences of each line, sorted by the most frequent:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` | uniq -c | sort -nr`
