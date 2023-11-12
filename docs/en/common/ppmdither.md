---
layout: page
title: common/ppmdither (English)
description: "Reduce the number of colors in an image by applying dithering."
content_hash: a5e442935d4e23b1756fa6488412e8468c3ac1ec
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ppmdither

Reduce the number of colors in an image by applying dithering.
More information: <https://netpbm.sourceforge.net/doc/ppmdither.html>.

- Read a PPM image, apply dithering and save it to a file:

`ppmdither `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Specify the desired number of shades for each primary color:

`ppmdither -red `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -green `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -blue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Specify the dimensions of the dithering matrix:

`ppmdither -dim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>
