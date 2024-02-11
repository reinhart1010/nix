---
layout: page
title: common/pbmtopgm (English)
description: "Convert a PBM image to PGM by averaging areas surrounding individual pixels."
content_hash: 700f181098fea7ffd7fc7c4d5fea9d70808b68bc
last_modified_at: 2024-02-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtopgm

Convert a PBM image to PGM by averaging areas surrounding individual pixels.
See also: `pnmconvol`, `pamditherbw`.
More information: <https://netpbm.sourceforge.net/doc/pbmtopgm.html>.

- Convert PBM image to PGM by averaging the `w`x`h`-sized area surrounding each pixel:

`pbmtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">w</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
