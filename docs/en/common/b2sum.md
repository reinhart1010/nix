---
layout: page
title: common/b2sum (English)
description: "Calculate BLAKE2 cryptographic checksums."
content_hash: 812aa844768ebb5ea24742ae0c11d264b2758a8a
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b2sum

Calculate BLAKE2 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/b2sum>.

- Calculate the BLAKE2 checksum for one or more files:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of BLAKE2 checksums to a file:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b2</span>

- Calculate a BLAKE2 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | b2sum`

- Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b2</span>

- Only show a message for missing files or when verification fails:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b2</span>

- Only show a message when verification fails, ignoring missing files:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b2</span>
