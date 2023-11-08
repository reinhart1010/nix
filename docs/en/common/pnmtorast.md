---
layout: page
title: common/pnmtorast (English)
description: "Convert a PNM file to a Sun rasterfile."
content_hash: 10660248467695eba1886401aeae4ae398e4b407
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pnmtorast

Convert a PNM file to a Sun rasterfile.
More information: <https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- Convert a PNM image to a RAST image:

`pnmtorast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rast</span>

- Force either `RT_STANDARD` or `RT_BYTE_ENCODED` form for the output:

`pnmtorast -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rast</span>
