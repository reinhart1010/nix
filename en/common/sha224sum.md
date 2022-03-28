---
layout: page
title: common/sha224sum (English)
description: "Calculate SHA224 cryptographic checksums."
content_hash: a8af5df25e0a490962daec2ebfb8c99d9ba0c1bd
related_topics:
  - title: sh version
    url: /sh/common/sha224sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha224sum.html
    icon: bi bi-globe
---
# sha224sum

Calculate SHA224 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA224 checksum for a file:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate SHA224 checksums for multiple files:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate and save the list of SHA224 checksums to a file:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha224</span>

- Read a file of SHA224 sums and verify all files have matching checksums:

`sha224sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha224</span>

- Only show a message for missing files or when verification fails:

`sha224sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha224</span>

- Only show a message for files for which verification fails, ignoring missing files:

`sha224sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha224</span>
