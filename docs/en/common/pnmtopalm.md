---
layout: page
title: common/pnmtopalm (English)
description: "Convert a PNM image to a Palm bitmap."
content_hash: 362e5b817a3331e8bd51efc5fe7450398daecb6a
last_modified_at: 2023-12-18
tldri18n_status: 2
---
# pnmtopalm

Convert a PNM image to a Palm bitmap.
More information: <https://netpbm.sourceforge.net/doc/pnmtopalm.html>.

- Convert a PNM image to a Palm bitmap:

`pnmtopalm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Specify the color depth of the resulting bitmap:

`pnmtopalm -depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|4|8|16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Choose a compression method for the resulting bitmap:

`pnmtopalm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scanline_compression|rle_compression|packbits_compression</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Build a custom colormap and include it in the resulting bitmap:

`pnmtopalm -colormap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Specify the bitmap's density:

`pnmtopalm -density `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72|108|144|216|288</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>
