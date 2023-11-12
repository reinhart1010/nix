---
layout: page
title: common/md5sum (English)
description: "Calculate MD5 cryptographic checksums."
content_hash: 1d41328293318f5803db4ccb98781639afb8fd5f
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# md5sum

Calculate MD5 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/md5sum>.

- Calculate the MD5 checksum for one or more files:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of MD5 checksums to a file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>

- Calculate an MD5 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | md5sum`

- Read a file of MD5 sums and filenames and verify all files have matching checksums:

`md5sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>

- Only show a message for missing files or when verification fails:

`md5sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>

- Only show a message when verification fails, ignoring missing files:

`md5sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>
