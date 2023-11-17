---
layout: page
title: common/pnmtorast (English)
description: "Convert a PNM file to a Sun rasterfile."
content_hash: 10660248467695eba1886401aeae4ae398e4b407
last_modified_at: 2023-11-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmtorast.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmtorast

Convert a PNM file to a Sun rasterfile.
More information: <https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- Convert a PNM image to a RAST image:

`pnmtorast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rast</span>

- Force either `RT_STANDARD` or `RT_BYTE_ENCODED` form for the output:

`pnmtorast -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.rast</span>
