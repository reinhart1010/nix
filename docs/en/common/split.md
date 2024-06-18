---
layout: page
title: common/split (English)
description: "Split a file into pieces."
content_hash: 767b9526644a3715cba81378a2fff94339069522
last_modified_at: 2024-06-18
related_topics:
  - title: Indonesia version
    url: /id/common/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Split a file into pieces.
More information: <https://www.gnu.org/software/coreutils/split>.

- Split a file, each split having 10 lines (except the last split):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file with at most 512 bytes in each split without breaking lines:

`split -C 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
