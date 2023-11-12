---
layout: page
title: osx/split (English)
description: "Split a file into pieces."
content_hash: 42f6c2dac5921f581e0cc228367c248246f490b9
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Split a file into pieces.
More information: <https://ss64.com/osx/split.html>.

- Split a file, each split having 10 lines (except the last split):

`split -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Split a file by a regular expression. The matching line will be the first line of the next output file:

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):

`split -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
