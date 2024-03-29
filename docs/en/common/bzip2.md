---
layout: page
title: common/bzip2 (English)
description: "A block-sorting file compressor."
content_hash: e7500d2c45a1323fc58b5d2a46cc1162976273d3
last_modified_at: 2024-02-19
related_topics:
  - title: italiano version
    url: /it/common/bzip2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bzip2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bzip2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzip2

A block-sorting file compressor.
More information: <https://manned.org/bzip2>.

- Compress a file:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_to_compress</span>

- [d]ecompress a file:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- [d]ecompress a file to `stdout`:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Test the integrity of each file inside the archive file:

`bzip2 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Show the compression ratio for each file processed with detailed information:

`bzip2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_files.bz2</span>

- Decompress a file overwriting existing files:

`bzip2 --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Display help:

`bzip2 -h`
