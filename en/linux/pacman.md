---
layout: page
title: linux/pacman (English)
description: "Arch Linux package manager utility."
content_hash: ca88c987122f1f0eb88a7288f2d6ff4e1872b70c
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Arch Linux package manager utility.
Some subcommands such as `pacman sync` have their own usage documentation.
More information: <https://man.archlinux.org/man/pacman.8>.

- Synchronize and update all packages:

`sudo pacman --sync --refresh --sysupgrade`

- Install a new package:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and its dependencies:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search the package database for a regular expression or keyword:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- List installed packages and versions:

`pacman --query`

- List only the explicitly installed packages and versions:

`pacman --query --explicit`

- List orphan packages (installed as dependencies but not actually required by any package):

`pacman --query --unrequired --deps --quiet`

- Empty the entire pacman cache:

`sudo pacman --sync --clean --clean`
