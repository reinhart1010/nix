---
layout: page
title: common/brotli (English)
description: "Compress/uncompress files with Brotli compression."
content_hash: e2afdf9713b6ce380133e8178e1592f8100ee5be
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# brotli

Compress/uncompress files with Brotli compression.
More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [d]ecompress a file, creating an uncompressed version next to the file:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.br</span>

- Compress a file specifying the [o]utput filename:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_output_file.br</span>

- [d]ecompress a Brotli file specifying the [o]utput filename:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_file.br</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Specify the compression quality (1=fastest (worst), 11=slowest (best)):

`brotli -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed_output_file.br</span>
