---
layout: page
title: common/pnmsmooth (English)
description: "Smooth out a PNM image."
content_hash: f5117fb5a344ad26b62699a9b518571a861edcc7
last_modified_at: 2023-12-16
tldri18n_status: 2
---
# pnmsmooth

Smooth out a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmsmooth.html>.

- Smooth out a PNM image using a convolution matrix of size 3x3:

`pnmsmooth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Smooth out a PNM image using a convolution matrix of size width times height:

`pnmsmooth -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
