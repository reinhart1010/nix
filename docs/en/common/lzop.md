---
layout: page
title: common/lzop (English)
description: "Compress or decompress files with LZO compression."
content_hash: cd8c25585e968f6efecde7969b90d18f38c90811
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# lzop

Compress or decompress files with LZO compression.
More information: <https://www.lzop.org/>.

- Compress a file into a new file with the `.lzo` suffix:

`lzop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file:

`lzop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.lzo</span>

- Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):

`lzop -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
