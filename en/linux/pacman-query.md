---
layout: page
title: linux/pacman-query (English)
description: "Arch Linux package manager utility."
content_hash: 903e77184e416b1bf5063501a9c90af2786fac34
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
---
# pacman --query

Arch Linux package manager utility.
More information: <https://man.archlinux.org/man/pacman.8>.

- List installed packages and versions:

`pacman --query`

- List only packages and versions that were explicitly installed:

`pacman --query --explicit`

- Find which package owns a file:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Display information about an installed package:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List files owned by a package:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List orphan packages (installed as dependencies but not required by any package):

`pacman --query --unrequired --deps --quiet`

- List installed packages not found in the repositories:

`pacman --query --foreign`

- List outdated packages:

`pacman --query --upgrades`
