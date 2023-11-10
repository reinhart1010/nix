---
layout: page
title: common/ppmtobmp (English)
description: "Convert a PPM image to a BMP file."
content_hash: 78d454100a5dff6145b0f4cfcc576259767a23b2
last_modified_at: 2023-11-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmtobmp

Convert a PPM image to a BMP file.
More information: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- Convert a PPM image to a BMP file:

`ppmtobmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Explicitly specify whether or not a Windows BMP file or an OS/2 BMP file should be created:

`ppmtobmp -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|os2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Specify the number of bits to use for each pixel:

`ppmtobmp -bbp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|4|8|24</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>
