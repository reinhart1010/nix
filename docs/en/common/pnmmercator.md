---
layout: page
title: common/pnmmercator (English)
description: "Perform Mercator transformations on Netpbm images."
content_hash: 00412600a64cbf52eeb8f13ed729c65d90b93f1a
last_modified_at: 2024-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmmercator.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmmercator

Perform Mercator transformations on Netpbm images.
See also: `pnmglobe`.
More information: <https://netpbm.sourceforge.net/doc/pnmmercator.html>.

- Convert a rectangular projection worldmap to Mercator projection:

`pnmmercator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Convert a Mercator projection worldmap to rectangular projection:

`pnmmercator -inverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
