---
layout: page
title: common/caller (English)
description: "Print function context."
content_hash: 356de0d08ef3eece8e691db1d8816b2ee2ae6463
last_modified_at: 2024-12-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/caller.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># caller

Print function context.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-caller>.

- Print the line and filename where the current function was called:

`caller`

- Print the line, function and filename where the current function was called:

`caller 0`

- Print the line, the function name and the filename of a function call `n` frames back:

`caller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
