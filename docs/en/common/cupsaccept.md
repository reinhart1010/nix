---
layout: page
title: common/cupsaccept (English)
description: "Accept jobs sent to destinations."
content_hash: ed393504ccd3f97e451d658dd98a8b4b4fd93810
last_modified_at: 2024-02-05
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsaccept.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsaccept

Accept jobs sent to destinations.
Note: destination is referred as a printer or a class of printers.
See also: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Accept print jobs to the specified destinations:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Specify a different server:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
