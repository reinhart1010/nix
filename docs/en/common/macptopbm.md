---
layout: page
title: common/macptopbm (English)
description: "Read a MacPaint file as input and produce a PBM image as output."
content_hash: 99864a510f9fcbf0cc6f086d4ca368b316b17cd3
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# macptopbm

Read a MacPaint file as input and produce a PBM image as output.
See also: `pbmtomacp`.
More information: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- Convert a MacPaint file into a PGM image:

`macptopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.macp</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Skip over a specified number of bytes when reading the file:

`macptopbm -extraskip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Suppress all informational messages:

`macptopbm -quiet > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Display version:

`macptopbm -version`
