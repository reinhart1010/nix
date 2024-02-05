---
layout: page
title: common/cupsreject (English)
description: "Reject jobs sent to printers."
content_hash: 88d60b863936ceb79c8a8792d8874865119279b4
last_modified_at: 2024-02-05
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsreject.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsreject

Reject jobs sent to printers.
Note: destination is referred as a printer or a class of printers.
See also: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Reject print jobs to the specified destinations:

`cupsreject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a different server:

`cupsreject -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a reason string ("Reason Unknown" by default):

`cupsreject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
