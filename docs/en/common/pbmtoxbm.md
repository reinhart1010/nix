---
layout: page
title: common/pbmtoxbm (English)
description: "Convert a PBM image to a X11 or X10 bitmap."
content_hash: 79b42676ec331c8fec85b126927fe9499a4e6de5
last_modified_at: 2023-11-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtoxbm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtoxbm

Convert a PBM image to a X11 or X10 bitmap.
More information: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- Convert a PPM image to a X11 XBM file:

`pbmtoxbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>

- Explicitly specify whether an X11 or X10 bitmap should be generated:

`pbmtoxbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11|x10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>
