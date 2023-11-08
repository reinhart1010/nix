---
layout: page
title: common/pnmtotiffcmyk (English)
description: "Convert a PNM image to a CMYK encoded TIFF."
content_hash: 0b263540b21901585362f68f48262d3d60ee24b4
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pnmtotiffcmyk

Convert a PNM image to a CMYK encoded TIFF.
More information: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

- Convert a PNM image to a CMYK encoded TIFF:

`pnmtotiffcmyk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Specify the TIFF compression method:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Control the fill order:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">msb2lsb|lsb2msb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>
