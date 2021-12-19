---
layout: page
title: common/sha512sum (English)
description: "Calculate SHA512 cryptographic checksums."
content_hash: f0cb8ee434d0cfd9dda99599560ddf8c560bc2ff
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

- Calculate the SHA512 checksum for a file:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate SHA512 checksums for multiple files:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate and save the list of SHA512 checksums to a file:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>

- Read a file of SHA512 sums and verify all files have matching checksums:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>

- Only show a message for files for which verification fails:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha512</span>
