---
layout: page
title: common/break (English)
description: "Break out of a `for`, `while`, `until` or `select` loop."
content_hash: 69d12c1d8e341f21e7e627e83d3c22384dfc1ae8
last_modified_at: 2024-12-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/break.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># break

Break out of a `for`, `while`, `until` or `select` loop.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-break>.

- Break out of a single loop:

`while :; do break; done`

- Break out of nested loops:

`while :; do while :; do break 2; done; done`
