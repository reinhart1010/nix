---
layout: page
title: linux/fatrace (English)
description: "Report file access events."
content_hash: b44bd61cd16acd47e147d80c6369c67b5ebfdda9
last_modified_at: 2024-11-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fatrace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fatrace

Report file access events.
More information: <https://manned.org/fatrace>.

- Print file access events in all mounted filesystems to `stdout`:

`sudo fatrace`

- Print file access events on the mount of the current directory, with timestamps, to `stdout`:

`sudo fatrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--current-mount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timestamp</span>
