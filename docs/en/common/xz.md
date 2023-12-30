---
layout: page
title: common/xz (English)
description: "Compress or decompress `.xz` and `.lzma` files."
content_hash: 32bafe3bbdd297e0becf202007fd974598effac7
last_modified_at: 2023-12-30
related_topics:
  - title: Nederlands version
    url: /nl/common/xz.html
    icon: bi bi-globe
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

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress an lzma file:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.lzma</span>

- Decompress a file and write to `stdout` (implies `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xz</span>

- Compress a file, but don't delete the original:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the fastest compression:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the best compression:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
