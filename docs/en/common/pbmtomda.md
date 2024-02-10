---
layout: page
title: common/pbmtomda (English)
description: "Convert a PBM image to a Microdesign MDA file."
content_hash: be62754ae340678a3603c4d0369d096798c19221
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# pbmtomda

Convert a PBM image to a Microdesign MDA file.
See also: `mdatopbm`.
More information: <https://netpbm.sourceforge.net/doc/pbmtomda.html>.

- Convert a PBM image to a MDA file:

`pbmtomda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.mda</span>

- Invert the colors in the input image:

`pbmtomda -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.mda</span>

- Halve the input image's height:

`pbmtomda -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.mda</span>
