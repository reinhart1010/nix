---
layout: page
title: common/cupsreject (English)
description: "Reject jobs sent to one or more printers."
content_hash: edff9246e801436f11439e7755f61d4d0ea4b116
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsreject.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsreject

Reject jobs sent to one or more printers.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Reject print jobs to the specified destinations:

`cupsreject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a different server:

`cupsreject -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a reason string ("Reason Unknown" by default):

`cupsreject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
