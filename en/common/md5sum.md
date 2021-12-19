---
layout: page
title: common/md5sum (English)
description: "Calculate MD5 cryptographic checksums."
content_hash: fcba79ab4c5be6ea41258016ee82f5b3be043e13
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
---
# md5sum

Calculate MD5 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/md5sum>.

- Calculate the MD5 checksum for a file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate MD5 checksums for multiple files:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filen2</span>

- Read a file of MD5SUMs and verify all files have matching checksums:

`md5sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md5</span>

- Calculate a MD5 checksum from the standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`" | md5sum`
