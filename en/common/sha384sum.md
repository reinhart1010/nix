---
layout: page
title: common/sha384sum (English)
description: "Calculate SHA384 cryptographic checksums."
content_hash: 25b23ce04605fe5817e56bc0de1ebd7c1de44c38
related_topics:
  - title: sh version
    url: /sh/common/sha384sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha384sum.html
    icon: bi bi-globe
---
# sha384sum

Calculate SHA384 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA384 checksum for a file:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate SHA384 checksums for multiple files:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate and save the list of SHA384 checksums to a file:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>

- Read a file of SHA384 sums and verify all files have matching checksums:

`sha384sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>

- Only show a message for files for which verification fails:

`sha384sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>
