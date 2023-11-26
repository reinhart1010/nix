---
layout: page
title: common/pstopnm (English)
description: "Convert a PostScript file to a PNM image."
content_hash: b90ed6d75e2d002527dda4101679d948ecae1726
last_modified_at: 2023-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pstopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pstopnm

Convert a PostScript file to a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

- Convert a PS file to PNM images, storing page N of the input to `path/to/fileN.ppm`:

`pstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>

- Explicitly specify the output format:

`pstopnm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pbm|pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>

- Specify the resolution of the output in dots per inch:

`pstopnm -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps</span>
