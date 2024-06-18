---
layout: page
title: osx/split (English)
description: "Split a file into pieces."
content_hash: 74ff84ab32ca592d5ddc4636c47fce5e5d63bd11
last_modified_at: 2024-06-18
related_topics:
  - title: español version
    url: /es/osx/split.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Split a file into pieces.
More information: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Split a file, each split having 10 lines (except the last split):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file by a regular expression. The matching line will be the first line of the next output file:

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
