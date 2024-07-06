---
layout: page
title: common/git-verify-pack (English)
description: "Verify packed Git archive files."
content_hash: 7d0bc422bf1de38386c2d3f56d83549b506cab17
last_modified_at: 2024-07-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-verify-pack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git verify-pack

Verify packed Git archive files.
More information: <https://git-scm.com/docs/git-verify-pack>.

- Verify a packed Git archive file:

`git verify-pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pack-file</span>

- Verify a packed Git archive file and show verbose details:

`git verify-pack --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pack-file</span>

- Verify a packed Git archive file and only display the statistics:

`git verify-pack --stat-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pack-file</span>
