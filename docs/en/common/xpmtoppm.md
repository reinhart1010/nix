---
layout: page
title: common/xpmtoppm (English)
description: "Convert an X11 pixmap to a PPM image."
content_hash: 61fbb8fdd38982c8b04d16395dc151ef38fe85b0
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# xpmtoppm

Convert an X11 pixmap to a PPM image.
More information: <https://netpbm.sourceforge.net/doc/xpmtoppm.html>.

- Convert an XPM image to a PPM image:

`xpmtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xpm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Store the transparency mask of the input image in the specified file:

`xpmtoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alpha_file.pbm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xpm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
