---
layout: page
title: linux/byzanz-record (English)
description: "Record the screen."
content_hash: 5dd2fd1786c1c2021d1b71d80e5acdfac56cbd4f
last_modified_at: 2023-12-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/byzanz-record.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># byzanz-record

Record the screen.
More information: <https://manned.org/byzanz-record>.

- Record the screen and write the recording to a file (by default, `byzanz-record` will only record for 10 seconds):

`byzanz-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.[byzanz|flv|gif|ogg|ogv|webm]</span>

- Show information while and after recording:

`byzanz-record --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.[byzanz|flv|gif|ogg|ogv|webm]</span>

- Record the screen for a minute:

`byzanz-record --duration 60 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.[byzanz|flv|gif|ogg|ogv|webm]</span>

- Delay recording for 10 seconds:

`byzanz-record --delay 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.[byzanz|flv|gif|ogg|ogv|webm]</span>
