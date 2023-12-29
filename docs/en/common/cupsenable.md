---
layout: page
title: common/cupsenable (English)
description: "Start printers and classes."
content_hash: 4b0b3d3dc9bb3b786cbe76f768213079eea9b626
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsenable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsenable

Start printers and classes.
NOTE: destination is referred as a printer or a class of printers.
See also: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
More information: <https://www.cups.org/doc/man-cupsenable.html>.

- Start one or more destination(s):

`cupsenable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>

- Resume printing of pending jobs of a destination (use after `cupsdisable` with `--hold`):

`cupsenable --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Cancel all jobs of the specified destination(s):

`cupsenable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
