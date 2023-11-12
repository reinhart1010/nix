---
layout: page
title: common/xz (English)
description: "Compress or decompress `.xz` and `.lzma` files."
content_hash: 7b3ca82995dcb607e36c652d72dc3a940362bd3e
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/xz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xz

Compress or decompress `.xz` and `.lzma` files.
More information: <https://manned.org/xz>.

- Compress a file using xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress an xz file:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xz</span>

- Compress a file using lzma:

`xz --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress an lzma file:

`xz --decompress --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.lzma</span>

- Decompress a file and write to `stdout` (implies `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xz</span>

- Compress a file, but don't delete the original:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the fastest compression:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the best compression:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
