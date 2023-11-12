---
layout: page
title: common/sha1sum (English)
description: "Calculate SHA1 cryptographic checksums."
content_hash: b2178281d00f4a72f3a9e4d8604f92e8450991b9
last_modified_at: 2023-11-12
related_topics:
  - title: sh version
    url: /sh/common/sha1sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha1sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha1sum

Calculate SHA1 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/sha1sum>.

- Calculate the SHA1 checksum for one or more files:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of SHA1 checksums to a file:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha1</span>

- Calculate a SHA1 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sha1sum`

- Read a file of SHA1 sums and filenames and verify all files have matching checksums:

`sha1sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha1</span>

- Only show a message for missing files or when verification fails:

`sha1sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha1</span>

- Only show a message when verification fails, ignoring missing files:

`sha1sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha1</span>
