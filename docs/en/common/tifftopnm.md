---
layout: page
title: common/tifftopnm (English)
description: "Convert a TIFF image to a PNM image."
content_hash: c39c0a52aba44682ed9c9eb4fc34403fdf41b635
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tifftopnm

Convert a TIFF image to a PNM image.
More information: <https://netpbm.sourceforge.net/doc/tifftopnm.html>.

- Convert a TIFF to a PNM file:

`tifftopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Create a PGM file containing the alpha channel of the input image:

`tifftopnm -alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alpha_file.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Respect the `fillorder` tag in the input TIFF image:

`tifftopnm -respectfillorder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Print TIFF header information to `stderr`:

`tifftopnm -headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>
