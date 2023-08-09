---
layout: page
title: common/bzip2 (English)
description: "A block-sorting file compressor."
content_hash: 3bca63a9d5c541b008c532de79b4353ad1aac2a7
last_modified_at: 2023-08-09
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
---
# bzip2

A block-sorting file compressor.
More information: <https://manned.org/bzip2>.

- Compress a file:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_to_compress</span>

- Decompress a file:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Decompress a file to `stdout`:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Test the integrity of each file inside the archive file:

`bzip2 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Show the compression ratio for each file processed with detailed information:

`bzip2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_files.bz2</span>

- Decompress a file overwriting existing files:

`bzip2 --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz2</span>

- Display help:

`bzip2 -h`
