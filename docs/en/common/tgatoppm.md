---
layout: page
title: common/tgatoppm (English)
description: "Convert a TrueVision Targa file to a Netpbm image."
content_hash: b95db6462ec98c2770dc8e8a68eddb9f50a44c9c
last_modified_at: 2023-11-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tgatoppm

Convert a TrueVision Targa file to a Netpbm image.
More information: <https://netpbm.sourceforge.net/doc/tgatoppm.html>.

- Convert a TrueVision Targa file to a PPM image:

`tgatoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Dump information from the TGA header to `stdout`:

`tgatoppm --headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Write the transparency channel values of the input image to the specified file:

`tgatoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/transparency_file.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Display version:

`tgatoppm -version`
