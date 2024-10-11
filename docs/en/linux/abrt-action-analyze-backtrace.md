---
layout: page
title: linux/abrt-action-analyze-backtrace (English)
description: "Analyze C/C++ backtrace."
content_hash: 599f45d1c9b485fd5e0e997a8f60322d3772a545
last_modified_at: 2024-10-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/abrt-action-analyze-backtrace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># abrt-action-analyze-backtrace

Analyze C/C++ backtrace.
Generate duplication hash, backtrace rating, and identify crash function.
Save the data as new elements `duphash`, `rating`, `crash_function` in the problem directory.
More information: <https://manned.org/abrt-action-analyze-backtrace>.

- Analyze backtrace for the current working directory:

`abrt-action-analyze-backtrace`

- Analyze backtrace for a specific directory:

`abrt-action-analyze-backtrace -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Analyze backtrace verbosely:

`abrt-action-analyze-backtrace -v`
