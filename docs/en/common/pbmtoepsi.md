---
layout: page
title: common/pbmtoepsi (English)
description: "Convert a PBM image to an encapsulated PostScript style preview bitmap."
content_hash: 893e79b35b696a20223f1af3770f4e79b4be7075
last_modified_at: 2024-11-02
tldri18n_status: 2
---
# pbmtoepsi

Convert a PBM image to an encapsulated PostScript style preview bitmap.
More information: <https://netpbm.sourceforge.net/doc/pbmtoepsi.html>.

- Convert a PBM image to an encapsulated PostScript style preview bitmap:

`pbmtoepsi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.bmp</span>

- Produce a quadratic output image with the specified resolution:

`pbmtoepsi -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">144</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.bmp</span>

- Produce an output image with the specified horizontal and vertical resolution:

`pbmtoepsi -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72x144</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.bmp</span>

- Only create a boundary box:

`pbmtoepsi -bbonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.bmp</span>
