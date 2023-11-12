---
layout: page
title: common/ppmhist (English)
description: "Print a histogram of the colors present in a PPM image."
content_hash: da85d1dae5ae3d98a5690e173692b3fbbd8522bb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ppmhist

Print a histogram of the colors present in a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- Generate the histogram for human reading:

`ppmhist -nomap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.ppm</span>

- Generate a PPM file of the colormap for the image, with the color histogram as comments:

`ppmhist -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.ppm</span>

- Display version:

`ppmhist -version`
