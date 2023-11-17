---
layout: page
title: common/ppmtoacad (English)
description: "Convert a PPM image to an AutoCAD database or slide."
content_hash: d03e61478d5c3df07624341ea7e4c049bc003231
last_modified_at: 2023-11-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoacad.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoacad

Convert a PPM image to an AutoCAD database or slide.
More information: <https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

- Convert a PPM image to an AutoCAD slide:

`ppmtoacad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.acad</span>

- Convert a PPM image to an AutoCAD binary database import file:

`ppmtoacad -dxb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dxb</span>

- Restrict the colors in the output to 8 RGB shades:

`ppmtoacad -8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dxb</span>
