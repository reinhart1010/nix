---
layout: page
title: common/sha384sum (English)
description: "Calculate SHA384 cryptographic checksums."
content_hash: eeedb55045d80778d73b7e6f5a2e3299278270eb
last_modified_at: 2023-05-20
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

- Calculate the SHA384 checksum for one or more files:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of SHA384 checksums to a file:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>

- Calculate a SHA384 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sha384sum`

- Read a file of SHA384 sums and filenames and verify all files have matching checksums:

`sha384sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>

- Only show a message for missing files or when verification fails:

`sha384sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>

- Only show a message when verification fails, ignoring missing files:

`sha384sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha384</span>
