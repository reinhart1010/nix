---
layout: page
title: common/lpq (English)
description: "Show printer queue status."
content_hash: d6deac32cfb3813a336e038d07717de1a2170094
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpq

Show printer queue status.
More information: <https://www.cups.org/doc/man-lpq.html>.

- Show the queued jobs of the default destination:

`lpq`

- Show the queued jobs of all printers enforcing encryption:

`lpq -a -E`

- Show the queued jobs in a long format:

`lpq -l`

- Show the queued jobs of a specific printer or class:

`lpq -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination[/instance]</span>

- Show the queued jobs once every n seconds until the queue is empty:

`lpq +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>
