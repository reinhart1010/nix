---
layout: page
title: common/bzip3 (English)
description: "An efficient statistical file compressor."
content_hash: 64e498df5ad49dfae5816ea89b253832d43a712f
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# bzip3

An efficient statistical file compressor.
More information: <https://github.com/kspalaiologos/bzip3>.

- Compress a file:

`bzip3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_to_compress</span>

- [d]ecompress a file:

`bzip3 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz3</span>

- Decompress a file to `stdout` ([c]):

`bzip3 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz3</span>

- Test the integrity of each file inside the archive file:

`bzip3 --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz3</span>

- Show the compression ratio for each file processed with detailed information:

`bzip3 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_files.bz3</span>

- Decompress a file overwriting existing files:

`bzip3 -d --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.bz3</span>

- Display help:

`bzip3 -h`
