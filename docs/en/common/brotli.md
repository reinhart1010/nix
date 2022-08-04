---
layout: page
title: common/brotli (English)
description: "Compress/uncompress files with Brotli compression."
content_hash: 69911ef33f79fd7e2cc770b685ae94f7fc5f0fc1
---
# brotli

Compress/uncompress files with Brotli compression.
More information: <https://github.com/google/brotli>.

- Compress a file, creating a compressed version next to the file:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Decompress a file, creating an uncompressed version next to the file:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>`.br`

- Compress a file specifying the output filename:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file.ext.br</span>

- Decompress a Brotli file specifying the output filename:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file.ext.br</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Specify the compression level. 1=Fastest (Worst), 11=Slowest (Best):

`brotli -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed_file.ext.br</span>
