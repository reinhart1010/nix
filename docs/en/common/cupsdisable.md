---
layout: page
title: common/cupsdisable (English)
description: "Stop printers and classes."
content_hash: bf02f20ebcb1ead96d4823d3de1ceae040196b2f
last_modified_at: 2023-12-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsdisable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsdisable

Stop printers and classes.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`.
More information: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Stop one or more destination(s):

`cupsdisable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Cancel all jobs of the specified destination(s):

`cupsdisable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
