---
layout: page
title: linux/lrzip (English)
description: "A large file compression program."
content_hash: 60eca92630698fce154dd43d85fff525ae5a76ca
---
# lrzip

A large file compression program.
See also `lrunzip`, `lrztar`, `lrzuntar`.
More information: <https://manned.org/lrzip>.

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Compress a file with BZIP2 - good middle ground for compression/speed:

`lrzip -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Compress with ZPAQ - extreme compression, but very slow:

`lrzip -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Compress with LZO - light compression, extremely fast decompression:

`lrzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Compress a file and password protect/encrypt it:

`lrzip -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Override the number of processor threads to use:

`lrzip -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
