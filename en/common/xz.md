---
layout: page
title: common/xz (English)
description: "Compress or decompress .xz and .lzma files."
content_hash: 8e2f5734c8d3e13e254def8a9fbacce616dd823f
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/xz.html
    icon: bi bi-globe
---
# xz

Compress or decompress .xz and .lzma files.
More information: <https://tukaani.org/xz/format.html>.

- Compress a file to the xz file format:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Decompress a xz file:

`xz -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xz</span>

- Compress a file to the LZMA file format:

`xz --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Decompress an LZMA file:

`xz -d --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.lzma</span>

- Decompress a file and write to stdout:

`xz -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xz</span>

- Compress a file, but don't delete the original:

`xz -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Compress a file using the fastest compression:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Compress a file using the best compression:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
