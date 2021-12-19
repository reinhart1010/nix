---
layout: page
title: common/sha256sum (English)
description: "Calculate SHA256 cryptographic checksums."
content_hash: 4a835f1e9df41904e68a9c07057dec405e628ac6
related_topics:
  - title: sh version
    url: /sh/common/sha256sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha256sum.html
    icon: bi bi-globe
---
# sha256sum

Calculate SHA256 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA256 checksum for a file:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate SHA256 checksums for multiple files:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate and save the list of SHA256 checksums to a file:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Read a file of SHA256 sums and verify all files have matching checksums:

`sha256sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Only show a message for files for which verification fails:

`sha256sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>
