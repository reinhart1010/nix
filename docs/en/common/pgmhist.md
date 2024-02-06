---
layout: page
title: common/pgmhist (English)
description: "Print a histogram of the values present in a PGM image."
content_hash: 4f4c0fb40bd5cb05493ee00724fe0ab58dcdcb59
last_modified_at: 2024-02-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pgmhist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pgmhist

Print a histogram of the values present in a PGM image.
See also: `ppmhist`.
More information: <https://netpbm.sourceforge.net/doc/pgmhist.html>.

- Display the histogram for human reading:

`pgmhist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>

- Display the median grey value:

`pgmhist -median `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>

- Display four quartile grey value:

`pgmhist -quartile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>

- Report the existence of invalid grey values:

`pgmhist -forensic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>

- Display machine-readable output:

`pgmhist -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>
