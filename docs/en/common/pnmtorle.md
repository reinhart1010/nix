---
layout: page
title: common/pnmtorle (English)
description: "Convert a PNM file to an Utah Raster Tools RLE image file."
content_hash: 5ef5e4fdfbe20c5dd708aa07ca43db23bf22343f
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pnmtorle

Convert a PNM file to an Utah Raster Tools RLE image file.
More information: <https://netpbm.sourceforge.net/doc/pnmtorle.html>.

- Convert a PNM image to an RLE image:

`pnmtorle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rle</span>

- Print PNM header information to `stdout`:

`pnmtorle -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rle</span>

- Include a transparency channel in the output image in which every black pixel is set to fully transparent and every other pixel is set to fully opaque:

`pnmtorle -alpha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rle</span>
