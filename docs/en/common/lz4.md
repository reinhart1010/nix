---
layout: page
title: common/lz4 (English)
description: "Compress or decompress .lz4 files."
content_hash: 58d816fa8857cf758ccf4a97b118a34edf0c7b5b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lz4

Compress or decompress .lz4 files.
More information: <https://github.com/lz4/lz4>.

- Compress a file:

`lz4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file:

`lz4 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.lz4</span>

- Decompress a file and write to `stdout`:

`lz4 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.lz4</span>

- Package and compress a directory and its contents:

`tar cvf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | lz4 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir.tar.lz4</span>

- Decompress and unpack a directory and its contents:

`lz4 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir.tar.lz4</span>` | tar -xv`

- Compress a file using the best compression:

`lz4 -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
