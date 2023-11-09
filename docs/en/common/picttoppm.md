---
layout: page
title: common/picttoppm (English)
description: "Convert a Macintosh PICT file to a PPM image."
content_hash: f4bd0fb433e94d96ca13ba97ced9f29ec33d531b
last_modified_at: 2023-11-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># picttoppm

Convert a Macintosh PICT file to a PPM image.
More information: <https://netpbm.sourceforge.net/doc/picttoppm.html>.

- Convert a PICT file to a PPM image:

`picttoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Force any images in the PICT file to be output at full resolution:

`picttoppm -fullres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Do not assume that the input file contains a PICT header and execute quickdraw operations only:

`picttoppm -noheader -quickdraw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>
