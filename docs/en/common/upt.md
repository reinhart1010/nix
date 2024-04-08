---
layout: page
title: common/upt (English)
description: "Unified interface for managing packages across various operating systems, like Windows, many Linux distributions, macOS, FreeBSD and even Haiku."
content_hash: 4c3644912c3c9227da319c729d87f6cc7bc4cd3c
last_modified_at: 2024-04-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/upt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># upt

Unified interface for managing packages across various operating systems, like Windows, many Linux distributions, macOS, FreeBSD and even Haiku.
It requires the native OS package manager to be installed.
See also: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
More information: <https://github.com/sigoden/upt>.

- Update the list of available packages:

`upt update`

- Search for a given package:

`upt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Show information for a package:

`upt info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a given package:

`upt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a given package:

`upt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all installed packages:

`upt upgrade`

- Upgrade a given package:

`upt upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List installed packages:

`upt list`
