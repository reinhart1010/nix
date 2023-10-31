---
layout: page
title: common/pbmtogem (English)
description: "Read a PBM image as input and produce a compressed GEM .img file as output."
content_hash: bc626fb90a448694f1afbbf76fee79e0c02163bd
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pbmtogem

Read a PBM image as input and produce a compressed GEM .img file as output.
`pbmtogem` cannot compress repeated lines.
More information: <https://netpbm.sourceforge.net/doc/pbmtogem.html>.

- Convert a PBM image into a GEM .img file:

`pbmtogem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>

- Suppress all informational messages:

`pbmtogem -quiet`

- Display version:

`pbmtogem -version`
