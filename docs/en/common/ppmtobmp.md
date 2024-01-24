---
layout: page
title: common/ppmtobmp (English)
description: "Convert a PPM image to a BMP file."
content_hash: f116392454e37c3870b1b9d29f83380d9bfc1e33
last_modified_at: 2024-01-24
tldri18n_status: 2
---
# ppmtobmp

Convert a PPM image to a BMP file.
More information: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- Convert a PPM image to a BMP file:

`ppmtobmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Explicitly specify whether or not a Windows BMP file or an OS/2 BMP file should be created:

`ppmtobmp -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|os2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Use a specific number of bits for each pixel:

`ppmtobmp -bbp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|4|8|24</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>
