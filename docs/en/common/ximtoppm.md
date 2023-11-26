---
layout: page
title: common/ximtoppm (English)
description: "Convert a XIM file to a PPM image."
content_hash: 4f8f9fc8e17f2be4a2467e605cfe9536fe3ab24b
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ximtoppm

Convert a XIM file to a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ximtoppm.html>.

- Convert an XIM image to a PPM image:

`ximtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xim</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Store the transparency mask of the input image in the specified file:

`ximtoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alpha_file.pbm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xim</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
