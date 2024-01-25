---
layout: page
title: common/cupsaccept (English)
description: "Accept jobs sent to destinations."
content_hash: 5caf121eb7c8e3160aa4af210f1d796ee8e7f744
last_modified_at: 2024-01-25
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsaccept.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsaccept

Accept jobs sent to destinations.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Accept print jobs to the specified destinations:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a different server:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
