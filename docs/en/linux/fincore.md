---
layout: page
title: linux/fincore (English)
description: "Display how much cache memory a file is taking."
content_hash: 2d31184515b1692e1eb4c08f9ec794d2895b56a0
last_modified_at: 2024-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fincore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fincore

Display how much cache memory a file is taking.
More information: <https://manned.org/fincore>.

- Display cache details for a file:

`fincore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display all possible data columns:

`fincore --output-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
