---
layout: page
title: common/ppmtorgb3 (English)
description: "Separate the color components of a PPM file into three separate PGM files."
content_hash: fe1ab3a7d563c335cb3d7d817088bae6d7b49ec4
last_modified_at: 2024-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtorgb3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtorgb3

Separate the color components of a PPM file into three separate PGM files.
See also: `rgb3toppm`.
More information: <https://netpbm.sourceforge.net/doc/ppmtorgb3.html>.

- Separate the color components of a PPM file, saving the outputs to `file.red`, `file.grn` and `file.blu`:

`ppmtorgb3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>
