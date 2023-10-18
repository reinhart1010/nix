---
layout: page
title: common/bmptopnm (English)
description: "Convert a BMP file into a PBM, PGM, or PNM image."
content_hash: 35a6e8984f7b34ab193903827b873fe93e4acbb5
last_modified_at: 2023-10-18
---
# bmptopnm

Convert a BMP file into a PBM, PGM, or PNM image.
More information: <https://netpbm.sourceforge.net/doc/bmptopnm.html>.

- Generate the PBM, PGM, or PNM image as output, for Windows or OS/2 BMP file as input:

`bmptopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Report contents of the BMP header to `stderr`:

`bmptopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bmp</span>

- Display version:

`bmptopnm -version`
