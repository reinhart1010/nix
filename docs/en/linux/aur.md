---
layout: page
title: linux/aur (English)
description: "Build packages from the AUR and manage local repositories."
content_hash: 90b4198a70ad3d015f94f69dc3a7326ced2581e5
last_modified_at: 2024-04-30
related_topics:
  - title: español version
    url: /es/linux/aur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aur

Build packages from the AUR and manage local repositories.
Note: A local repository needs to be defined in `/etc/pacman.conf` and `vifm` needs to be installed for this to fully function.
More information: <https://github.com/aurutils/aurutils>.

- Search the AUR database for a package:

`aur search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Download a package and its dependencies from AUR, build them and add them to a local repository:

`aur sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [l]ist packages available in your local repository:

`aur repo --list`

- [u]pgrade local repository packages:

`aur sync --upgrades`

- Install a package without viewing changes in Vim:

`aur sync --noview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
