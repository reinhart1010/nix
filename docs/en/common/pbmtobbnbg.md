---
layout: page
title: common/pbmtobbnbg (English)
description: "Convert a PBM image to a BitGraph graphic."
content_hash: 4347f9ae13202b0c5e8e48392370a83ba5005416
last_modified_at: 2024-02-12
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtobbnbg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtobbnbg

Convert a PBM image to a BitGraph graphic.
More information: <https://netpbm.sourceforge.net/doc/pbmtobbnbg.html>.

- Convert a PBM image to a BitGraph terminal Display Pixel Data sequence:

`pbmtobbnbg < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.dpd</span>

- Specify the rasterop:

`pbmtobbnbg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.dpd</span>
