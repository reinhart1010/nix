---
layout: page
title: common/zstd (English)
description: "Compress or decompress files with Zstandard compression."
content_hash: 47614052751e30a8acb816a314803cb0c270c53f
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/zstd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zstd

Compress or decompress files with Zstandard compression.
More information: <https://github.com/facebook/zstd>.

- Compress a file into a new file with the `.zst` suffix:

`zstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file:

`zstd --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zst</span>

- Decompress to `stdout`:

`zstd --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zst</span>

- Compress a file specifying the compression level, where 1=fastest, 19=slowest and 3=default:

`zstd -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Unlock higher compression levels (up to 22) using more memory (both for compression and decompression):

`zstd --ultra -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
