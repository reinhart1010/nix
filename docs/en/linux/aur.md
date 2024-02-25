---
layout: page
title: linux/aur (English)
description: "Build packages from the AUR and manage local repositories."
content_hash: 62ce334ce772535581dedc56b8c5e3e350ff3355
last_modified_at: 2024-02-25
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
