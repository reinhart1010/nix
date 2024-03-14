---
layout: page
title: common/xz (English)
description: "Compress or decompress XZ and LZMA files."
content_hash: c84582043401de1c001e9370f44ad973a4be59d0
last_modified_at: 2024-03-14
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

Compress or decompress XZ and LZMA files.
More information: <https://manned.org/xz>.

- Compress a file using xz:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress an XZ file:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xz</span>

- Compress a file using lzma:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress an LZMA file:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.lzma</span>

- Decompress a file and write to `stdout` (implies `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xz</span>

- Compress a file, but don't delete the original:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the fastest compression:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file using the best compression:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
