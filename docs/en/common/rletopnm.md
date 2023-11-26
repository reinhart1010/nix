---
layout: page
title: common/rletopnm (English)
description: "Convert a Utah Raster Tools RLE image file to a PNM file."
content_hash: 38ec0df6dc6b80fa3ea11814b7278ce418245c4b
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# rletopnm

Convert a Utah Raster Tools RLE image file to a PNM file.
More information: <https://netpbm.sourceforge.net/doc/rletopnm.html>.

- Convert an RLE image to a PNM file:

`rletopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Create a PGM image containing the RLE file's alpha channel:

`rletopnm -alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alpha_file.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Operate in verbose mode and print the contents of the RLE header to `stdout`:

`rletopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
