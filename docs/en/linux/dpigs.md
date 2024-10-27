---
layout: page
title: linux/dpigs (English)
description: "Show which installed packages occupy the most space on `apt` based systems."
content_hash: cc620c56688a03f374d7ccbf831faa2711adc657
last_modified_at: 2024-10-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dpigs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dpigs

Show which installed packages occupy the most space on `apt` based systems.
More information: <https://manned.org/dpigs>.

- Display the N largest packages on the system:

`dpigs --lines=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Use the specified file instead of the default dpkg [s]tatus file:

`dpigs --status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the largest [S]ource packages of binary packages installed on the system:

`dpigs --source`

- Display package sizes in [H]uman-readable format:

`dpigs --human-readable`

- Display help:

`dpigs --help`
