---
layout: page
title: linux/aurman (English)
description: "An Arch Linux utility to build and install packages from the Arch User Repository."
content_hash: b0d735eea717460c5a26ff6ed8e0a7262b57188c
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/aurman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurman

An Arch Linux utility to build and install packages from the Arch User Repository.
See also `pacman`.
More information: <https://github.com/polygamma/aurman>.

- Synchronize and update all packages:

`aurman --sync --refresh --sysupgrade`

- Synchronize and update all packages without show changes of `PKGBUILD` files:

`aurman --sync --refresh --sysupgrade --noedit`

- Install a new package:

`aurman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a new package without show changes of `PKGBUILD` files:

`aurman --sync --noedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a new package without prompting:

`aurman --sync --noedit --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a keyword from the official repositories and AUR:

`aurman --sync --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Remove a package and its dependencies:

`aurman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Clear the package cache (use two `--clean` flags to clean all packages):

`aurman --sync --clean`
