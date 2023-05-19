---
layout: page
title: common/b3sum (English)
description: "Calculate BLAKE3 cryptographic checksums."
content_hash: 9127d9d1af581c42b4e11df32b1ec945545c3908
last_modified_at: 2023-05-19
---
# b3sum

Calculate BLAKE3 cryptographic checksums.
More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calculate the BLAKE3 checksum for one or more files:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of BLAKE3 checksums to a file:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Calculate a BLAKE3 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | b3sum`

- Read a file of BLAKE3 sums and filenames and verify all files have matching checksums:

`b3sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Only show a message for missing files or when verification fails:

`b3sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>
