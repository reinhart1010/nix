---
layout: page
title: common/ppmtoppm (English)
description: "Copy a PPM image."
content_hash: 35bf316d56a26cbf483aab83879c643a3ae848e4
last_modified_at: 2023-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoppm

Copy a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmtoppm.html>.

- Copy a PPM image (i.e. a PBM, PGM or PPM image) from `stdin` to `stdout`:

`ppmtoppm < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Display version:

`ppmtoppm -version`
