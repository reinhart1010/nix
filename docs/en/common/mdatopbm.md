---
layout: page
title: common/mdatopbm (English)
description: "Convert a Microdesign MDA file to a PBM image."
content_hash: 850ff22d76564a717541e198a89c846a20ec9550
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# mdatopbm

Convert a Microdesign MDA file to a PBM image.
See also: `pbmtomda`.
More information: <https://netpbm.sourceforge.net/doc/mdatopbm.html>.

- Convert a MDA file to a PBM image:

`mdatopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Invert the colors in the input image:

`mdatopbm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Double the input image's height:

`mdatopbm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.mda</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
