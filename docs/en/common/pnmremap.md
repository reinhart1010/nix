---
layout: page
title: common/pnmremap (English)
description: "Replace the colors in a PNM image."
content_hash: 9a074ec4b6e7bdf7a0cc15b1520ced0054731c7b
last_modified_at: 2023-12-22
related_topics:
  - title: Nederlands version
    url: /nl/common/pnmremap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmremap

Replace the colors in a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- Replace the colors in an image with those in the specified color palette:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/palette_file.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Use Floyd-Steinberg dithering for representing colors missing in the color palette:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/palette_file.ppm</span>` -floyd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Use the first color in the palette for representing colors missing in the color palette:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/palette_file.ppm</span>` -firstisdefault `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Use the specified color for representing colors missing in the color palette:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/palette_file.ppm</span>` -missingcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
