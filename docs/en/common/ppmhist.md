---
layout: page
title: common/ppmhist (English)
description: "Print a histogram of the colors present in a PPM image."
content_hash: b82d2dc2880b43194fed7891108a29b8b7c25030
last_modified_at: 2024-02-06
tldri18n_status: 2
---
# ppmhist

Print a histogram of the colors present in a PPM image.
See also: `pgmhist`.
More information: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- Generate the histogram for human reading:

`ppmhist -nomap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>

- Generate a PPM file of the colormap for the image, with the color histogram as comments:

`ppmhist -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>

- Display version:

`ppmhist -version`
