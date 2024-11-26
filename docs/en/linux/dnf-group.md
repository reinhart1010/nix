---
layout: page
title: linux/dnf-group (English)
description: "Manage virtual collections of packages on Fedora-based systems."
content_hash: 531c536f35f4c86dc87dd082bda29cbfadb6c332
last_modified_at: 2024-11-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf-group.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf group

Manage virtual collections of packages on Fedora-based systems.
More information: <https://manned.org/man/dnf-group>.

- List DNF groups, showing installed and uninstalled status in a table:

`dnf group list`

- Show DNF group info, including repository and optional packages:

`dnf group info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Install DNF group:

`dnf group install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Remove DNF group:

`dnf group remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Upgrade DNF group:

`dnf group upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>
