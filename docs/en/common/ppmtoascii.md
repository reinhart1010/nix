---
layout: page
title: common/ppmtoascii (English)
description: "Convert a PPM image to an ASCII image using ANSI terminal color codes."
content_hash: 5f8486498da7e29d217ce9c38bad17fca25f125b
last_modified_at: 2024-03-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoascii.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoascii

Convert a PPM image to an ASCII image using ANSI terminal color codes.
See also: `ppmtoterm`, `pbmtoascii`, `pbmto4425`.
More information: <https://netpbm.sourceforge.net/doc/ppmtoascii.html>.

- Convert a PPM image to an ASCII image, combining an area of 1x2 pixels into a character:

`ppmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>

- Convert a PPM image to an ASCII image, combining an area of 2x4 pixels into a character:

`ppmtoascii -2x4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>
