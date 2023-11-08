---
layout: page
title: common/pamtotiff (English)
description: "Convert a PAM image to a TIFF file."
content_hash: f3555a4be320f12d9ddcc4b59507c3e654b5abc7
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pamtotiff

Convert a PAM image to a TIFF file.
More information: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- Convert a PAM image to a TIFF image:

`pamtotiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Explicitly specify a compression method for the output file:

`pamtotiff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw|g3|g4|flate|adobeflate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Always produce a color TIFF image, even if the input image is greyscale:

`pamtotiff -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>
