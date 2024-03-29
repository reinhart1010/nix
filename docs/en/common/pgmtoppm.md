---
layout: page
title: common/pgmtoppm (English)
description: "Colorize a PGM image."
content_hash: a49e8199facc435b8403db3c9575757d748052a6
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pgmtoppm

Colorize a PGM image.
More information: <https://netpbm.sourceforge.net/doc/pgmtoppm.html>.

- Map all greyscale values of the input image to all colors between the two specified colors:

`pgmtoppm -black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` --white `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Map all greyscale values of the input image to colors according to the specified colormap:

`pgmtoppm -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/colormap.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
