---
layout: page
title: common/continue (English)
description: "Skip to the next iteration of a `for`, `while`, `until` or `select` loop."
content_hash: 02fbdaa1c6a6202aac5e19ffa2be2c4e404e8ce8
last_modified_at: 2024-12-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/continue.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># continue

Skip to the next iteration of a `for`, `while`, `until` or `select` loop.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-continue>.

- Skip to the next iteration:

`while :; do continue; echo "This will never be reached"; done`

- Skip the next iteration from within a nested loop:

`for i in {1..3}; do while :; do continue 2; done; done`
