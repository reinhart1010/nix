---
layout: page
title: linux/aura (English)
description: "The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR."
content_hash: 5d71a38f17204a3b410a652f6782c1e8c696f3d3
related_topics:
  - title: 中文 version
    url: /zh/linux/aura.html
    icon: bi bi-globe
---
# aura

The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
More information: <https://github.com/fosskers/aura>.

- Search for packages from the official repositories and AUR:

`aura --aursync --both --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name|search_regex</span>

- Install a package from the AUR:

`aura --aursync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Install a package from the official repositories:

`aura --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Synchronize and update all packages from the official repositories:

`aura --sync --refresh --sysupgrade`

- Downgrade a package using the package cache:

`aura --downgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and its dependencies:

`aura --remove --recursive --unneeded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove orphan packages (installed as dependencies but not required by any package):

`aura --orphans --abandon`
