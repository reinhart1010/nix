---
layout: page
title: common/ppmtospu (English)
description: "Convert a PPM file to an Atari Spectrum 512 image."
content_hash: b3d9611e9a906c368c99eb72483393c70e0e7dba
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmtospu

Convert a PPM file to an Atari Spectrum 512 image.
More information: <https://netpbm.sourceforge.net/doc/ppmtospu.html>.

- Convert a PPM file to an Atari Spectrum 512 image:

`ppmtospu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.spu</span>

- Use a dithering matrix of the specified size (0 means no dithering):

`ppmtospu -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|2|4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.spu</span>
