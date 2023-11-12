---
layout: page
title: linux/paru (English)
description: "An AUR helper and pacman wrapper."
content_hash: 2ec53cdbcc6d0594be3c526741d887b23b37c65a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paru

An AUR helper and pacman wrapper.
More information: <https://github.com/Morganamilo/paru>.

- Interactively search for and install a package:

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name_or_search_term</span>

- Synchronize and update all packages:

`paru`

- Upgrade AUR packages:

`paru -Sua`

- Get information about a package:

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Download `PKGBUILD` and other package source files from the AUR or ABS:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display the `PKGBUILD` file of a package:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
