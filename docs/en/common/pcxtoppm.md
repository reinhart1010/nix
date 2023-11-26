---
layout: page
title: common/pcxtoppm (English)
description: "Convert a PCX file to a PPM image."
content_hash: 4fe7095995cc165eb9ffe3b31ea0b9d22e63a476
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pcxtoppm

Convert a PCX file to a PPM image.
More information: <https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

- Convert a PCX file to a PPM image:

`pcxtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Use a predefined standard palette even if the PCX file provides one:

`pcxtoppm -stdpalette `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>

- Print information on the PCX header to `stdout`:

`pcxtoppm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>
