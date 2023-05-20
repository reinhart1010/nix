---
layout: page
title: common/shasum (English)
description: "Calculate SHA cryptographic checksums."
content_hash: b510e09dc099ad4736e92f27bd9cbcd6ef9c97f3
last_modified_at: 2023-05-20
related_topics:
  - title: தமிழ் version
    url: /ta/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
---
# shasum

Calculate SHA cryptographic checksums.
More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for one or more files:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate the SHA256 checksum for one or more files:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate the SHA512 checksum for one or more files:

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate a SHA1 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | shasum`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Read a file of SHA1 sums and filenames and verify all files have matching checksums:

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only show a message for missing files or when verification fails:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only show a message when verification fails, ignoring missing files:

`shasum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
