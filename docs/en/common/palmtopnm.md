---
layout: page
title: common/palmtopnm (English)
description: "Convert a Palm bitmap file to a PNM image."
content_hash: ef594c6bb5ed9b6b735950becd0d643cd2e210b0
last_modified_at: 2023-12-17
tldri18n_status: 2
---
# palmtopnm

Convert a Palm bitmap file to a PNM image.
More information: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Convert a Palm bitmap to a PNM image:

`palmtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>

- Display information about the input file:

`palmtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>

- Convert the n'th rendition of the image contained in the input file:

`palmtopnm -rendition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>

- Write a histogram of the colors in the input file to `stdout`:

`palmtopnm -showhist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>

- Output the transparent color of the input image if set:

`palmtopnm -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>
