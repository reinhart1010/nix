---
layout: page
title: common/cupsaccept (English)
description: "Accept jobs sent to one or more destinations."
content_hash: 3168f7b11f8ababc60b9cba22059e8c7ec590069
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsaccept.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsaccept

Accept jobs sent to one or more destinations.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Accept print jobs to the specified destinations:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a different server:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
