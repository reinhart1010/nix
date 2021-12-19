---
layout: page
title: common/lzop (English)
description: "Compress or decompress files with LZO compression."
content_hash: e1a597324c492ce4c5be80021b708b73e6f454ac
---
# lzop

Compress or decompress files with LZO compression.
More information: <https://www.lzop.org/>.

- Compress a file into a new file with the `.lzo` suffix:

`lzop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Decompress a file:

`lzop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.lzo`

- Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):

`lzop -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
