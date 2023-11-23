---
layout: page
title: common/pnmtotiffcmyk (English)
description: "Convert a PNM image to a CMYK encoded TIFF."
content_hash: 0b263540b21901585362f68f48262d3d60ee24b4
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtotiffcmyk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtotiffcmyk

Convert a PNM image to a CMYK encoded TIFF.
More information: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

- Convert a PNM image to a CMYK encoded TIFF:

`pnmtotiffcmyk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Specify the TIFF compression method:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>

- Control the fill order:

`pnmtotiffcmyk -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">msb2lsb|lsb2msb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.tiff</span>
