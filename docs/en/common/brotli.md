---
layout: page
title: common/brotli (English)
description: "Compress/uncompress files with Brotli compression."
content_hash: 1f3f40474c6ffe2189ece2510a39858fffd502cf
last_modified_at: 2023-04-23
---
# brotli

Compress/uncompress files with Brotli compression.
More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file, creating an uncompressed version next to the file:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.br</span>

- Compress a file specifying the output filename:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_output_file.br</span>

- Decompress a Brotli file specifying the output filename:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.br</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Specify the compression level [1=Fastest (Worst), 11=Slowest (Best)]:

`brotli -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_output_file.br</span>
