---
layout: page
title: common/sldtoppm (English)
description: "Convert an AutoCAD slide file to a PPM image."
content_hash: a3a2377be71236593022954c25f50343d7f12ca6
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# sldtoppm

Convert an AutoCAD slide file to a PPM image.
More information: <https://netpbm.sourceforge.net/doc/sldtoppm.html>.

- Convert an SLD file to a PPM image:

`sldtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.sld</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Compensate for non-square pixels by scaling the width of the image:

`sldtoppm -adjust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.sld</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
