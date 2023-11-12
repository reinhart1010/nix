---
layout: page
title: common/macptopbm (English)
description: "Read a MacPaint file as input and produce a PBM image as output."
content_hash: 80c237a63fa6e60aee410a9fa13eb14e662f2b4d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# macptopbm

Read a MacPaint file as input and produce a PBM image as output.
More information: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- Convert a MacPaint file into a PGM image:

`macptopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mac</span>

- Skip over a specified number of bytes when reading the file:

`macptopbm -extraskip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Suppress all informational messages:

`macptopbm -quiet`

- Display version:

`macptopbm -version`
