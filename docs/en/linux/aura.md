---
layout: page
title: linux/aura (English)
description: "The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR."
content_hash: c4c610d27a4ffdb86105ea14f8bdeccd81377796
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/aura.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aura

The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
More information: <https://github.com/fosskers/aura>.

- Search for packages from the official repositories and AUR:

`aura --aursync --both --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword|regular_expression</span>

- Install a package from the AUR:

`aura --aursync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Install a package from the official repositories:

`aura --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Synchronize and update all packages from the official repositories:

`aura --sync --refresh --sysupgrade`

- Downgrade a package using the package cache:

`aura --downgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`aura --remove --recursive --unneeded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove orphan packages (installed as dependencies but not required by any package):

`aura --orphans --abandon`
