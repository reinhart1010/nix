---
layout: page
title: common/zlib-flate (English)
description: "Raw zlib compression and decompression program."
content_hash: 1452dd1ab65f7659952ada2f828c8a74434771ac
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zlib-flate

Raw zlib compression and decompression program.
Part of `qpdf`.
More information: <https://manned.org/zlib-flate>.

- Compress a file:

`zlib-flate -compress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zlib</span>

- Uncompress a file:

`zlib-flate -uncompress < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zlib</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Compress a file with a specified compression level. 0=Fastest (Worst), 9=Slowest (Best):

`zlib-flate -compress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compression_level</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zlib</span>
