---
layout: page
title: linux/sestatus (English)
description: "Print the current SELinux status."
content_hash: 3fe53e287f85481965cdfae6fcf2d61a303de982
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sestatus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sestatus

Print the current SELinux status.
More information: <https://manned.org/sestatus>.

- Print the current status:

`sestatus`

- Print the current states of all policy booleans:

`sestatus -b`

- Print the current file and process contexts:

`sestatus -v`
