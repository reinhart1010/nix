---
layout: page
title: common/ippeveps (English)
description: "Print to Adobe PostScript printers."
content_hash: 30752631e58dcdf1b0d00ab9ffb0c9cf21495927
last_modified_at: 2023-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ippeveps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ippeveps

Print to Adobe PostScript printers.
Supports PDF, PostScript, JPEG, PWG Raster or Apple Raster files.
See also: `ippevepcl`, `ippeveprinter`.
More information: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Print a file to `stdout` (status and progress messages are sent to `stderr`):

`ippeveps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a file from `stdin` to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wget -O - https://examplewebsite.com/file</span>` | ippeveps`
