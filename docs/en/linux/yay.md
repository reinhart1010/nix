---
layout: page
title: linux/yay (English)
description: "Yet Another Yogurt: A utility for Arch Linux to build and install packages from the Arch User Repository."
content_hash: 3c9f00d078d14245a43fdeba8905bb30e00797ef
last_modified_at: 2023-08-26
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
---
# yay

Yet Another Yogurt: A utility for Arch Linux to build and install packages from the Arch User Repository.
Also see `pacman`.
More information: <https://github.com/Jguer/yay>.

- Interactively search and install packages from the repos and AUR:

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name|search_term</span>

- Synchronize and update all packages from the repos and AUR:

`yay`

- Synchronize and update only AUR packages:

`yay -Sua`

- Install a new package from the repos and AUR:

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove an installed package and both its dependencies and configuration files:

`yay -Rns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a keyword from the repos and AUR:

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Remove orphaned packages (installed as dependencies but not required by any package):

`yay -Yc`

- Show statistics for installed packages and system health:

`yay -Ps`
