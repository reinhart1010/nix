---
layout: page
title: common/cupsdisable (English)
description: "Stop printers and classes."
content_hash: bf02f20ebcb1ead96d4823d3de1ceae040196b2f
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsdisable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsdisable

Stop printers and classes.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`.
More information: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Stop one or more destination(s):

`cupsdisable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Cancel all jobs of the specified destination(s):

`cupsdisable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
