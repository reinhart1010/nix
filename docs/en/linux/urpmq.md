---
layout: page
title: linux/urpmq (English)
description: "Query information about packages and media in Mageia."
content_hash: 577c1087accd11608db16d84439039be027233c0
last_modified_at: 2024-01-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmq

Query information about packages and media in Mageia.
See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`.
More information: <https://wiki.mageia.org/en/URPMI#urpmq>.

- Display information about an installable package:

`urpmq -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display direct dependencies of a package:

`urpmq --requires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display direct and indirect dependencies of a package:

`urpmq --requires-recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List the not installed packages needed for an RPM file with their sources:

`sudo urpmq --requires-recursive -m --sources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rpm</span>

- List all configured media with their URLs, including inactive media:

`urpmq --list-media --list-url`

- Search for a package printing [g]roup, version and [r]elease:

`urpmq -g -r --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search for a package with using its exact name:

`urpmq -g -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
