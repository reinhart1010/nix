---
layout: page
title: common/asciitopgm (English)
description: "Convert ASCII graphics into a PGM file."
content_hash: 9ffcd75ddb7c971a5e6fbd0661551eb9ba82e64d
last_modified_at: 2023-10-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># asciitopgm

Convert ASCII graphics into a PGM file.
More information: <https://netpbm.sourceforge.net/doc/asciitopgm.html>.

- Read ASCII data as input and produce a PGM image with pixel values that are an approximation of the "brightness" of the ASCII characters:

`asciitopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pgm</span>

- Display version:

`asciitopgm -version`
