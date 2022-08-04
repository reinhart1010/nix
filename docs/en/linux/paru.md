---
layout: page
title: linux/paru (English)
description: "An AUR helper and pacman wrapper."
content_hash: 9d95d89114de52ae25bd8feef5ea99bcea020ffa
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

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Download `PKGBUILD` and other package source files from the AUR or ABS:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Display the `PKGBUILD` file of a package:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
