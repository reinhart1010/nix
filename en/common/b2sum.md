---
layout: page
title: common/b2sum (English)
description: "Calculate BLAKE2 cryptographic checksums."
content_hash: 2c5fbc3af5197d30009b21b931ed7f8216bb98d6
related_topics:
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
---
# b2sum

Calculate BLAKE2 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/b2sum>.

- Calculate the BLAKE2 checksum for a file:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate BLAKE2 checksums for multiple files:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:

`b2sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b2</span>

- Calculate the BLAKE2 checksum from stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | b2sum`
