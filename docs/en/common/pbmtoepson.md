---
layout: page
title: common/pbmtoepson (English)
description: "Convert a PBM image to an Epson printer graphic."
content_hash: a4f57f90dcc31d34f81d684ed25d41d4807d13c9
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pbmtoepson

Convert a PBM image to an Epson printer graphic.
See also: `pbmtoescp2`.
More information: <https://netpbm.sourceforge.net/doc/pbmtoepson.html>.

- Convert a PBM image to an Epson printer graphic:

`pbmtoepson `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.epson</span>

- Specify the printer protocol of the output:

`pbmtoepson -protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">escp9|escp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.epson</span>

- Specify the horizontal DPI of the output:

`pbmtoepson -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60|72|80|90|120|144|240</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.epson</span>
