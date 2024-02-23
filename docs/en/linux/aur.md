---
layout: page
title: linux/aur (English)
description: "Build packages from the AUR and manage local repositories."
content_hash: c23e51968091591b7d9eaec494f308e2a1f2bd37
last_modified_at: 2024-02-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aur.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aur

Build packages from the AUR and manage local repositories.
Note: A local repository needs to be set in `/etc/pacman.conf` and `vifm` needs to be installed for this to fully function.
More information: <https://github.com/aurutils/aurutils>.

- Search the AUR database for a package:

`aur search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Download a package and its dependencies from AUR, build them and add them to a local repository:

`aur sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [l]ist packages available in your local repository:

`aur repo --list`

- [u]pgrade local repository packages:

`aur sync --upgrades`
