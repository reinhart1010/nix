---
layout: page
title: linux/lrzip (English)
description: "A large file compression program."
content_hash: c9edeb0cf81540770f6e0294cc821097cadc2de6
last_modified_at: 2023-12-27
tldri18n_status: 2
---
# lrzip

A large file compression program.
See also: `lrunzip`, `lrztar`, `lrzuntar`.
More information: <https://manned.org/lrzip>.

- Compress a file with LZMA - slow compression, fast decompression:

`lrzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file with BZIP2 - good middle ground for compression/speed:

`lrzip -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress with ZPAQ - extreme compression, but very slow:

`lrzip -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress with LZO - light compression, extremely fast decompression:

`lrzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compress a file and password protect/encrypt it:

`lrzip -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Override the number of processor threads to use:

`lrzip -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
