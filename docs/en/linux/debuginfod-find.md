---
layout: page
title: linux/debuginfod-find (English)
description: "Request debuginfo-related data."
content_hash: 421031ea34d1f996237febdca9d476b85c5054f6
last_modified_at: 2024-02-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debuginfod-find.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debuginfod-find

Request debuginfo-related data.
More information: <https://manned.org/debuginfod-find>.

- Request data based on the `build_id`:

`debuginfod-find -vv debuginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build_id</span>
