---
layout: page
title: common/pnmtoddif (English)
description: "Convert a PNM image to a DDIF image file."
content_hash: 84cc60ab73cd02b690133c29fb50167fbfc9b083
last_modified_at: 2023-12-16
tldri18n_status: 2
---
# pnmtoddif

Convert a PNM image to a DDIF image file.
More information: <https://netpbm.sourceforge.net/doc/pnmtoddif.html>.

- Convert a PNM image to a DDIF image file:

`pnmtoddif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ddif</span>

- Explicitly specify the horizontal and vertical resolution of the output image:

`pnmtoddif -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horizontal_dpi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vertical_dpi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ddif</span>
