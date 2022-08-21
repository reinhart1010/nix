---
layout: page
title: common/unzstd (English)
description: "Decompress files with Zstandard compression."
content_hash: 5c958eaa579b856a3a4671166918cc1f1caf4596
---
# unzstd

Decompress files with Zstandard compression.
More information: <https://github.com/facebook/zstd>.

- Decompress files:

`unzstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.ztd path/to/file2.ztd ...</span>

- Decompress a file into a specific output file:

`unzstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.ztd</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/extracted_file</span>

- Display information about a compressed file:

`unzip --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zst</span>
