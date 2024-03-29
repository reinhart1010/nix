---
layout: page
title: common/ppmtoxpm (English)
description: "Convert a PPM image to an X11 version 3 pixmap."
content_hash: cad80ab39377cdfd8f31591482f5a307cbe4711c
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmtoxpm

Convert a PPM image to an X11 version 3 pixmap.
More information: <https://netpbm.sourceforge.net/doc/ppmtoxpm.html>.

- Convert a PPM image to a XPM image:

`ppmtoxpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xpm</span>

- Specify the prefix string in the output XPM image:

`ppmtoxpm -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xpm</span>

- In the output XPM file, specify colors by their hexadecimal code instead of their name:

`ppmtoxpm -hexonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xpm</span>

- Use the specified PGM file as a transparency mask:

`ppmtoxpm -alphamask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/alpha_file.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xpm</span>
