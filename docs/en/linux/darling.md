---
layout: page
title: linux/darling (English)
description: "Run macOS software on Linux."
content_hash: 3ea2763e7cd07a9798f7b0a0a5727ddbd5c40c3e
last_modified_at: 2024-11-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/darling.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># darling

Run macOS software on Linux.
More information: <https://darlinghq.org>.

- Run a builtin command:

`darling shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uname</span>

- Run a specific program in the current path with arguments:

`darling shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_argument_1 program_argument_2 ...</span>

- Open a macOS shell:

`darling shell`

- Shutdown the service:

`darling shutdown`
