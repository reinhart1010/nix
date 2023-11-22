---
layout: page
title: common/gemtopnm (English)
description: "Convert a GEM image file into a PNM image."
content_hash: daa2ed6432ac30310ac89a2098e7efbaf735116e
last_modified_at: 2023-11-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gemtopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gemtopbm

Convert a GEM image file into a PNM image.
More information: <https://netpbm.sourceforge.net/doc/gemtopnm.html>.

- Convert a GEM image file to a PNM image:

`gemtopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Describe the contents of the specified GEM image:

`gemtopbm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>

- Display version:

`gemtopbm -version`
