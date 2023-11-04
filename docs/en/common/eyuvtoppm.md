---
layout: page
title: common/eyuvtoppm (English)
description: "Convert a Berkeley YUV file to PPM."
content_hash: 24623236176d7e3eaf0391bf6cd6b09a567d3c68
last_modified_at: 2023-11-04
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># eyuvtoppm

Convert a Berkeley YUV file to PPM.
More information: <https://netpbm.sourceforge.net/doc/eyuvtoppm.html>.

- Read a Berkeley YUV file from the specified input file, convert it to a PPM image and store it in the specified output file:

`eyuvtoppm --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.eyuv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
