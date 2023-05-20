---
layout: page
title: common/sha512sum (English)
description: "Calculate SHA512 cryptographic checksums."
content_hash: 85a23b9cf3bfb875f1324c9cfffc87ceb8816880
last_modified_at: 2023-05-20
related_topics:
  - title: sh version
    url: /sh/common/sha512sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha512sum.html
    icon: bi bi-globe
---
# sha512sum

Calculate SHA512 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA512 checksum for one or more files:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of SHA512 checksums to a file:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>

- Calculate a SHA512 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sha512sum`

- Read a file of SHA512 sums and filenames and verify all files have matching checksums:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>

- Only show a message for missing files or when verification fails:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>

- Only show a message when verification fails, ignoring missing files:

`sha512sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>
