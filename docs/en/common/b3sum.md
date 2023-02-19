---
layout: page
title: common/b3sum (English)
description: "Command line utility for calculating BLAKE3 hashes."
content_hash: d46d3975a70d8d2ac0e0753ff339def4079fe828
last_modified_at: 2023-02-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># b3sum

Command line utility for calculating BLAKE3 hashes.
It is similar to Coreutils tools like b2sum or md5sum.
More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calculate the BLAKE3 checksum for a file:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate BLAKE3 checksums for multiple files:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate the BLAKE3 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | b3sum`

- Create a file of BLAKE3 checksums:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Read and verify a file of BLAKE3 checksums:

`b3sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>
