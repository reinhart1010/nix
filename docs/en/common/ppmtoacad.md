---
layout: page
title: common/ppmtoacad (English)
description: "Convert a PPM image to an AutoCAD database or slide."
content_hash: d03e61478d5c3df07624341ea7e4c049bc003231
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmtoacad

Convert a PPM image to an AutoCAD database or slide.
More information: <https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

- Convert a PPM image to an AutoCAD slide:

`ppmtoacad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.acad</span>

- Convert a PPM image to an AutoCAD binary database import file:

`ppmtoacad -dxb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dxb</span>

- Restrict the colors in the output to 8 RGB shades:

`ppmtoacad -8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dxb</span>
