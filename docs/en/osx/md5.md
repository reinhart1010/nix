---
layout: page
title: osx/md5 (English)
description: "Calculate MD5 cryptographic checksums."
content_hash: 9a8e5221d5a4093712cce7097acdb3199cabe956
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/md5.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/md5.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/md5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# md5

Calculate MD5 cryptographic checksums.
More information: <https://keith.github.io/xcode-man-pages/md5.1.html>.

- Calculate the MD5 checksum for a file:

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate MD5 checksums for multiple files:

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Output only the md5 checksum (no filename):

`md5 -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a checksum of the given string:

`md5 -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`
