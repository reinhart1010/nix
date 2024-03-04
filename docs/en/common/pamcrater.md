---
layout: page
title: common/pamcrater (English)
description: "Create a PAM image of cratered terrain."
content_hash: eb4258f97ef1e3c73371e260e7856e32170825aa
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamcrater.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamcrater

Create a PAM image of cratered terrain.
See also: `pamshadedrelief`, `ppmrelief`.
More information: <https://netpbm.sourceforge.net/doc/pamcrater.html>.

- Create an image of cratered terrain with the specified dimensions:

`pamcrater -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Create an image containing the specified number of craters:

`pamcrater -number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_craters</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
