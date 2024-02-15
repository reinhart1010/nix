---
layout: page
title: common/cupsenable (English)
description: "Start printers and classes."
content_hash: e3011e88ec78e1554a6f700633375c7fd4f72264
last_modified_at: 2024-02-15
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsenable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsenable

Start printers and classes.
Note: destination is referred as a printer or a class of printers.
See also: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsenable.html>.

- Start one or more destination(s):

`cupsenable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Resume printing of pending jobs of a destination (use after `cupsdisable` with `--hold`):

`cupsenable --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Cancel all jobs of the specified destination(s):

`cupsenable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
