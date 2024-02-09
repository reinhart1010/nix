---
layout: page
title: common/pbmtomacp (English)
description: "Convert a PBM image to a MacPaint file."
content_hash: c454931a9c665889ca2341c7e2c3729abca91d3a
last_modified_at: 2024-02-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtomacp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtomacp

Convert a PBM image to a MacPaint file.
See also: `macptopbm`.
More information: <https://netpbm.sourceforge.net/doc/pbmtomacp.html>.

- Convert a PBM image to a MACP file:

`pbmtomacp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.macp</span>

- Do not compress the output file:

`pbmtomacp -norle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.macp</span>
