---
layout: page
title: common/dolt-gc (English)
description: "Search the repository for data that are no longer referenced and no longer needed."
content_hash: 6549e85c0c8e1b0a27910380bb06c0992058431f
last_modified_at: 2024-03-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-gc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt gc

Search the repository for data that are no longer referenced and no longer needed.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-gc>.

- Clean up unreferenced data from the repository:

`dolt gc`

- Initiate a faster but less thorough garbage collection process:

`dolt gc --shallow`
