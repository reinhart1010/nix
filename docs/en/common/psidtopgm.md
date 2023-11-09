---
layout: page
title: common/psidtopgm (English)
description: "Convert PostScript image data to a PGM image."
content_hash: 594a1758e7339afa82d9a8ba5bc67672487064f4
last_modified_at: 2023-11-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># psidtopgm

Convert PostScript image data to a PGM image.
More information: <https://netpbm.sourceforge.net/doc/psidtopgm.html>.

- Convert the image data in a PS file to a PGM image of the specified dimensions and quality:

`psidtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bits_per_sample</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>
